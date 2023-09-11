#!/usr/bin/node
let Agrs = process.argv[2];
Agrs = Number(Agrs);

if (isNaN(Agrs)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Agrs; i++) {
    let row = '';
    for (let k = 0; k < Agrs; k++) {
      row += 'X';
    }
    console.log(row);
  }
}
