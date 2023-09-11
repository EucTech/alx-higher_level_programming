#!/usr/bin/node

const numberOfAgr = process.argv.length - 2;

if (numberOfAgr === 0) {
  console.log('No argument');
} else if (numberOfAgr === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
