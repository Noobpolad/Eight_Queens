class board:

	def __init__(self,arr):
		self._array = arr
		self._totalCounter = 0

	def chechRow(self,row):
		for col in range(1,9):
			if self._array[row][col] == "Q":
				return False

	def chechCol(self,col):
		for row in range(1,9):
			if self._array[row][col] == "Q":
				return False				
		
	def chechDiagonalLtoR(self,row,col):
		r = row
		c = col
		while self._array[r][c] != 0:
			if self._array[r][c] == "Q":
				return False
			r += 1
			c += 1	
		r = row
		c = col
		while self._array[r][c] != 0:
			if self._array[r][c] == "Q":
				return False
			r -= 1
			c -= 1		
						

	def chechDiagonalRtoL(self,row,col):
		r = row
		c = col
		while self._array[r][c] != 0:
			if self._array[r][c] == "Q":
				return False
			r += 1
			c -= 1	
		r = row
		c = col
		while self._array[r][c] != 0:
			if self._array[r][c] == "Q":
				return False
			r -= 1
			c += 1	

	def allSolved(self):
		counter = 0
		for a in range(1,9):
			for b in range(1,9):
				if self._array[a][b] == "Q":
					counter += 1
		if counter == 8:
			return True		

	def displayOption(self):
		for a in range(1,9):
			for b in range(1,9):
				print(self._array[a][b],end = " ",flush=True)
			print()	
					
	def solution(self):
		for a in range(1,9):
			for b in range(1,9):
				if self.chechRow(a) != False and self.chechCol(b) != False and self.chechDiagonalLtoR(a,b) != False and self.chechDiagonalRtoL(a,b) != False:
					self._array[a][b] = "Q"
					if self.allSolved() == True:
						self.displayOption()
						self._totalCounter += 1
						print()
						print("Number of combinations:",self._totalCounter)	
						print()
					else:	
						self.solution()
					self._array[a][b] = "E"	
			if self.chechRow(a) != False:		
				return False		

playBoard = []  		

for a in range(0,10):
	tmp = ["E"] * 10
	playBoard.append(tmp)

for a in range(0,10):
	for b in range(0,10):
		if a == 0 or b == 0 or a == 9 or b == 9:
			playBoard[a][b] = 0	

b = board(playBoard)
b.solution()
