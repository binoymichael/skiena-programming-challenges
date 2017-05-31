var cache = {};

function cycle_length(n) {
  if (n in cache) return cache[n];
  if (n === 1) return 1;

  var next = (n % 2 === 0) ? (n / 2) : (3 * n + 1);

  var ans = 1 + cycle_length(next);
  cache[n] = ans;

  return ans;
}

var input = [];
for (var i = 900; i <= 1000; i++) { input.push(i); }
var result = Math.max(...input.map(cycle_length));

console.log(result);
