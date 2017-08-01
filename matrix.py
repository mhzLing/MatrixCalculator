

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


def smaller_row_vec(v1, v2):
    for index in range(len(v1)):
        if v1[index] != v2[index]:
            return v1 if min(v1[index], v2[index]) == v1[index] else v2
    return ""    


##def reduce(m):
##    ''' returns (reduced matrix, operations performed) or (list, [str])'''
##    assert is_matrix(m)
##    new_m = copy_matrix(m)
##    operations = []
##    current_col = 0
##    
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
assert smaller_row_vec(v1, v2) == v1
##assert add(x, y)
##print(mul_by_num(x, 2))
##print(mul_by_num(y, 4))
##add(v1, v2)
