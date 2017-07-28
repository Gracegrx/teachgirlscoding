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
    var a = $('#num1').val();
    var b = $('#num1').val();
    a_int = parseInt(a, 10);
    b_int = parseInt(b, 10);
}

$('#add').click(function () {
    getInputNum();
    var res = addition(a_int, b_int);
    $('#result').html(String(res));
});
$('#subtract').click(function () {
    getInputNum();
    var res = subtraction(a_int, b_int);
    $('#result').html(String(res));
});
$('#multiply').click(function () {
    getInputNum();
    var res = multiplication(a_int, b_int);
    $('#result').html(String(res));
});
$('#divide').click(function () {
    getInputNum();
    var res = division(a_int, b_int);
    $('#result').html(String(res));
});


