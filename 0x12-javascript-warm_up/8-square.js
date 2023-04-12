#!/usr/bin/node

const myArg = process.argv[2];

if (parseInt(myArg)) {
  for (let i = 0; i < myArg; i++) {
    let myY = 0;
    let myX = '';

    while (myY < myArg) {
      myX += 'X';
      myY++;
    }
    console.log(myX);
  }
} else {
  console.log('Missing size');
}
