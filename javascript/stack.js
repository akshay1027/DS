// const prompt = require('prompt-sync')();
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

function getInput(question) {
    let data;
    readline.question(question, element => {
        // console.log(`Hey there ${name}!`);
        data = element;
        readline.close();
    });
    return data;
}

let stack = [];

push = () => {

}

let choice = getInput('choose operation 1->push | 2->pop | 3->quit')
console.log(choice)