#!/usr/bin/node

const myArg = parseInt(process.argv[2]);
let myX = '';
if (!isNaN(myArg)) {
  for (let i = 0; i < myArg; i++) {
    myX += 'X';
    console.log(myX);
  }
} else {
  console.log('Missing size');
}
