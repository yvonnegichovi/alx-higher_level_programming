#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const content = process.argv[3];

if (!filePath || !content) {
  console.error('Please provide both the file path and the content.');
  process.exit(1);
}
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log(content);
  }
});
