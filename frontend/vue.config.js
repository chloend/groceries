const { defineConfig } = require('@vue/cli-service')
const BundleTracker = require('webpack-bundle-tracker')

module.exports = defineConfig({
  transpileDependencies: true,
  publicPath: "/",
  outputDir: './dist/',

  chainWebpack: config => {

    config.optimization
      .splitChunks(false)

    config
      .plugin('BundleTracker')
      .use(BundleTracker, [{ path: "../frontend/", filename: "webpack-stats.json" }])

    config.resolve.alias
      .set('__STATIC__', 'static')
  },

  devServer: {
    host: '0.0.0.0',
    port: 8080,
    hot: true,
    https: false,
    headers: {"Access-Control-Allow-Origin": ["*"]},
    // .watchOptions({poll: 1000}),
    // public: 'http://127.0.0.1:8080'
  }
})
