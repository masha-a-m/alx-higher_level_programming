#!/usr/bin/node

// task java script

exports.esrever = function (list) {
  let len = list.length - 1; // reversed version of a list:

  let i = 0; //8-main.js


  while ((len - i) > 0) {
    const aux = list[len]; //const aux list

    list[len] = list[i]; //list len 

    list 
    list[i] = aux; //aux

    i++; //incre

    len--;
  }
  return list;
};
