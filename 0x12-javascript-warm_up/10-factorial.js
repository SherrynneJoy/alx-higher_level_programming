#!/usr/bin/node
const args = process.argv.slice(2);
const num = args[0];

function factorial (num) {
  if (isNaN(num)) {
    return (1);
  }
  num = parseInt(num);
  if (num === 0 || num === 1) {
    return (1);
  } else {
    return (num * factorial(num - 1));
  }
}
const fact = factorial(num);
console.log(fact);
