arr1 = [1, 2, 3]

arr2 = arr1
arr2.push(4)
console.log(arr1, arr2)

// op: [ 1, 2, 3, 4 ] [ 1, 2, 3, 4 ]

arr3 = JSON.parse(JSON.stringify(arr1))
arr2.push(4)
console.log(arr1, arr2)

// op: [ 1, 2, 3 ] [ 1, 2, 3, 4 ]

const s1 = ['⭐', '⭐', '⭐'];
const s2 = ['⭐', '⭐', '⭐'];

const s3 = s1;
const s4 = [...s2];

s3.push(4)
s4.push(4)

console.log(s1, s2)
// op: ['⭐', '⭐', '⭐', 4] ['⭐', '⭐', '⭐']
