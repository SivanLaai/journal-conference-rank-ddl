import string
import requests
import yaml
from termcolor import colored
from argparse import ArgumentParser
from datetime import datetime
from datetime import timezone
from models import *
from lxml import etree
from sqlalchemy import and_

from io import StringIO, BytesIO
class Crawler:
    def __init__(self, sql_url, source_url):
        try:
            self.source_url = source_url
            self.db = initDB(sql_url)
        except Exception as e:
            print(e)
            self.db = None
    def parseTz(self, tz):
        if tz == "AoE":
            return "-1200"
        elif tz.startswith("UTC-"):
            return "-{:04d}".format(int(tz[4:]))
        elif tz.startswith("UTC+"):
            return "+{:04d}".format(int(tz[4:]))
        else:
            return "+0000"




    def formatDuraton(self, ddl_time: datetime, now: datetime) -> str:
            duration = ddl_time - now
            months, days= duration.days // 30, duration.days
            hours, remainder= divmod(duration.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            day_word_str = "days" if days > 1 else "day "
            # for alignment
            months_str, days_str, = str(months).zfill(2), str(days).zfill(2)
            hours_str, minutes_str = str(hours).zfill(2), str(minutes).zfill(2)

            if days < 1:
                return colored(f'{hours_str}:{minutes_str}:{seconds}', "red")
            if days < 30:
                return colored(f'{days_str} {day_word_str}, {hours_str}:{minutes_str}', "yellow")
            if days < 100:
                return colored(f"{days_str} {day_word_str}", "blue")
            return colored(f"{months_str} months", "green")
        
            
    def format_header(self, header_str):
        header = dict()
        for line in header_str.split('\n'):
            header[line.split(':')[0]] = ":".join(line.split(':')[1:])
        return header
    
    def format_params(self, params_str):
        params = dict()
        for line in params_str.split('\n'):
            params[line.split('=')[0]] = line.split('=')[1]
        return params
    
    def parseSingleNode(self, curr_tree, parser):
        confNode = curr_tree.xpath("//small/center")
        if not len(confNode):
            return None
        name = confNode[0].text
        curr_html = etree.tostring(confNode[1])
        link_tree = etree.parse(StringIO(str(curr_html)), parser=parser)
        link = link_tree.xpath("//i/a")[0].text
        curr_html = etree.tostring(confNode[2])
        ddl_tree = etree.parse(StringIO(str(curr_html)), parser=parser)
        deadline = ddl_tree.xpath("//b")[0].text
        date = confNode[3].text

        curr_basic_dict = dict()
        curr_basic_dict['year'] = date[:4]
        if "MICRO" in name:
            name = "MICRO"
        else:
            name = name.replace(date[:4], "").strip()
        curr_basic_dict['name'] = name
        curr_basic_dict['id'] = name.lower().replace("-", "").replace(" ", "")
        curr_basic_dict['link'] = link
        curr_basic_dict['deadline'] = deadline 
        curr_basic_dict['date'] = date

        return curr_basic_dict

    def crawlConferenceFromWebsite(self):
        final_datas = list()
        try:
            head='''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cache-Control: max-age=0
Connection: keep-alive
Host: www.cse.chalmers.se
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46
sec-ch-ua: "Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"'''.replace(": ",":")
            header = self.format_header(head)
            html = requests.get(self.source_url, headers=header).content.decode("utf-8")
            parser = etree.HTMLParser()
            tree = etree.parse(StringIO(str(html)), parser=parser)
            if tree is None:
                return final_datas
            x_path = '//table//tr'
            treeNodes = tree.xpath(x_path)
            for curr_node in treeNodes:
                curr_html = etree.tostring(curr_node)
                curr_tree = etree.parse(StringIO(str(curr_html)), parser=parser)
                curr_conference = self.parseSingleNode(curr_tree, parser)
                if not curr_conference:
                    continue
                id = curr_conference["id"]
                year = curr_conference["year"]

                confs = self.db.query(Conference).filter(Conference.id==id).all()
                if not len(confs):
                    self.db.bulk_insert_mappings(Conference, [dict(id=id, name=curr_conference["name"])])
                    self.db.commit()

                confs = self.db.query(ConferenceDetail).filter(ConferenceDetail.id==id, ConferenceDetail.year==year).all()
                del curr_conference["name"]
                if len(confs):
                    self.db.query(ConferenceDetail).filter(ConferenceDetail.id==id, ConferenceDetail.year==year).update(curr_conference)
                    self.db.commit()
                else:
                    self.db.bulk_insert_mappings(ConferenceDetail, [curr_conference])
                    self.db.commit()
        except Exception as e:
            print(e)
            
        return final_datas
        
    def crawlConferenceFromCCFDDL(self):
        if not self.db:
            print("sql session is None, Exit")
            return
        yml_str = requests.get(
            "https://ccfddl.github.io/conference/allconf.yml").content.decode("utf-8")
        all_conf = yaml.safe_load(yml_str)

        eda_confs = [conf.name for conf in self.db.query(Conference).all()]
        self.db.commit()
        for conf in all_conf:
            if conf["title"] not in eda_confs:
                continue
            curr_db_conf = self.db.query(Conference).filter(Conference.name==conf["title"]).all()
            print(conf)
            if len(curr_db_conf):
                curr_db_conf_data = dict()
                curr_db_conf_data["id"] = conf["dblp"]
                curr_db_conf_data["dblp"] = conf["dblp"]
                curr_db_conf_data["ccf"] = conf["rank"]["ccf"]
                curr_db_conf_data["full_name"] = conf["description"]
                curr_db_conf_data["sub"] = conf["sub"]
                self.db.query(Conference).filter(Conference.name==conf["title"]).update(curr_db_conf_data)
            for c in conf["confs"]:
                id = conf["dblp"].lower().replace(" ","").replace("-","").replace("/","")
                year = c["year"]
                data = dict()
                data["link"] = c["link"]
                data["timezone"] = c["timezone"]
                data["place"] = c["place"]
                data["date"] = c["date"]
                if len(c["timeline"]) == 1:
                    data["deadline"] = list(c["timeline"][0].values())[0]
                elif len(c["timeline"]) == 2:
                    data["abstract_deadline"] = list(c["timeline"][0].values())[0]
                    data["deadline"] = list(c["timeline"][1].values())[0]
                elif len(c["timeline"]) > 2:
                    data["abstract_deadline"] = list(c["timeline"][0].values())[0]
                    data["deadline"] = list(c["timeline"][1].values())[0]
                    for i in range(2, len(c["timeline"])):
                        data["extended_deadline"] = list(c["timeline"][i].values())[0]
                confs = self.db.query(ConferenceDetail).filter(ConferenceDetail.id==id, ConferenceDetail.year==int(year)).all()
                if data["deadline"] == "TBD":
                   data["deadline"] = None
                if len(confs):
                    # f.write(f"{id},{year}\n")
                    # f.write(f"query: {confs[0].id},{confs[0].year}\n\n")
                    self.db.query(ConferenceDetail).filter(ConferenceDetail.id==id, ConferenceDetail.year==int(year)).update(data)
                    self.db.commit()
                else:
                    data["id"] = id
                    data["year"] = year
                    self.db.bulk_insert_mappings(ConferenceDetail, [data])
                    self.db.commit()

    def getConferenceList(self):
        if not self.db:
            print("sql session is None, Exit")
            return
        eda_confs = [conf for conf in self.db.query(Conference).all()]
        self.db.commit()
        Confs = dict()
        for i in range(len(eda_confs)):
            conf = eda_confs[i]
            if conf.id not in Confs:
                curr_j = dict()
                curr_j["title"] = conf.name
                curr_j["description"] = conf.full_name
                curr_j["dblp"] = conf.dblp
                curr_j["sub"] = conf.sub
                if not conf.sub:
                    curr_j["sub"] = "DS"
                curr_j["rank"] = conf.ccf
                if not conf.ccf:
                    curr_j["rank"] = "N"
                curr_j["home_link"] = conf.home_link
                curr_j["remark"] = conf.remark
                curr_j["confs"] = list()
                Confs[conf.id] = curr_j
            confsDetail = self.db.query(ConferenceDetail).filter(ConferenceDetail.id==conf.id).all()
            for curr in confsDetail:
                curr_conf = dict()
                curr_conf["year"] = curr.year
                curr_conf["id"] = curr.id+str(curr.year)
                curr_conf["link"] = curr.link
                timeline = list()
                if curr.abstract_deadline:
                    timeline.append(dict(deadline=str(curr.abstract_deadline), comment="Abstract Deadline"))
                if curr.deadline:
                    timeline.append(dict(deadline=str(curr.deadline), comment="Full Paper Deadline"))
                if curr.extended_deadline:
                    for cur_ext_ddl in curr.extended_deadline.split(";"):
                        if len(cur_ext_ddl):
                            timeline.append(dict(deadline=cur_ext_ddl, comment="Extended Full Paper Deadline"))
                if not len(timeline):
                    timeline.append(dict(deadline=f'2023-01-01 23:59:59', comment="Full Paper Deadline"))
                curr_conf["timeline"] = timeline
                curr_conf["timezone"] = curr.timezone
                if not curr.timezone:
                    curr_conf["timezone"] = "UTC+8"
                curr_conf["date"] = curr.date
                curr_conf["place"] = curr.place
                Confs[conf.id]["confs"].append(curr_conf)
        return list(Confs.values())

    def getJournalList(self):
        if not self.db:
            print("sql session is None, Exit")
            return
        eda_jours = [jour for jour in self.db.query(Journal).all()]
        self.db.commit()
  
        Jours = list()
        for i in range(len(eda_jours)):
            jour = eda_jours[i]
            curr_j = dict()
            curr_j["title"] = jour.name
            curr_j["description"] = jour.full_name
            curr_j["acceptance_rate"] = jour.acceptance_rate
            curr_j["submission"] = jour.submission
            curr_j["dblp"] = jour.dblp
            curr_j["page"] = jour.page
            curr_j["review_duration"] = jour.review_duration
            curr_j["ranks"] = list()
            if jour.ccf:
                curr_j["ranks"].append(jour.ccf)
            if jour.cas:
                curr_j["ranks"].append("cas" + jour.cas)
            if jour.jcr:
                curr_j["ranks"].append("jcr" + jour.jcr)
            if jour._if:
                curr_j["ranks"].append("IF " + jour._if)
            if not len(curr_j["ranks"]):
                curr_j["ranks"].append('N')
            if jour.remark:
                curr_j["remark"] = jour.remark
            curr_j["sub"] = "DS"
            curr_j["id"] = jour.id
            curr_j["link"] = jour.home_link
            Jours.append(curr_j)
        return Jours

    # save yaml info to mysql
    def saveConferenceAndJournalInfoToDatabase(self):
        try:

            # yaml.dump(Jours, sort_keys=False, allow_unicode=True)
            with open(r'data/jours.yml', 'rb') as file:
                jours = yaml.load(file.read(), Loader=yaml.FullLoader)
                format_jours = list()
                for jour in jours:
                    curr_jour = dict()
                    curr_jour["id"] = jour["id"]
                    curr_jour["name"] = jour["title"]
                    curr_jour["full_name"] = jour["description"]
                    curr_jour["submission"] = jour["submission"]
                    curr_jour["home_link"] = jour["link"]
                    curr_jour["acceptance_rate"] = jour["acceptance_rate"]
                    curr_jour["review_duration"] = jour["review_duration"]
                    ranks = jour["ranks"]
                    print(ranks)
                    for rank in ranks:
                        if "cas" in rank:
                            curr_jour["cas"] = rank.replace("cas", "")
                        elif "jcr" in rank:
                            curr_jour["jcr"] = rank.replace("jcr", "")
                        elif "IF" in rank:
                            curr_jour["if"] = rank.replace("IF ", "")
                        else:
                            curr_jour["ccf"] = rank
                    format_jours.append(curr_jour)
                # db_jours = self.db.query(Journal).filter(Conference.id==id).all()
                db_jours = self.db.query(Journal).all()
                if not len(db_jours):
                    self.db.bulk_insert_mappings(Journal, format_jours)
                    self.db.commit()
                else:
                    for jour in format_jours:
                        self.db.query(Journal).filter(Journal.id==jour["id"]).update(jour)
                        self.db.commit()

            # Confs = self.getConferenceList()

            # with open(r'data/confs.yml', 'w') as file:
            #     yaml.safe_dump(list(Confs), file, sort_keys=False, allow_unicode=True)
        except Exception as e:
            print(e)
    
    def saveConferenceAndJournalInfo(self):
        try:
            Jours = self.getJournalList()

            # yaml.dump(Jours, sort_keys=False, allow_unicode=True)
            with open(r'data/jours.yml', 'w') as file:
                yaml.safe_dump(Jours, file, sort_keys=False, allow_unicode=True)

            Confs = self.getConferenceList()
            # yaml.dump(list(Confs), sort_keys=False, allow_unicode=True)
            with open(r'data/confs.yml', 'w') as file:
                yaml.safe_dump(list(Confs), file, sort_keys=False, allow_unicode=True)
        except Exception as e:
            print(e)



def parse_args():
    parser = ArgumentParser(description="cli for eda")
    parser.add_argument("--sql_url", type=str, help="SQL connect url", default=None)
    parser.add_argument("--source_url", type=str, help="Web source url", default=None)
    args = parser.parse_args()
    # Convert all arguments to lowercase
    # for arg_name in vars(args):
    #     arg_value = getattr(args, arg_name)
    #     if arg_value:
    #         setattr(args, arg_name, [arg.lower() for arg in arg_value])
    return args
if "__main__" == __name__:
    args = parse_args()
    crawler = Crawler(args.sql_url, args.source_url)
    info = crawler.crawlConferenceFromWebsite()
    info = crawler.crawlConferenceFromCCFDDL()
    info = crawler.saveConferenceAndJournalInfo()
    # crawler.saveConferenceAndJournalInfoToDatabase()
