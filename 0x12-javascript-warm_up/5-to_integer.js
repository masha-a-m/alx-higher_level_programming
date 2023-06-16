#!/usr/bin/node

//java sdcript file

const num = Math.floor(Number(process.argv[2])); //math floor

console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`); //my number. not a number
