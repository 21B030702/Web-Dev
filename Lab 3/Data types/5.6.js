function Calculator() {
    this.calculate = function(str) {
        const arr = str.split(" ");
        let a = +arr[0], sign = arr[1], b = +arr[2];
        return this.methods[sign](a, b);
    };
    this.addMethod = function(sign, func) {
        this.methods[sign] = func;
    };
    this.methods = {
      "-": (a, b) => a - b,
      "+": (a, b) => a + b
    };
}

let calc = new Calculator;

alert( calc.calculate("3 + 7") ); // 10

let powerCalc = new Calculator;
powerCalc.addMethod("*", (a, b) => a * b);
powerCalc.addMethod("/", (a, b) => a / b);
powerCalc.addMethod("**", (a, b) => a ** b);

let result = powerCalc.calculate("2 ** 3");
alert( result ); // 8
