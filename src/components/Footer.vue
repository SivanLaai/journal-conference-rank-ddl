
<template>
  <section class="footer">

    <el-row style="padding-top: 8px">
      <div style="float: center; text-align: center; color: #666666;font-size: 12px;">
        <div>
          Powered By <a href="https://github.com/SivanLaai" target="_blank" title="icp" alt="icp">{{ author }}</a>
        </div>
        <div>
          Based on <a href="https://github.com/ccfddl/ccf-deadlines" target="_blank" title="icp" alt="icp">ccfddl</a>
        </div>
        <div style="padding-top: 3px">{{ icp }}</div>
      </div>
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