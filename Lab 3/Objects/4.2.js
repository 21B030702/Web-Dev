let calculator = {
    a : 0,
    b : 0,
    read(){this.a = +prompt("Value1"); this.b = +prompt("Value2");},
    sum(){return this.a + this.b},
    mul(){return this.a * this.b}
  };
  
  calculator.read();
  alert( calculator.sum() );
  alert( calculator.mul() );