const prompt = require('prompt-sync')();

let stack = [1, 2, 3];

console.log('length', stack.length)

push = (data) => {
    stack.push(data);
}

pop = () => {
    stack.pop();
}

const operation = prompt('choose operation 1->push | 2->pop | 3->quit');
console.log(operation == 1);

if (operation == 1) {
    const data = prompt('enter element to be pushed');
    push(data);
    prompt(`stack is ${stack}`)
} else if (operation == 2) {
    pop();
    prompt(`stack is ${stack}`)
}