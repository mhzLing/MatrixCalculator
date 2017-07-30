function add()
{
  var x = parseInt(document.forms["matrixForm"]["matrix1"].value);
  document.getElementById("answerAdd").innerHTML = x;
}

function det()
{
  var x = parseInt(document.forms["matrixForm"]["matrix1"].value);
  document.getElementById("answerDet").innerHTML = x;
}

function mult()
{
  var x = parseInt(document.forms["matrixForm"]["matrix1"].value);
  var y = parseInt(document.forms["matrixForm"]["matrix2"].value);
  var z = x + y;
  document.getElementById("answerMult").innerHTML = z;
}
