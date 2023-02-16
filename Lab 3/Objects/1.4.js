// before the call
let menu = {
    width: 200,
    height: 300,
    title: "My menu"
};

  function multiplyNumeric(menu){
    for (let x in menu){
        if (typeof menu[x] == "number"){
            menu[x] *= 2;
        }
    }
  };
  
  multiplyNumeric(menu);

  for (let x in menu){
    alert(menu[x]);
  }