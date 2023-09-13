#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let n = 0; n < this.height; n++) {
      let row = '';
      for (let k = 0; k < this.width; k++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    const value = this.width;
    this.width = this.height;
    this.height = value;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
