#!/usr/bin/node
const args = process.argv.slice(2);
const size = args[0];
const newInt = parseInt(size);

if (isNaN(newInt)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < newInt; i++) {
    let mysq = '';
    for (let j = 0; j < newInt; j++) {
      mysq += 'X';
    }
    console.log(mysq);
  }
}
