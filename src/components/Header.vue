<template>
  <section>
    <el-row>
      <a href="/" class="title">研究领域的相关会议和期刊</a>
    </el-row>
    <el-row class="subtitle">
      收集个人所关注领域相关的会议和期刊，以较清晰的逻辑列表展示，辅助科研
      <svg-icon style="height: 20px; width: 20px;" icon-class="celebration" />
      <svg-icon style="height: 20px; width: 20px;" icon-class="cheers" />
      <p>
      （点击下方按纽可以在会议和期刊之间来回切换）
      </p>
    </el-row>
  </section>
</template>

<script>
export default {
  name: 'Header',
  data() {
    return {
      showLatestConf: false,
      showStr: ''
    }
  },
  mounted() {
    this.$http.get('https://api.github.com/repos/ccfddl/ccf-deadlines/commits?page=1&per_page=10').then(response => {
      let len = response.body.length

      for(let i = 0; i < len; i++) {
        let str = response.body[i].commit.message
        let strArr = str.split(' ')
        let idx=str.indexOf('(');
        if(strArr[0].toLowerCase() === 'update' || strArr[0].toLowerCase() === 'add'){
          if(idx !== -1){
            str = str.substr(0, idx)
          }
          this.showStr = str
          this.showLatestConf = true
          break;
        }
      }
    })
  },
}
</script>

<style scoped>
.title{
  font-size: 29px;
  color: #2c3e50;
}
.subtitle{
  padding-top: 15px;
  padding-bottom: 15px;
  color: #666666;
}
</style>
