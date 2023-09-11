#!/usr/bin/node

const firstArg = Number(process.argv[2]);
const secArg = Number(process.argv[3]);

add(firstArg, secArg);

function add (a, b) {
	console.log(a + b);
}
