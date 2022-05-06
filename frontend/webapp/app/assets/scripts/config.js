'use strict';
import defaultsDeep from 'lodash.defaultsdeep';

var configurations = require(
  './config/*.js', { mode: 'hash' }
);

// defaults.js
var config = configurations.defaults || {};

if (process.env.DS_ENV === 'staging') {
  // staging.js
  config = defaultsDeep(configurations.staging, config);
} else if (process.env.DS_ENV === 'production') {
  // production.js
  config = defaultsDeep(configurations.production, config);
}
module.exports = config.default;
