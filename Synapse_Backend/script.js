const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Enter starting number: ", (startInput) => {

    rl.question("Enter ending number: ", (endInput) => {

        let start = Number(startInput);
        let end = Number(endInput);

        let result = {};

        for (let num = start; num < end; num++) {

            let str = num.toString();
            let reversed = str.split('').reverse().join('');

            if (str === reversed) {
                result[num] = num.toString(2);
            } else {
                result[num] = Number(reversed);
            }
        }

        console.log(result);

        rl.close();
    });
});