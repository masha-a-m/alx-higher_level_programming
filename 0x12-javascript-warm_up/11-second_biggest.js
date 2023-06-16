#!/usr/bin/node

if (process.argv.length <= 3) 
processes argc length

{
  console.log(0); //task javascript
} 

  else 
{

  const args = process.argv.map(Number) //const args = process argv map

    .slice(2, process.argv.length)

    .sort((a, b) => a - b);
  //sort 
  console.log(args[args.length - 2]);
}
