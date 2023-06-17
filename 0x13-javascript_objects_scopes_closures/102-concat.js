#!/usr/bin/node


const fs = require('fs'); // task 102 java script


const fArg = fs.readFileSync(process.argv[2]).toString(); //const fArg =fa read


const sArg = fs.readFileSync(process.argv[3]).toString(); //to String procss argv


fs.writeFileSync(process.argv[4], fArg + sArg); //write file sync

//
