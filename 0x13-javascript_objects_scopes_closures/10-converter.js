#!/usr/bin/node

exports.converter = function (base) {
  return function convertToBaseN (number) {
    if (number < base) {
      return number.toString();
    } else {
      return convertToBaseN(Math.floor(number / base)) + (number % base).toString();
    }
  };
};
