#!/usr/bin/node
const args = process.argv.slice(2);
const firstarg = args[0];
if (firstarg === undefined) {
  console.log('No argument');
} else {
  console.log(firstarg);
}
