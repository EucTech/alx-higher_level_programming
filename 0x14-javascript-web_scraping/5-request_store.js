#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const file = process.argv[3];

request.get(url, (error, response, content) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(file, content, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
