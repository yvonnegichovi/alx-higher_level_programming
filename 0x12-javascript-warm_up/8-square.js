#!/usr/bin/node
const arg = process.argv[2];
const num = parseInt(arg);
let i = 0;
if (!isNaN(num) && Number.isInteger(num) && num > 0) {
  for (i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
} else {
  console.log('Missing size');
}
