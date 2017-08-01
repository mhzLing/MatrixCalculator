function toMatrix(input)
{
  var rowCounter=0;
  var colCounter=0;

}

function add()
{
  var x = document.forms["matrixForm"]["matrix"].value;

  document.getElementById("ansMatrix").innerHTML = x;
}

function det()
{
  var x = document.forms["matrixForm"]["matrix"].value;
  document.getElementById("ansMatrix").innerHTML = x;
}

function mult()
{
  var x = parseInt(document.forms["matrixForm"]["matrix1"].value);
  var y = parseInt(document.forms["matrixForm"]["matrix2"].value);
  var z = x + y;
  document.getElementById("ansMatrix").innerHTML = z;
}
