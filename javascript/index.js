const update = () => {
    setTimeout(() => {
        console.log("updated")
    }, 2000)
}

const create = (callback) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log("created");
            let error = false
            if (!error) {
                resolve()
            } else {
                reject()
            }
        }, 2000)
    })
}

// async await
const init = async () => {
    await create()
    update()
}

init()

// 
// create().then(update).catch(() => console.log("error"))

arr1 = [1, 2, 3]

arr2 = JSON.parse(JSON.stringify(arr1))
arr2.push(4)
console.log(arr1, arr2)

