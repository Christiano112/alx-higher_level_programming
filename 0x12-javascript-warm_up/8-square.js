#!/usr/bin/node

const myArg = parseInt(process.argv[2]);

if (myArg) {
  for (let i = 0; i < myArg; i++) {
    let myY = 0;
    let myX = '';

    while (myY < myX) {
      myX = myX + 'X';
      myY++;
    }
    console.log(myX);
  }
} else {
  console.log('Missing size');
}
