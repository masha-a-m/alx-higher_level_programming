#!/usr/bin/node 

// task 3 java script

class Rectangle //class of rectangle 
{
  constructor (w, h)
// constructor w, h
  {
    if ((w > 0) && (h > 0)) //if w> 0, h) 0

    {
      this.width = w;
      this.height = h;

    }
  }

  print () //print ()

  {
    for (let i = 0; i < this.height; i++)  //for let i =0; i < this height


    {
      let s = '';

      for (let j = 0; j < this.width; j++) //for let
      {
        s += 'X';
      }
      console.log(s);
    }
  }

  rotate () {
    const aux = this.width;
    this.width = this.height;
    this.height = aux;
  }

  double () {
    this.width *= 2;

    this.height *= 2;
  }
}

module.exports = Rectangle;
