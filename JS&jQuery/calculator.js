// JavaScript source code
function addition(a, b) {
    return a + b;
}
function subtraction(a, b) {
    return a - b;
}
function multiplication(a, b) {
    return a * b;
}
function division(a, b) {
    if (b == 0) {
        alert("b cannot be 0");
        return;
    } else {
        return a / b;
    }
}

var a_int;
var b_int;
function getInputNum() {
    var a = document.getElementById("num1").value;
    var b = document.getElementById("num2").value;
    a_int = parseInt(a, 10);
    b_int = parseInt(b, 10);
}


var addBtn = document.getElementById("add");
var subtractBtn = document.getElementById("subtract");
var multiplyBtn = document.getElementById("multiply");
var divideBtn = document.getElementById("divide");
var resultNum = document.getElementById("result");

addBtn.onclick = function () {
    getInputNum();
    var res = addition(a_int, b_int);
    resultNum.innerHTML = String(res);
};
subtractBtn.onclick = function () {
    getInputNum();
    var res = subtraction(a_int, b_int);
    resultNum.innerHTML = String(res);
};
multiplyBtn.onclick = function () {
    getInputNum();
    var res = multiplication(a_int, b_int);
    resultNum.innerHTML = String(res);
};
divideBtn.onclick = function () {
    getInputNum();
    var res = division(a_int, b_int);
    resultNum.innerHTML = String(res);
};



