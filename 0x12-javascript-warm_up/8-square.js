#!/usr/bin/node

const myArg = parseInt(process.argv[2]);
let myX = '';
if (!isNaN(myArg)) {
  for (let i = 0; i < myArg; i++) {
    let myY = 0;
    while (myY < myX) {
      myX += 'X';
      myY++;
    }
    console.log(myX);
  }
} else {
  console.log('Missing size');
}
