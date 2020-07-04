#!/usr/bin/node
const argv = process.argv;
const request = require('request');
let character;
const getChars = {};
request('https://swapi-api.hbtn.io/api/films/' + argv[2], function (error, request) {
  if (error) {
    console.log(error);
    return;
  }
  if (request.statusCode === 200) {
    const response = JSON.parse(request.body);
    for (let i = 0; i < response.characters.length; i++) {
      character = response.characters[i];
      const request = require('request');
      request(character, function (error, request) {
        if (error) {
          console.log(error);
          return;
        }
        if (request.statusCode === 200) {
          const response2 = JSON.parse(request.body);
          getChars[i] = response2.name;
          if (i === response.characters.length - 1) {
            for (const c in getChars) {
              console.log(getChars[c]);
            }
          }
        }
      });
    }
  }
});