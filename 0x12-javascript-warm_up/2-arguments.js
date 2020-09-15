#!/usr/bin/node
const found = process.argv.length;
if (found === 2) {
  console.log('No argument');
} else if (found === 3) {
  console.log('Argument found');
} else if (found > 3) {
  console.log('Arguments found');
}
