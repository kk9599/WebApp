var ExtractTextPlugin = require('extract-text-webpack-plugin')
var webpack = require("webpack");
module.exports = {
    // This is the "main" file which should include all other modules
    entry: './client/main.js',
    // Where should the compiled file go?
    output: {
        library: '',
        // To the `dist` folder

        path: './static/js',
        // With the filename `build.js` so it's dist/build.js
        filename: 'build.js'
    },
    module: {
        loaders: [
            {
                test: /\.js$/,
                loader: 'babel',
                exclude: /node_modules/
            },
            {
                test: /\.vue$/,
                loader: 'vue'
            },

            {
                test: /\.css$/,
                loader: ExtractTextPlugin.extract("style-loader", "css-loader")
            },
            {
                test: /\.sass$/,
                loader: ExtractTextPlugin.extract('css!sass')
            },
            {
                test: /\.(woff|woff2|eot|ttf|svg)?(\?v=[0-9]\.[0-9]\.[0-9])?$/,
                loader: "url-loader?limit=10000&minetype=application/font-woff&name=../css/[hash].[ext]"
            },
            {
                test: /\.(jpg|jpeg|gif|png)$/,
                exclude: /node_modules/,
                loader: 'url-loader?limit=1024&name=../img/[name].[ext]'

            },
        ]
    },
    vue: {
        loaders: {
            js: 'babel',
            css: ExtractTextPlugin.extract("css"),
            less: ExtractTextPlugin.extract("css!less"),
            sass: ExtractTextPlugin.extract("css!sass")
        }
    }
    ,

    plugins: [
        new ExtractTextPlugin("../css/style.css"),
        new webpack.ProvidePlugin({
            jQuery: 'jquery',
            $: 'jquery',
            "window.jQuery": "jquery"
        })
    ]

}
