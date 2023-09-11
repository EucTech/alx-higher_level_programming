#!/usr/bin/node

let Agrs = process.argv[2];

Agrs = Number(Agrs);

if ((Agrs === undefined) || isNaN(Agrs)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${Agrs}`);
}
