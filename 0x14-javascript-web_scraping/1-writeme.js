#!/usr/bin/node

const fs = require('fs');

const writeFile = (fp, info) => {
  try {
    fs.writeFileSync(fp, info, 'utf-8');
    console.log(`info was written successfully into: ${fp}`);
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
};

if (process.argv.length !== 4) {
  console.log('Usage: node write_file.js <file_path> <info_to_write>');
} else {
  const fp = process.argv[2];
  const infoToWrite = process.argv[3];
  writeFile(fp, infoToWrite);
}
