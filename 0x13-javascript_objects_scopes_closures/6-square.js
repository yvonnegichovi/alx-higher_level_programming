#!/usr/bin/node

const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  constructor (size) {
    super(size);
  }

  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
}

module.exports = Square;
