// hositing example

let a = 10

const init1 = (() => {
    // let a       // happens because js while compiling takes varibles declarations to the top of the scope.
    console.log(a) // undefined 
    let a = 20
    console.log(a) // 20
})()

// clouser example

let b = 10

const init2 = (() => {
    // let b       // js will first take the global value of b, but if its inside the scope, js will take the inside value only.
    console.log(b) // 10
    b = 20
    console.log(b) // 20
})()