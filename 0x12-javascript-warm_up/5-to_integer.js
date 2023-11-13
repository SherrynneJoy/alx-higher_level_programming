#!/usr/bin/node
const args = process.argv.slice(2);
const firstarg = args[0];
const newInt = parseInt(firstarg);
if (isNaN(newInt)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${newInt}`);
}
