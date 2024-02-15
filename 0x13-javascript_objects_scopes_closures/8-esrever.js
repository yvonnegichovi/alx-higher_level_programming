#!/usr/bin/node

exports.esrever = function (list) {
  const length = list.length;
  for (let i = 0; i < Math.floor(length / 2); i++) {
    const temp = list[i];
    list[i] = list[length - 1 - i];
    list[length - 1 - i] = temp;
  }
  return list;
};
