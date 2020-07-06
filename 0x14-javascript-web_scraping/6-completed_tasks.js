#!/usr/bin/node
const process = require('process');
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) { throw error; }
  const jsn = JSON.parse(body);
  let ze = 0;
  let usr = 1;
  let number = 0;
  for (let i = 0; jsn[i]; i++) number = jsn[i].userId;
  for (let z = 0; z < number; z++) {
    ze = 0;
    for (let i = 0; jsn[i]; i++) { if (jsn[i].userId === usr && jsn[i].completed === true) ze++; }
    if (usr === 1) { console.log(`{ '${usr}': ${ze},`); } else if (usr === 10) { console.log(`  '${usr}': ${ze} }`); } else { console.log(`  '${usr}': ${ze},`); } usr++;
  }
});
