# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

def check_vector(vector):
	#print "check vector", vector
	checked = []
	for i in range(1,len(vector) + 1):
		try:
			if i in vector:
				if i not in checked:
					checked.append(i)
				else:
					print "Duplicate", i
					return False
			else:
				print "Not in vector", i
				return False
		except:
			print "Error", i
			return False
	return True

def check_rows(matrix):
	for i in range(len(matrix)):
		v = matrix[i]
		if not check_vector(v):
			return False
	return True

def check_columns(matrix):
	for j in range(len(matrix)):
		v = []
		for i in range(len(matrix)):
			v.append(matrix[i][j])
		if not check_vector(v):
			return False
	return True

def check_sudoku(matrix):
	if check_rows(matrix) and check_columns(matrix):
		return True
	else:
		return False

print check_rows([ [0,1,2], [2,0,1], [1,2,0] ])