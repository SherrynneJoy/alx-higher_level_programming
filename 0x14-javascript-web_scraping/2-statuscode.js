#!/usr/bin/node

const axios = require('axios');

function checkStatus (url) {
  axios.get(url)
    .then(response => {
      console.log(`code: ${response.status}`);
    })
    .catch(error => {
      console.error(`code: ${error.message}`);
      process.exit(1); // Terminate the script with an error code
    });
}

if (process.argv.length !== 3) {
  console.error('Usage: node script.js <URL>');
  process.exit(1);
}

const url = process.argv[2];
checkStatus(url);
