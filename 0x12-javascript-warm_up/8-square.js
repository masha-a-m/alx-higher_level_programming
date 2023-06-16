#!/usr/bin/node

//consta size math floor


const size = Math.floor(Number(process.argv[2])); //process argv.w


if (isNaN(size)) 
{
  console.log('Missing size');
} 
else 

{
  for (let r = 0; r < size; r++);  //for let r+0


  {
    let row = ''; //letr row

    for (let c = 0; c < size; c++) row += 'X'; //rpw +='X';


    console.log(row);
  }
}
