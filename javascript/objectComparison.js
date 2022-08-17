obj1 = {
    a: "mamey",
    b: 1
}

obj2 = {
    a: "mamey",
    b: 1
}

console.log(obj1 == obj2, obj1 === obj2) // false, false
console.log(JSON.stringify(obj1) === JSON.stringify(obj1)) // true