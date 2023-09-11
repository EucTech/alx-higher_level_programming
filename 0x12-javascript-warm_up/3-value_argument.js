#!/usr/bin/node

const agrNum = process.argv;

if (agrNum[2] === undefined) {
  console.log('No argument');
} else {
  console.log(agrNum[2]);
}
