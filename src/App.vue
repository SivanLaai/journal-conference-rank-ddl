<template>
  <div id="app">
    <Header></Header>
    <el-switch style="display: block; margin-bottom: 15px;" v-model="select" active-color="#13ce66"
      inactive-color="purple" active-text="学术期刊" inactive-text="学术会议">
    </el-switch>
    <div v-if="select === false">
      <Conference></Conference>
    </div>
    <div v-else>
      <Journal></Journal>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
import Header from '@/components/Header'
import Footer from '@/components/Footer'
import Conference from "@/components/Conference";
import Journal from "@/components/Journal";

export default {
  name: 'App',
  components: {
    Conference,
    Journal,
    Header,
    Footer,
  },
  data() {
    return {
      activeName: 'first',
      select: false
    };
  },
  methods: {
    handleClick(tab, event) {
      console.log(tab, event);
    }
  }
}
</script>

<style>
#app {
  font-family: "Roboto", "Helvetica Neue", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  max-width: 980px;
  margin-left: auto;
  margin-right: auto;
}
</style>
