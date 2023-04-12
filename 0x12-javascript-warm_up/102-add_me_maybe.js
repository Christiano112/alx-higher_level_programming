#!/usr/bin/node
exports.addMeMaybe = function (number, myFunc) {
  myFunc(++number);
};
