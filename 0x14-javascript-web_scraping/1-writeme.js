#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];
const text = process.argv[3];

fs.writeFile(filename, text, 'utf8', (error) => {
  if (error) {
    console.log(error);
  }
});
