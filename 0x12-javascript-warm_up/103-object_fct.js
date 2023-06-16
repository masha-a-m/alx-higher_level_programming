#!/usr/bin/node

// task 103

const myObject = 

{
  type: 'object', //type pbject
  value: 12 //value 12
};

console.log(myObject);  

myObject.incr = function () 
{
  this.value++;
};

myObject.incr();
console.log(myObject);

myObject.incr(); //myobject incr
console.log(myObject); //console log

myObject.incr(); //myobject

console.log(myObject);//console log
