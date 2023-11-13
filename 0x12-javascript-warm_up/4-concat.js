#!/usr/bin/node
const args = process.argv.slice(2);
const firstarg = args[0];
const secondarg = args[1];

if (firstarg === undefined && secondarg === undefined) {
  console.log('undefined ' + 'is ' + 'undefined');
} else if (secondarg === undefined) {
  console.log(firstarg + ' ' + 'is ' + 'undefined');
} else {
  console.log(firstarg + ' ' + 'is ' + secondarg);
}
