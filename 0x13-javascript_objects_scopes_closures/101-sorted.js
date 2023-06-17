#!/usr/bin/node


const dict = require('./101-data').dict; //task java script



const totalist = Object.entries(dict); // bject entries dict


const vals = Object.values(dict); //Object Values


const valsUniq = [...new Set(vals)]; //const vals Uniq 


const newDict = {}; //const newDict

for (const j in valsUniq) {
 
	 const list = [];
  for (const k in totalist) {
    if (totalist[k][1] === valsUniq[j]) {

      list.unshift(totalist[k][0]); //list.unshift
    }
  }

  newDict[valsUniq[j]] = list; //newDict valsUniq

}



console.log(newDict); //console log new Dict
