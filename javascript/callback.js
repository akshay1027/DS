const update = () => {
    setTimeout(() => {
        console.log("updated")
    }, 2000)
}

const create = (callback) => {
    setTimeout(() => {
        console.log("created")
        callback()
    }, 1000)
}


create(update)
