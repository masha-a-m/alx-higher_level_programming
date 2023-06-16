#!/usr/bin/node

//task of javascript

const x = Math.floor(Number(process.argv[2])); //const x 

//if isNaN

if (isNaN(x)) {
  console.log('Missing number of occurrences'); //missing number of occurences 
} 
else 
{
  for (let i = 0; i < x; i++) {
    console.log('C is fun'); //c isfun
  }
}
