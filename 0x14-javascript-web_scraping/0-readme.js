#!/usr/bin/node

const fs = require('fs');
const arg = process.argv[2];

fs.readFile(arg, 'utf8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
