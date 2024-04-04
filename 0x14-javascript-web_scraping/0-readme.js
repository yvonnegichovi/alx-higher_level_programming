#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];
if (!filePath) {
  console.error('Please provide the file path as an argument.');
  process.exit(1);
}
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
