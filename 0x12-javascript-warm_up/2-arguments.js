#!/usr/bin/node

//task for java script


const count = process.argv.length;

console.log(count === 2 ? 'No argument' : count === 3 ? 'Argument found': 'Arguments found');
