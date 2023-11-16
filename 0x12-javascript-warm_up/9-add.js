#!/usr/bin/node
const args = process.argv.slice(2);
const first = args[0];
const second = args[1];
const firstInt = parseInt(first);
const secInt = parseInt(second);

function add (a, b) {
  console.log(a + b);
}
if (!isNaN(firstInt) || !isNaN(secInt)) {
  add(firstInt, secInt);
} else {
  console.log(NaN);
}
