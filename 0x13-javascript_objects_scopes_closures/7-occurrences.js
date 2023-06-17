#!/usr/bin/node 

// task 7 Write a function that returns the number of occurrences in a list


exports.nbOccurences = function (list, searchElement) {

  let nOccurrences = 0; //let occurences

  for (let i = 0; i < list.length; i++) {

	   if (searchElement === list[i]) {
      nOccurrences++;
    }
  }
  return nOccurrences;
};
