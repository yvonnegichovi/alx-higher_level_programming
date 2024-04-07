#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const [, , url, filePath] = process.argv;

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to get data. Status code:', response.statusCode);
    return;
  }

  fs.writeFile(filePath, body, { encoding: 'utf-8' }, err => {
    if (err) {
      console.error('Error writing to file:', err);
      return;
    }
  });
});
