x = [ [1, 2], [3, 4] ]
y = [ [5, 6], [7, 8] ]
z = [ [9, 10, 11], [12, 13, 14] ]

def is_matrix(matrix):
    if type(matrix) is not list:
        return False
    
    len1 = len(matrix[0])
    for i in matrix:
        if len1 != len(i):
            return False
    return True
    

def same_size(m1, m2):
    assert is_matrix(m1) and is_matrix(m2)
    assert len(m1) == len(m2)
    
    for i in m1:
        for j in m2:
            if len(i) != len(j):
                return False
    return True

    
def add(m1, m2):
    try:
        assert same_size(m1, m2)
        m = []

        for row in range(len(m1)):
            m.append([])
            for col in range(len(m1[0])):
                m[row].append(m1[row][col] + m2[row][col])
        return m
    
    except AssertionError:
        print("unequal size")


def mul_by_num(m, num):
    try:
        assert is_matrix(m)
        assert type(num) in (int, float)
        new_m = []

        for row in range(len(m)):
            new_m.append(list(m[row]))
            for col in range(len(m[0])):
                new_m[row][col] *= num
        return new_m
                
    except AssertionError:
        print("not a matrix") if not is_matrix(m) else print("num must be int or float")
    

assert is_matrix(x)
assert is_matrix(y)
assert is_matrix(z)
assert same_size(x, y)
assert same_size(x, z) == False
assert add(x, y)
print(mul_by_num(x, 2))
print(mul_by_num(y, 4))

