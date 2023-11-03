// var x = 10;
// console.log(x);
// if (true) {
//     let x = 20;
//     console.log(x);
// }
// console.log(x);

function foo() {
   var a = b = c = 5;
}
foo();
console.log(`The value of c is ${c}`); // 5
console.log(`The value of b is ${b}`); // 5
console.log(`The value of a is ${a}`)  // error