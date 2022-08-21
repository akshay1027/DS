// Coersion example

x = 10
y = "10"

console.log(x == y) // due to type coersion, y is converted to Number
// true

console.log(x + y) // due to type coersion, x is converted into String
// 1010

// solution:

console.log(Number(x) + Number(y))
