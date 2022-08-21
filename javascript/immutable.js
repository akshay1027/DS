arr1 = [1, 2, 3]

arr2 = arr1
arr2.push(4)
console.log(arr1, arr2)

// op: [ 1, 2, 3, 4 ] [ 1, 2, 3, 4 ]

arr3 = JSON.parse(JSON.stringify(arr1))
arr2.push(4)
console.log(arr1, arr2)

// op: [ 1, 2, 3 ] [ 1, 2, 3, 4 ]