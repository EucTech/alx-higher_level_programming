#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let cal = 0;
  let i = 0;
  while (i < list.length) {
    if (list[i] === searchElement) {
      cal++;
    }
    i++;
  }
  return cal;
};
