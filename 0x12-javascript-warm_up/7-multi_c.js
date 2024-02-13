#!/usr/bin/node
const arg = process.argv[2];
const num = parseInt(arg);
let i = 0;
if (!isNaN(num) && Number.isInteger(num)) {
  for (i = 0; i < num; i++) {
	 console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrence');
}
