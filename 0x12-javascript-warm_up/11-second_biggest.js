#!/usr/bin/node

const myArg = process.argv.length;
const args = process.argv;
if (myArg <= 3) {
  console.log(0);
} else {
  args.map(Number).slice(2, myArg).sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
