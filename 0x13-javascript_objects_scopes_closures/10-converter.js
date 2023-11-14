#!/usr/bin/node
exports.converter = function (base) {
  return function convertToBase (number) {
    if (number === 0) {
      return 0;
    }
    const remainder = number % base;
    const answer = Math.floor(number / base);
    const result = convertToBase(answer) + (remainder < 10 ? remainder : String.fromCharCode(87 + remainder));
    return result;
  };
};
