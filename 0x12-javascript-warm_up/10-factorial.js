#!/usr/bin/node

const Agrs = Number(process.argv[2]);
const val = factorial(Agrs);
console.log(val);

function factorial (res) {
  if (isNaN(res) || res <= 1) {
    return 1;
  }
  return (res * factorial(res - 1));
}
