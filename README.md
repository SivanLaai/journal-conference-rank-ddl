# Journal-Conference-Rank-Deadlines

[![LICENSE](https://img.shields.io/github/license/ccfddl/ccf-deadlines)](https://github.com/ccfddl/ccf-deadlines/blob/main/LICENSE) 
Based on [CCFDDL](https://github.com/ccfddl/ccf-deadlines)

# 为什么?
- CCFDDL显示太多的会议了，且有些自己关注的会议有延期不会及时更新，对于大部分研究人员说，只关心自己本领域的会议
- 添加自己关注的领域的期刊列表，支持添加期刊审稿周期、期刊篇幅、期刊投稿网址和接受率
- 期刊和会议，支持添加备注

简体中文 | [English](./README.md)

帮助需要关注自己本领域的科研人员追踪会议的投稿时间，同时关注收集自己的意向期刊。

[网站预览 (主页)](https://eda.laais.cn/)
<!-- | <div style="width:330px">[网站预览 (主页)](https://ccfddl.github.io/)</div> | <div style="width:330px">[表格预览](https://ccfddl.top/) <br> [无需科学上网]</div> |
| :----: | :----: |
| <img src=".readme_assets/screenshot_website.png" width="300px"/> | <img src=".readme_assets/screenshot_tabular.png" width="300px"/> | -->


**构建一个属于自己的科研规划平台!**

## 会议录入文件

文件: data/confs.yml

```yaml
- title: SIGMOD
  description: ACM Conference on Management of Data
  sub: DB
  rank: A
  dblp: sigmod
  remark: 系统领域顶会
  confs:
    - year: 2022
      id: sigmod22
      link: http://2022.sigmod.org/
      timeline:
        - deadline: '2021-07-02 17:00:00'
          comment: 'first round'
        - deadline: '2021-09-15 17:00:00'
          comment: 'second round'
      timezone: UTC-8
      date: June 12-17, 2022
      place: Philadelphia, PA, USA
```

字段描述:

<table>
   <tr>
      <th colspan="3">字段名</th>
      <th>描述</th>
   </tr>
   <tr>
      <td colspan="3"><code>title</code>*</td>
      <td>缩写的会议名称, 不需要年份, 大写</td>
   </tr>
   <tr>
      <td colspan="3"><code>description</code>*</td>
      <td>介绍, 或全称, 无需第几届</td>
   </tr>
   <tr>
      <td colspan="3"><code>sub</code>*</td>
      <td>会议在CCF中被标注的类别, 可参考下面的辅助文档</td>
   </tr>
   <tr>
      <td colspan="3"><code>rank</code>*</td>
      <td>会议在CCF中被标注的等级, 示例, <code>A</code>, <code>B</code>, <code>C</code></td>
   </tr>
   <tr>
      <td colspan="3"><code>dblp</code>*</td>
      <td>会议在dblp的URL的后缀, 示例, <code>iccv</code> in https://dblp.uni-trier.de/db/conf/iccv</td>
   </tr>
   <tr>
      <td colspan="3"><code>remark</code>*</td>
      <td>添加对于会议的一些备注, 示例, 会议难度较大 </td>
   </tr>
   <tr>
      <td rowspan="9"><code>confs</code></td>
      <td colspan="2"><code>year</code>*</td>
      <td>会议的年份</td>
   </tr>
   <tr>
      <td colspan="2"><code>id</code>*</td>
      <td>会议名字和年份, 小写</td>
   </tr>
   <tr>
      <td colspan="2"><code>link</code>*</td>
      <td>会议首页的URL</td>
   </tr>
   <tr>
      <td rowspan="3"><code>timeline</code>*</td>
      <td><code>abstract_deadline</code></td>
      <td>Abstract的截稿日期, 可选填</td>
   </tr>
   <tr>
      <td><code>deadline</code>*</td>
      <td>截稿日期, 格式为 <code>yyyy-mm-dd hh:mm:ss</code> or <code>TBD</code></td>
   </tr>
   <tr>
      <td><code>comment</code></td>
      <td>额外的一些辅助信息, 可选填</td>
   </tr>
   <tr>
      <td colspan="2"><code>timezone</code>*</td>
      <td>截稿日期的时区, 目前支持 <code>UTC-12</code> ~ <code>UTC+12</code> & <code>AoE</code></td>
   </tr>
   <tr>
      <td colspan="2"><code>date</code>*</td>
      <td>会议举办的日期, 示例, Mar 12-16, 2021</td>
   </tr>
   <tr>
      <td colspan="2"><code>place</code>*</td>
      <td>会议举办的地点, 示例, <code>city, country</code></td>
   </tr>
</table>

## 期刊录入文件

文件: data/jours.yml

```yaml
- title: JSSC
  description: IEEE Journal of Solid-State Circuits
  acceptance_rate: 0.15
  submission: https://submission.com
  dblp: jssc
  page: 15
  review_duration: 6
  ranks:
  - casQ1
  remark: 一区Top，最顶级期刊没有之一，实至名归没有什么好说的
  sub: DS
  id: jssc
  link: https://journal.home.com
```

字段描述:

<table>
   <tr>
      <th colspan="3">字段名</th>
      <th>描述</th>
   </tr>
   <tr>
      <td colspan="3"><code>title</code>*</td>
      <td>缩写的期刊名称, 大写</td>
   </tr>
   <tr>
      <td colspan="3"><code>description</code>*</td>
      <td>介绍, 或全称</td>
   </tr>
   <tr>
      <td colspan="3"><code>acceptance_rate</code>*</td>
      <td>接受率, 如0.15 表示 接收率15%</td>
   </tr>
   <tr>
      <td colspan="3"><code>page</code>*</td>
      <td>期刊的要求篇幅页码</td>
   </tr>
   <tr>
      <td colspan="3"><code>review_duration</code>*</td>
      <td>审稿周期</td>
   </tr>
   <tr>
      <td colspan="3"><code>submission</code>*</td>
      <td>期刊投搞网址</td>
   </tr>
   <tr>
      <td colspan="3"><code>sub</code>*</td>
      <td>期刊在CCF中被标注的类别, 可参考下面的辅助文档</td>
   </tr>
   <tr>
      <td colspan="3"><code>rank</code>*</td>
      <td>期刊在CCF\JCR\中科院分区表中被标注的等级和影响因子, <code>CCF: A\B\C</code>, 中科院分区: <code> casQ1\casQ2\casQ3\casQ4</code>, JCR: <code>jcrQ1\jcrQ2\jcrQ3\jcrQ4</code>, 影响因子: <code>IF 5.5</code></td>
   </tr>
   <tr>
      <td colspan="3"><code>dblp</code>*</td>
      <td>期刊在dblp的URL的后缀, 示例, <code>jssc</code> in https://dblp.uni-trier.de/db/journal/jssc</td>
   </tr>
   <tr>
      <td colspan="3"><code>remark</code>*</td>
      <td>添加对于期刊的一些备注, 示例, 期刊难度较大 </td>
   </tr>
</table>

带星标(*)的字段是必填项。

## 类别匹配表:

| `sub` | 类别名称 |
| ----------- | --------------------------------------------------------- |
| `DS`        | 计算机体系结构/并行与分布计算/存储系统                    |
| `NW`        | 计算机网络                                                |
| `SC`        | 网络与信息安全                                            |
| `SE`        | 软件工程/系统软件/程序设计语言                            |
| `DB`        | 数据库/数据挖掘/内容检索                                  |
| `CT`        | 计算机科学理论                                            |
| `CG`        | 计算机图形学与多媒体                                      |
| `AI`        | 人工智能                                                  |
| `HI`        | 人机交互与普适计算                                        |
| `MX`       | 交叉/综合/新兴                                            |

## License

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fccfddl%2Fccf-deadlines.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fccfddl%2Fccf-deadlines?ref=badge_large)
