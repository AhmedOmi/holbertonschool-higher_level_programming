#!/usr/bin/node
const process = require('process');
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) throw error;
  console.log('code:', response.statusCode);
});
