#!/usr/bin/node
function secondBiggest(args) {
  let integers = args.map(Number);
  let sorted = integers.sort((a, b) => b - a);
  if (sorted.length < 2) {
    return 0;
  }
  return sorted[1];
}
let argts = process.argv.slice(2);
console.log(secondBiggest(argts));
