module.exports = {
    // chainWebpack: config => {
    //     const svgRule = config.module.rule('svg')
    //     svgRule.uses.clear()
    //     svgRule
    //       .use('vue-svg-loader')
    //       .loader('vue-svg-loader')
    //   },
    chainWebpack: (config) => {
        // svg rule loader
        const svgRule = config.module.rule('svg') // 找到 svg-loader
        svgRule.uses.clear() // 清除已有 loader
        svgRule.exclude.add(/node_modules/) // 排除 node_modules 目录
        svgRule // 添加新的 svg loader
          .test(/\.svg$/)
          .use('svg-sprite-loader')
          .loader('svg-sprite-loader')
          .options({
            symbolId: 'icon-[name]',
          })
      },
    pages: {
        index: {
            entry: 'src/main.js',
            template: 'public/index.html',
            filename: 'index.html',
            title: '研究领域的相关会议和期刊',
        }
    },
    // assetsDir: 'eda',
}