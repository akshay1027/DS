// var -> Functional scope
// let -> Block scope { .. }

function bro (){
    {
        var z1 = 10 // functional scope
        let z2 = 20  // block scope
    }
    console.log(z1, z2) // 10, undefined
}
bro()