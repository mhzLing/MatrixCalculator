from fractions import gcd

def is_matrix(m):
    ''' return true if m is matrix or vector '''
    if not (type(m) is list and type(m[0]) in (list, int, float)):
        return False

    for i in m:
        if type(m[0]) != type(i):
            return False
        
    if type(m[0]) is list:
        len1 = len(m[0])
        for i in m:
            if len1 != len(i):
                return False
    return True
    

def same_size(m1, m2):
    if not (is_matrix(m1) and is_matrix(m2) and len(m1) == len(m2)):
        return False
    if type(m1[0]) != type(m2[0]):
        return False

    if type(m1[0]) is list:
        for i in m1:
            for j in m2:
                if len(i) != len(j):
                    return False
    return True


def size(m):
    if not is_matrix(m):
        return ""

    result = f"{len(m)} x "
    result += "1" if type(m[0]) in (int, float) else f"{len(m[0])}"
    return result


def copy_matrix(m):
    ''' returns a copy of the matrix with different id '''
    return [ list(row) for row in m ]


def smaller_row_vector(v1, v2):
    for index in range(len(v1)):
        if v1[index] != v2[index]:
            return v1 if min(v1[index], v2[index]) == v1[index] else v2
    return ""


############################################
###############  OPERATIONS  ###############
############################################


def _reduce_vector_gcd(v):
    ''' returns (reduced vector, gcd) '''
    min_num = gcd(v[0], v[1])
    result = []

    for i in range(len(v) - 1):
        divisor = gcd(v[i], v[i + 1])
        if divisor < min_num:
            min_num = divisor // 2 if divisor % 2 == 0 and divisor != 2 else divisor

    for i in v:
        if i // min_num < i / min_num:
            return (v, 1)
        else:
            result.append(i // min_num)
    return (result, min_num)


def reduce_vector(v):
    ''' returns (correctly reduced vector, least common divisor) '''
    result = _reduce_vector_gcd(v)[0]
    next_result = _reduce_vector_gcd(result)
    
    if next_result[1] == 1:
        return result
    else:
        return reduce_vector(result)


def compare_vectors(m):
    ''' changes repeated row vector to 0's, order unchanged.
        returns (changed matrix, operations) '''
    result = copy_matrix(m)
    operations = []
    counter = 0

    while counter != len(result) - 1:
        for row in range(len(result)):
            if id(result[counter]) != id(result[row]) and result[counter] == result[row]:
                result[row] = [ 0 for i in m[row] ]
        counter += 1
    return (result, operations)
    
    

def reduce_matrix(m):      #INCOMPLETE
    ''' returns (reduced matrix, operations performed) or (list, [str])'''
    assert is_matrix(m)
    new_m = []
    operations = []
    current_col = 0

    for v in m:
        new_v = reduce_vector(v)
        new_m.append(new_v)
        operations.append(f"*{v[0] // new_v[0]}") ########?
        print(operations)
        
    temp = compare_vectors(new_m)
    new_m = temp[0]
    operations.append(temp[1])
##    while current_col < len(m[0]):
##        change_rows = []
##        row_with_pivot = new_m[0]
##        
##        for row in range(len(m)):
##            if new_m[row][current_col] != 0:
##                change_rows.append(row)
##                
##                
##        if len(change) != 0:
##            pass


def echelon_form(m):
    pass


def rref(m):
    ''' reduced row echelon form '''
    pass

    
def add(m1, m2):
    try:
        assert same_size(m1, m2)
        result = []

        for row in range(len(m1)):
            result.append([])
            
            for col in range(len(m1[0])):
                result[row].append(m1[row][col] + m2[row][col])
        return result
    
    except AssertionError:
        print("unequal size")


def mul_by_num(m, num):
    try:
        assert is_matrix(m)
        assert type(num) in (int, float)
        result = []

        for row in range(len(m)):
            result.append(list(m[row]))
            for col in range(len(m[0])):
                result[row][col] *= num
        return result
                
    except AssertionError:
        print("not a matrix") if not is_matrix(m) else print("num must be int or float")
    

x = [ [1, 2], [3, 4] ]
y = [ [5, 6], [7, 8] ]
z = [ [9, 10, 11], [12, 13, 14] ]
v1 = [1, -2]
v2 = [2, -5]
nope = [ [1, 2], 3, 4 ]

assert is_matrix(x)
assert is_matrix(v1)
assert is_matrix(nope) == False
assert same_size(x, y)
assert same_size(x, z) == False
assert same_size(x, nope) == False
assert same_size(v1, v2)
assert size(x) == "2 x 2"
assert size(v1) == "2 x 1"
assert size(nope) == ""
assert smaller_row_vector(v1, v2) == v1
assert reduce_vector([1, 2, 3, 4]) == [1, 2, 3, 4]
assert reduce_vector([2, 4, 6]) == [1, 2, 3]
##assert add(x, y)
##print(mul_by_num(x, 2))
##print(mul_by_num(y, 4))
##add(v1, v2)
