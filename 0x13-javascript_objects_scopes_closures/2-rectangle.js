#!/usr/bin/node

// task 2 rectangle that defines a rectangle


class Rectangle 
 //task 2
{
  constructor (w, h) //w, h

  {
    if ((w > 0) && (h > 0)) //if w> 0 && h < 0
    {
      this.width = w; //widtth w
      this.height = h; // height h
    
    }
  }
}



module.exports = Rectangle; //module export rectangle 
