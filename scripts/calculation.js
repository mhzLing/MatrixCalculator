var TYPES = {
    'undefined'        : 'undefined',
    'number'           : 'number',
    'boolean'          : 'boolean',
    'string'           : 'string',
    '[object Function]': 'function',
    '[object Array]'   : 'array'
}

TOSTRING = Object.prototype.toString;


function type(o)
{
    return TYPES[typeof o] || TYPES[TOSTRING.call(o)] || (o ? 'object' : 'null');
};


function isMatrix(m)
{
  if( !(type(m) == 'array' && (type(m[0]) == 'array' || type(m[0]) == 'number')) ){
    return false;
  }

  for(i in m){
    if(type(m[0]) !== type(m[i])){
      return false;
    }
  }

  if(type(m[0]) == 'array'){
    var len = m[0].length;
    for(i in m){
      if(len != m[i].length){
        return false;
      }
    }
  }
  return true;
}


function sameSize(m1, m2)
{
  if( !(isMatrix(m1) && isMatrix(m2) && m1.length == m2.length && type(m1[0]) == type(m2[0])) ){
    return false;
  }

  if(type(m1[0]) == 'array'){
    for(i in m1){
      for(j in m2){
        if(m1[i].length != m2[j].length){
          return false;
        }
      }
    }
  }
  return true;
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
