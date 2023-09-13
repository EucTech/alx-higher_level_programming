#!/usr/bin/node

exports.esrever = function (list) {
  const reverseList = [];
  for (let n = list.length - 1; n >= 0; n--) {
    reverseList.push(list[n]);
  }
  return reverseList;
};
