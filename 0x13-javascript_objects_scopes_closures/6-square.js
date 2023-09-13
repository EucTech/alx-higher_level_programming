#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let n = 1; n <= this.height; n++) {
        let row = '';
        for (let k = 1; k <= this.width; k++) {
          row += c;
        }
        console.log(row);
      }
    }
  }
}

module.exports = Square;
