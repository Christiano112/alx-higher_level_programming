#!/usr/bin/node

function add(a, b) {
  return console.log(a + b);
}
add (process.argv[2], process.argv[3]);
