exports.modifyWebpackConfig = ({ config, stage }) => {
  if (stage === "build-html") {
    config.loader("null", {
      test: /web3/,
      loader: "null-loader",
    });
  }
};
