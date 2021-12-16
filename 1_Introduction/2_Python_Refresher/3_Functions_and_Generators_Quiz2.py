correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
# Define a function check_sudoku() here:
def array(num):
    return [i for i in range(1, num+1)]

def check_sudoku(square_list):
    inx = 0
    # each row
    for i in range(1, len(square_list)+1):
        doub = []

        # each item in the row
        for i in range(len(square_list)):
            if not square_list[inx][i] in array(len(square_list)) or square_list[inx][i] in doub:
                return False
            doub.append(square_list[inx][i])

        inx += 1


    inx = 0
    # each column
    for i in range(1, len(square_list)+1):
        doub = []

        # each item in the column
        for i in range(len(square_list)):
            if not square_list[i][inx] in array(len(square_list)) or square_list[i][inx] in doub:
                return False
            doub.append(square_list[i][inx])

        inx += 1
    return True


    
    
print(check_sudoku(incorrect))
#>>> False

print(check_sudoku(correct))
#>>> True

print(check_sudoku(incorrect2))
#>>> False

print(check_sudoku(incorrect3))
#>>> False

print(check_sudoku(incorrect4))
#>>> False

print(check_sudoku(incorrect5))
#>>> False
