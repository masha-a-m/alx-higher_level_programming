#!/usr/bin/node
//task 10 javascript 

function factorial (n) {
  return n === 0 || isNaN(n) ? 1 : n * factorial(n - 1);}


//function factorial 


console.log(factorial(Number(process.argv[2]))) //nuevo task 
