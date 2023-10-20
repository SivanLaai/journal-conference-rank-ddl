
<template>
  <section class="footer">
    <el-row class="icp">
      Powered By <a href="https://github.com/SivanLaai" target="_blank" title="icp" alt="icp">{{ author }}</a>
    </el-row>
    <el-row class="icp">
      Based on <a href="https://github.com/ccfddl/ccf-deadlines" target="_blank" title="icp" alt="icp">ccfddl</a>
    </el-row>
    <el-row class="icp">
      <a target="_blank" title="icp" alt="icp">{{ icp }}</a>
    </el-row>
  </section>
</template>

<script>
export default {
  name: 'Footer',
  data() {
    return {
      author: 'SivanLaai',
      icp: '京ICP备2023014024号-1',
      gov: ''
    }
  },
  mounted() {
  },
}
</script>

<style scoped>
.icp{
  font-size: 16px;
  color: #2c3e50;
  text-align: center;
}
.footer {
    height: auto;
    width: 100%;
    text-align: center;
    line-height: 1.25rem;
    padding: 1rem 0;
}
</style>