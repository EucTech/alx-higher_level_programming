#!/usr/bin/node
addMeMaybe function (number, theFunction) {
  number += 1;
  theFunction(number);
};

module.exports = addMeMaybe;
