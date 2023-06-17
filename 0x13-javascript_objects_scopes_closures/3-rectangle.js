#!/usr/bin/node

// task 3

class Rectangle  //java script

{
  constructor (w, h) //constructor w, h
  {
    if ((w > 0) && (h > 0)) //class notation for defining your class

    {
      this.width = w; // constructor must take 2 arguments: w and h
      this.height = h; // instance attribute height with the value of h

    }
  }

  print () 

  {
    for (let i = 0; i < this.height; i++)  //If w or h is equal to 0 or not a positive integer, create an empty object

    {
      
    let s = ''; //let s = '';

      for (let j = 0; j < this.width; j++) //fir let j = 0;

      {
        s += 'X'; //s+= 'X'
     
      }

      console.log(s); //console.log(s);

    }
  }
}

module.exports = Rectangle;
