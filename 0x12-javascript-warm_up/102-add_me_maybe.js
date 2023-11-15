#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  const newNo = number + 1;
  theFunction(newNo);
};
