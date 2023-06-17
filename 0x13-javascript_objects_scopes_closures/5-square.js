#!/usr/bin/node

//Square that defines a square and inherits from Rectangle

const Rectangle = require('./4-rectangle'); //class notation for defining your class and extends
class Square extends Rectangle //class extends rectangle {
  constructor (size){
    super(size, size); //super size, size
  }
}

module.exports = Square; //module.exports
