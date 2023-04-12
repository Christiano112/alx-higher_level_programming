#!/usr/bin/node

const myArg = process.argv.length;

if (myArg <= 3) {
  console.log(0);
} else {
  const args = process.argv.map(Number).slice(2, myArg).sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
