#!/usr/bin/node

const SquareP = require('./5-square'); //const SquareP =require .5 square

class Square extends SquareP //class Square extends SquareP
{
  charPrint (c) //charPrint (c)
  
  {
    if (c === undefined) //if c==undefined 
    {
      c = 'X'; //c =X
    }
    for (let i = 0; i < this.height; i++) //for let i = 0
    {
      let s = ''; //let s= '';
      for (let j = 0; j < this.width; j++) //
      {
        s += c;
      }
      console.log(s);
    }
  }
}

module.exports = Square;
