var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    context: __dirname,

    entry: './hptrivia_app/static/hptrivia_app/js/index', // entry point of our app. assets/js/index.jsx should require other js modules and dependencies it needs

    output: {
        path: path.resolve('./hptrivia_app/static/hptrivia_app/bundles/'),
        filename: "[name]-[hash].js"
    },

    plugins: [
        new BundleTracker({filename: './webpack-stats.json'})
    ],

    module: {
        loaders: [
            {
                // to transform JSX into JS
                test: /\.jsx?$/,
                exclude: /node_modules/,
                loader: 'babel-loader',
                query: {
                    presets: ['react']
                }
            },
            {
                // loads CSS and injects it into the DOM via a <link> tag
                test: /\.css$/,
                loader: 'style-loader'
            },
            {
                // parses a CSS file and apply various transforms to it
                test: /\.css$/,
                loader: 'css-loader',
                query: {
                    modules: true,
                    localIdentName: '[name]__[local]___[hash:base64:5]'
                }
            }
        ],
    },
    resolve: {
        modules: ['node_modules', 'bower_components'],
        extensions: ['.js', '.jsx']
    }
};