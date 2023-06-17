#!/usr/bin/node

//task 100 java script

const list = require('./100-data').list; //const list = require list


const newList = list.map(function (num, index) {
  return num * index;

});


console.log(list); //console log list


console.log(newList);
