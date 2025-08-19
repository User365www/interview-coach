const path = require("path");
const webpack = require("webpack");
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = {
    entry: "./src/index.js",
    output: {
        path: path.resolve(__dirname, "./static/frontend"), // Пусть сборка для продакшена идет сюда
        filename: "main.js",
        publicPath: '/', // Очень важная строка
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader",
                },
            },
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader'],
            },
        ],
    },
    // --- САМАЯ ВАЖНАЯ НОВАЯ СЕКЦИЯ ---
    devServer: {
        static: {
          directory: path.join(__dirname, 'templates/frontend'), // Указываем, где лежит базовый index.html
        },
        compress: true,
        port: 3000,
        host: '0.0.0.0', // Позволяет подключаться к серверу извне контейнера
        historyApiFallback: true, // Нужно для React Router
    },
    // ------------------------------------
    plugins: [
        new HtmlWebpackPlugin({
            template: './templates/frontend/index.html', // Говорим плагину использовать ваш HTML как шаблон
        }),
        new webpack.DefinePlugin({
            'process.env.NODE_ENV': JSON.stringify(process.env.NODE_ENV || 'development')
        })
    ],
};