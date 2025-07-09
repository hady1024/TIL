const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

let i = 0;
while (i < input.length) {
  const [a, b] = input[i].split(' ').map(Number);
  if (a === 0 && b === 0) break;
  console.log(a + b);
  i++;
}