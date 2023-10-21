<template>
  <section>
    <el-checkbox style="padding-top: 10px;width: 33%" :indeterminate="isIndeterminate" v-model="checkAll"
      @change="handleCheckAllChange"><span style="color: #666666">全选</span></el-checkbox>

    <el-checkbox-group v-model="checkList" @change="handleCheckedChange">
      <el-checkbox class="boxes" size="medium" v-for="item in subList" :label="item.sub" :key="item.sub"><span
          style="color: #666666">{{ formatSubName(item) }}</span></el-checkbox>
    </el-checkbox-group>
    <el-row class="timezone">
      <div style="float: left">
        Deadlines are shown in {{ timeZone }} time.
      </div>
      <div style="float: left; width: 155px">
        <el-input prefix-icon="el-icon-search" size="mini" v-model="input" placeholder="search conference"
          @change="handleInputChange">
        </el-input>
      </div>
      <div style="float: right">
        <el-checkbox-group v-model="rankList" size="mini" @change="handleRankChange" class="rankbox">
          <el-checkbox-button v-for="(rank, index) in rankoptions" :label="index" :key="index">{{ rank
          }}</el-checkbox-button>
        </el-checkbox-group>
      </div>
    </el-row>
    <el-row class="zonedivider"></el-row>
    <el-table :data="showList" :show-header="false" style="width: 100%">
      <!-- <el-table-column type="expand">
        <template slot-scope="scope">
          <el-form label-position="right" inline class="demo-table-expand">
            <el-form-item>
              <span>{{ scope.row.remark }}</span>
            </el-form-item>
          </el-form>
        </template>
      </el-table-column> -->
      <el-table-column>
        <template slot-scope="scope">
          <el-row class="conf-title">
            <a :href="scope.row.link">{{ scope.row.title }}</a>
            <!-- <svg-icon style="width: 200px; height: 200px;" icon-class="dblp" /> -->
            <i @click="jump2DBLP(scope.row.dblp)">
              <svg-icon icon-class="dblp" />
            </i>
            <i @click="open(scope.row.remark, scope.row.title)">
              <svg-icon icon-class="note" />
            </i>
            <i v-if="scope.row.isLike === true" @click="handleClickIcon(scope.row, true)">
              <svg-icon icon-class="star-on" />
            </i>
            <i v-else @click="handleClickIcon(scope.row, false)">
              <svg-icon icon-class="star-off" />
            </i>
          </el-row>
          <el-row class="conf-des">{{ scope.row.description }}</el-row>
          <el-row>
            <el-tag size="mini" :key="displayrank" v-for="displayrank in scope.row.displayranks" type="" effect="plain">{{
              displayrank }}</el-tag>
            <span style="color: #409eff" v-show="scope.row.comment"><b>NOTE:</b> {{ scope.row.comment }}</span>
          </el-row>
          <el-row style="padding-top: 5px">
            <span class="conf-sub" style="padding-left: 5px">{{ scope.row.subname }}</span>
          </el-row>
          <!-- <el-button type="text" @click="open">点击打开 Message Box</el-button> -->

        </template>
      </el-table-column>
      <el-table-column>
        <template slot-scope="scope">
          <el-row>
            <el-col>submission: <a :href="scope.row.submission">{{ scope.row.submission }}</a></el-col>
          </el-row>
          <el-row>
            <el-col>acceptance rate: {{ scope.row.acceptance_rate * 100 }}%</el-col>
          </el-row>
          <el-row>
            <el-col>review duration: {{ scope.row.review_duration }}</el-col>
          </el-row>
          <el-row>
            <el-col>average page: {{ scope.row.page }}</el-col>
          </el-row>
        </template>
      </el-table-column>
    </el-table>
    <el-row style="padding-top: 8px">
      <div style="float: right">
        <el-pagination background small layout="prev, pager, next" :page-size=pageSize
          @current-change="handleCurrentChange" :current-page="page" :total=showNumber>
        </el-pagination>
      </div>
    </el-row>

  </section>
</template>

<script>
const yaml = require('js-yaml')
const moment = require('moment-timezone')
const tz = moment.tz.guess()
export default {
  name: "Journal",
  components: {
  },
  data() {
    return {
      publicPath: '/data/',
      checkAll: true,
      isIndeterminate: false,
      pageSize: 10,
      page: 1,
      checkList: [],
      subList: [],
      allconfList: [],
      showList: [],
      showNumber: 0,
      typeMap: new Map(),
      timeZone: '',
      utcMap: new Map(),
      rankoptions: { 'A': 'CCF A', 'B': 'CCF B', 'C': 'CCF C', 'N': 'Non-CCF', 'casQ1': '1区', 'casQ2': '2区', 'casQ3': '3区', 'casQ4': '4区' },
      typesList: [],
      rankList: [],
      cachedLikes: [],
      cachedRanks: [],
      input: '',
      iconName: 'dblp'
    }
  },
  methods: {
    open(remark, title) {
      this.$alert(remark, title, {
        confirmButtonText: 'OK',
        // callback: action => {
        //   this.$message({
        //     type: 'info',
        //     message: `action: ${action}`
        //   });
        // }
      });
    },
    jump2DBLP(dblp) {
      let dblpUrl = this.generateDBLP(dblp)
      window.open(dblpUrl)
    },
    loadFile() {
      this.timeZone = tz
      this.$http.get(this.publicPath + 'types.yml').then(response => {
        const doc = yaml.load(response.body)
        this.subList = doc
        for (let i = 0; i < this.subList.length; i++) {
          this.checkList.push(this.subList[i].sub)
          this.typesList.push(this.subList[i].sub)
          this.typeMap.set(this.subList[i].sub, this.subList[i].name)
        }
        this.loadCachedTypes()
        this.getAllConf()

      }, () => {
        alert('sorry your network is not stable!')
      })
    },
    getAllConf() {
      // get all conf
      this.$http.get(this.publicPath + 'jours.yml').then(response => {
        const allconf = yaml.load(response.body)
        // preprocess

        for (let i = 0; i < allconf.length; i++) {
          let curItem = allconf[i]
          curItem.displayranks = []
          curItem.subname = this.typeMap.get(curItem.sub)
          curItem.isLike = false
          for (let j = 0; j < curItem.ranks.length; j++) {
            let currRank = curItem.ranks[j]
            let displayrank = this.rankoptions[currRank]
            if (currRank.indexOf("cas") !== -1) {
              displayrank = "中科院" + displayrank
            }
            if (displayrank)
              curItem.displayranks.push(displayrank)
            else {
              displayrank = currRank.replace("jcr", "JCR").replace("Q", " Q")
              curItem.displayranks.push(displayrank)
            }
          }
          // check cachedLikes
          if (this.cachedLikes && this.cachedLikes.indexOf(curItem.title + curItem.id) >= 0) {
            curItem.isLike = true
          } else {
            curItem.isLike = false
          }
          this.allconfList.push(curItem)
        }
        this.showConf(this.typesList, this.rankList, this.input, 1)
      }, () => {
        alert('sorry your network is not stable!')
      })
    },
    showConf(types, rank, input, page) {
      let filterList = []
      filterList.push.apply(filterList, this.allconfList)

      if (types != null && types.length != 0) {
        filterList = filterList.filter(function (item) { return types.indexOf(item.sub.toUpperCase()) >= 0 })
      }

      if (rank != null && rank.length > 0) {
        filterList = filterList.filter(function (item) {
          let count = 0
          for (let i = 0; i <= item.ranks.length; ++i) {
            count += rank.indexOf(item.ranks[i]) >= 0 ? 1 : 0
          }
          return count > 0
        })
      }

      if (input != null && input.length > 0) {
        filterList = filterList.filter(function (item) {
          return item.id.toLowerCase().indexOf(input.toLowerCase()) >= 0
        })
      }

      this.showList = []
      let likesList = []

      let allList = filterList

      for (let i = allList.length - 1; i >= 0; i--) {
        let curDoc = allList[i]
        if (curDoc.isLike === true) {
          likesList.push(curDoc)
          allList.splice(i, 1)
        }
      }
      likesList.reverse()
      likesList.push.apply(likesList, allList)
      this.showList = likesList
      this.showNumber = this.showList.length
      this.showList = this.showList.slice(this.pageSize * (page - 1), this.pageSize * page)
      this.page = page
    },
    transform(props) {
      Object.entries(props).forEach(([key, value]) => {
        // Adds leading zero
        const digits = value < 10 ? `0${value}` : value
        // uses singular form when the value is less than 2
        const word = value < 2 ? key.replace(/s$/, '') : key
        if (word[0] === 'd') {
          props[key] = `${digits} ${word}`
        } else {
          props[key] = `${digits} ${word[0]}`
        }
      })
      return props
    },
    loadUTCMap() {
      for (let i = -12; i <= 12; i++) {
        if (i >= 0) {
          this.utcMap.set('UTC+' + i, '+' + (Array(2).join(0) + i).slice(-2) + '00')
        } else {
          this.utcMap.set('UTC' + i, '-' + (Array(2).join(0) + i * -1).slice(-2) + '00')
        }
      }
      this.utcMap.set('AoE', '-1200')
      this.utcMap.set('UTC', '+0000')
    },
    handleCheckedChange(types) {
      this.typesList = types
      let checkedCount = types.length
      this.checkAll = checkedCount === this.subList.length
      this.isIndeterminate = checkedCount > 0 && checkedCount < this.subList.length
      this.$ls.set('joursTypes', Array.from(this.typesList))
      this.showConf(this.typesList, this.rankList, this.input, 1)
    },
    handleInputChange() {
      this.showConf(this.typesList, this.rankList, this.input, 1)
    },
    handleRankChange(rank) {
      this.rankList = rank
      this.$ls.set('joursRanks', Array.from(this.rankList))
      this.showConf(this.typesList, this.rankList, this.input, 1)
    },
    handleCurrentChange(page) {
      this.showConf(this.typesList, this.rankList, this.input, page)
    },
    handleCheckAllChange() {
      this.typesList = (this.checkList.length === this.subList.length) ? [] : this.subList.map((obj) => { return obj.sub }).join(",").split(',');
      this.checkList = this.typesList
      this.isIndeterminate = false
      this.$ls.set('joursTypes', Array.from(this.typesList))
      this.showConf(this.typesList, this.rankList, this.input, 1)
    },
    handleClickIcon(record, judge) {
      if (judge === true) {
        record.isLike = false
        let index = this.cachedLikes.indexOf(record.title + record.id)
        if (index > -1) this.cachedLikes.splice(index, 1)
        this.$ls.set('joursLikes', Array.from(new Set(this.cachedLikes)))
      } else {
        record.isLike = true
        this.cachedLikes.push(record.title + record.id)
        this.$ls.set('joursLikes', Array.from(new Set(this.cachedLikes)))
      }
    },
    generateDBLP(name) {
      return 'https://dblp.uni-trier.de/db/journals/' + name
    },
    _isMobile() {
      let flag = navigator.userAgent.match(/(phone|pad|pod|iPhone|iPod|ios|iPad|Android|Mobile|BlackBerry|IEMobile|MQQBrowser|JUC|Fennec|wOSBrowser|BrowserNG|WebOS|Symbian|Windows Phone)/i)
      return flag;
    },
    formatSubName(item) {
      if (this._isMobile()) {
        return item.sub
      } else {
        return item.name
      }
    },
    loadCachedTypes() {
      let tmpList = this.$ls.get('joursTypes')
      if (tmpList) {
        this.typesList = tmpList
        this.checkList = this.typesList
        let checkedCount = this.checkList.length
        this.checkAll = checkedCount === this.subList.length
        this.isIndeterminate = checkedCount > 0 && checkedCount < this.subList.length
      }
    },
    loadCachedLikes() {
      this.cachedLikes = this.$ls.get('joursLikes')
      if (!this.cachedLikes) this.cachedLikes = []
    },
    loadCachedRanks() {
      this.cachedRanks = this.$ls.get('joursRanks')
      if (!this.cachedRanks) this.cachedRanks = []
      this.rankList = this.cachedRanks
    },
  },
  mounted() {
    // this.loadCachedTypes()
    this.loadCachedRanks()
    this.loadCachedLikes()
    this.loadUTCMap()
    this.loadFile()
  }
}
</script>

<style scoped>
/*/deep/ .el-table tbody tr { pointer-events:; }*/
/deep/ .el-input--mini .el-input__inner {
  height: 20px;
  line-height: 20px;
}

/deep/ .el-input--mini .el-input__icon {
  line-height: 20px;
}

/deep/ .el-checkbox__inner {
  height: 20px;
  width: 20px;
}

/deep/ .el-button {
  height: 20px;
  padding: 0px 5px;
}

/deep/ .el-checkbox-button--mini .el-checkbox-button__inner {
  padding: 3px 10px;
}

/deep/ .el-checkbox__inner::after {
  -webkit-box-sizing: content-box;
  box-sizing: content-box;
  content: "";
  border: 3px solid #FFF;
  border-left: 0;
  border-top: 0;
  height: 11px;
  left: 6px;
  position: absolute;
  top: 1px;
  -webkit-transform: rotate(45deg) scaleY(0);
  transform: rotate(45deg) scaleY(0);
  width: 4px;
  -webkit-transition: -webkit-transform .15s ease-in .05s;
  transition: -webkit-transform .15s ease-in .05s;
  transition: transform .15s ease-in .05s, -webkit-transform .15s ease-in .05s;
  -webkit-transform-origin: center;
  transform-origin: center;
}

/deep/ .el-checkbox__input.is-indeterminate .el-checkbox__inner::before {
  height: 6px;
  top: 6px;
}

.icon:hover {
  color: rgb(64, 158, 255);
}

.rankbox {
  padding-top: 1px;
}

.boxes {
  width: 33%;
  margin-right: 0px;
  padding-top: 10px;
}

.timezone {
  padding-top: 15px;
  color: #666666;
}

.zonedivider {
  margin-top: 8px;
  border-bottom: 1px solid #ebeef5;
}

.conf-title {
  font-size: 20px;
  font-weight: 400;
  color: black;
}

a {
  text-decoration: none;
  border-bottom: 1px solid #ccc;
  color: inherit;
}

.conf-des {
  font-size: 13px;
}

.conf-sub {
  color: rgb(36, 101, 191);
  background: rgba(236, 240, 241, 0.7);
  font-size: 13px;
  padding: 3px 5px;
  cursor: pointer;
  font-weight: 400;
}

.conf-timer {
  font-size: 20px;
  font-weight: 400;
}

.conf-fin {
  opacity: 0.4;
}
</style>
