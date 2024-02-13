#!/usr/bin/node
function secondBiggest (args) {
  const integers = args.map(Number);
  const sorted = integers.sort((a, b) => b - a);
  if (sorted.length < 2) {
    return 0;
  }
  return sorted[1];
}
const argts = process.argv.slice(2);
console.log(secondBiggest(argts));
