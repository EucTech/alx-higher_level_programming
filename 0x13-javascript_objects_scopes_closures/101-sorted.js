#!/usr/bin/node

const dict = require('./101-data').dict;

const sortObj = {};

for (const key in dict) {
  const value = dict[key];
  if (sortObj[value]) {
    sortObj[value].push(key);
  } else {
    sortObj[value] = [key];
  }
}

console.log(sortObj);
