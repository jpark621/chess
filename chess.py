from pprint import pprint

class King:
	def __init__(self, player, position, board):
		self.player = player
		self.position = position
		self.board = board

		# check protection for checkmating
		self.protects = []
		self.protected_by = []

	def moves(self):
		position = self.position
		moves = set()
		for i in range(position[0] - 1, position[0] + 2):
			for j in range(position[1] - 1, position[1] + 2):
				if not (i == self.position[0] and j == self.position[1]):
					moves.add((i, j))
		new_moves = set()
		for move in moves:
			if move[0] >= 0 and move[0] < 8 and move[1] >= 0 and move[1] < 8:
				new_moves.add(move)
		moves = new_moves
		new_moves = set()
		for move in moves:
			if not (board[move[0]][move[1]] and board[move[0]][move[1]].player == self.player):
				new_moves.add(move)
		moves = new_moves
		new_moves = set()
		for move in moves:
			if not (board[move[0]][move[1]] and board[move[0]][move[1]].player != self.player and board[move[0]][move[1]].protected_by):
				new_moves.add(move)
		moves = new_moves
		return moves

	def validate_move(self, end_position):
		return end_position in self.moves()

	def move(self, end_position):
		self.unprotect()
		board = self.board
		start, end = self.position, end_position
		board[start[0]][start[1]] = None
		board[end[0]][end[1]] = self
		self.position = end_position
		self.protect()

	def attacks(self):
		return self.moves()

	def protect(self):
		position = self.position
		board = self.board
		moves = set()
		for i in range(position[0] - 1, position[0] + 2):
			for j in range(position[1] - 1, position[1] + 2):
				if not (i == self.position[0] and j == self.position[1]):
					moves.add((i, j))
		new_moves = set()
		for move in moves:
			if move[0] >= 0 and move[0] < 8 and move[1] >= 0 and move[1] < 8:
				new_moves.add(move)
		moves = new_moves
		new_moves = set()
		for move in moves:
			if board[move[0]][move[1]] and board[move[0]][move[1]].player == self.player:
				board[move[0]][move[1]].protected_by.append(self)
				self.protects.append(board[move[0]][move[1]])

	def unprotect(self):
		for piece in self.protects:
			piece.protected_by.remove(self)
		self.protects = []

	def to_string(self):
		return "k" + ("w" if self.player else "b")


class Queen:
	def __init__(self, player, position, board):
		self.player = player
		self.position = position
		self.board = board

		# check protection for checkmating
		self.protects = []
		self.protected_by = []

	def moves(self):
		position = self.position
		board = self.board
		moves = set()
		for j in range(position[1] + 1, 8):
			i = position[0] - (j - position[1])
			if i < 0:
				break
			if board[i][j]:
				if board[i][j].player != self.player:
					moves.add((i, j))
				break
			moves.add((i, j))
		for j in range(position[1] - 1, -1, -1):
			i = position[0] + (position[1] - j)
			if i > 7:
				break
			if board[i][j]:
				if board[i][j].player != self.player:
					moves.add((i, j))
				break
			moves.add((i, j))
		for j in range(position[1] + 1, 8):
			i = position[0] + (j - position[1])
			if i > 7:
				break
			if board[i][j]:
				if board[i][j].player != self.player:
					moves.add((i, j))
				break
			moves.add((i, j))
		for j in range(position[1] - 1, -1, -1):
			i = position[0] - (position[1] - j)
			if i < 0:
				break
			if board[i][j]:
				if board[i][j].player != self.player:
					moves.add((i, j))
				break
			moves.add((i, j))
		for i in range(position[0] - 1, -1, -1):
			j = position[1]
			if board[i][j]:
				if board[i][j].player != self.player:
					moves.add((i, j))
				break
			moves.add((i, j))
		for i in range(position[0] + 1, 8):
			j = position[1]
			if board[i][j]:
				if board[i][j].player != self.player:
					moves.add((i, j))
				break
			moves.add((i, j))
		for j in range(position[1] + 1, 8):
			i = position[0]
			if board[i][j]:
				if board[i][j].player != self.player:
					moves.add((i, j))
				break
			moves.add((i, j))
		for j in range(position[1] - 1, -1, -1):
			i = position[0]
			if board[i][j]:
				if board[i][j].player != self.player:
					moves.add((i, j))
				break
			moves.add((i, j))
		return moves

	def validate_move(self, end_position):
		return end_position in self.moves()

	def move(self, end_position):
		self.unprotect()
		board = self.board
		start, end = self.position, end_position
		board[start[0]][start[1]] = None
		board[end[0]][end[1]] = self
		self.position = end_position
		self.protect()

	def attacks(self):
		return self.moves()

	def protect(self):
		position = self.position
		board = self.board
		for j in range(position[1] + 1, 8):
			i = position[0] - (j - position[1])
			if i < 0:
				break
			if board[i][j]:
				if board[i][j].player == self.player:
					piece = board[i][j]
					piece.protected_by.append(self)
					self.protects.append(piece)
				break
		for j in range(position[1] - 1, -1):
			i = position[0] + (position[1] - j)
			if i > 7:
				break
			if board[i][j]:
				if board[i][j].player == self.player:
					piece = board[i][j]
					piece.protected_by.append(self)
					self.protects.append(piece)
				break
		for j in range(position[1] + 1, 8):
			i = position[0] + (j - position[1])
			if i > 7:
				break
			if board[i][j]:
				if board[i][j].player == self.player:
					piece = board[i][j]
					piece.protected_by.append(self)
					self.protects.append(piece)
				break
		for j in range(position[1] - 1, -1):
			i = position[0] - (position[1] - j)
			if i < 0:
				break
			if board[i][j]:
				if board[i][j].player == self.player:
					piece = board[i][j]
					piece.protected_by.append(self)
					self.protects.append(piece)
				break
		for i in range(position[0] - 1, -1):
			j = position[1]
			if board[i][j]:
				if board[i][j].player == self.player:
					piece = board[i][j]
					piece.protected_by.append(self)
					self.protects.append(piece)
				break
		for i in range(position[0] + 1, 8):
			j = position[1]
			if board[i][j]:
				if board[i][j].player == self.player:
					piece = board[i][j]
					piece.protected_by.append(self)
					self.protects.append(piece)
				break
		for j in range(position[1] + 1, 8):
			i = position[0]
			if board[i][j]:
				if board[i][j].player == self.player:
					piece = board[i][j]
					piece.protected_by.append(self)
					self.protects.append(piece)
				break
		for j in range(position[1] - 1, -1):
			i = position[0]
			if board[i][j]:
				if board[i][j].player == self.player:
					piece = board[i][j]
					piece.protected_by.append(self)
					self.protects.append(piece)
				break

	def unprotect(self):
		for piece in self.protects:
			piece.protected_by.remove(self)
		self.protects = []

	def to_string(self):
		return "q" + ("w" if self.player else "b")

class Bishop:
	def __init__(self, player, position, board):
		self.player = player
		self.position = position
		self.board = board

		# check protection for checkmating
		self.protects = []
		self.protected_by = []

	def moves(self):
		position = self.position
		board = self.board
		moves = set()
		for j in range(position[1] + 1, 8):
			i = position[0] - (j - position[1])
			if i < 0:
				break
			if board[i][j]:
				if board[i][j].player != self.player:
					moves.add((i, j))
				break
			moves.add((i, j))
		for j in range(position[1] - 1, -1, -1):
			i = position[0] + (position[1] - j)
			if i > 7:
				break
			if board[i][j]:
				if board[i][j].player != self.player:
					moves.add((i, j))
				break
			moves.add((i, j))
		for j in range(position[1] + 1, 8):
			i = position[0] + (j - position[1])
			if i > 7:
				break
			if board[i][j]:
				if board[i][j].player != self.player:
					moves.add((i, j))
				break
			moves.add((i, j))
		for j in range(position[1] - 1, -1, -1):
			i = position[0] - (position[1] - j)
			if i < 0:
				break
			if board[i][j]:
				if board[i][j].player != self.player:
					moves.add((i, j))
				break
			moves.add((i, j))
		return moves

	def validate_move(self, end_position):
		return end_position in self.moves()

	def move(self, end_position):
		self.unprotect()
		board = self.board
		start, end = self.position, end_position
		board[start[0]][start[1]] = None
		board[end[0]][end[1]] = self
		self.position = end_position
		self.protect()

	def attacks(self):
		return self.moves()

	def protect(self):
		position = self.position
		board = self.board
		for j in range(position[1] + 1, 8):
			i = position[0] - (j - position[1])
			if i < 0:
				break
			if board[i][j]:
				if board[i][j].player == self.player:
					piece = board[i][j]
					piece.protected_by.append(self)
					self.protects.append(piece)
				break
		for j in range(position[1] - 1, -1):
			i = position[0] + (position[1] - j)
			if i > 7:
				break
			if board[i][j]:
				if board[i][j].player == self.player:
					piece = board[i][j]
					piece.protected_by.append(self)
					self.protects.append(piece)
				break
		for j in range(position[1] + 1, 8):
			i = position[0] + (j - position[1])
			if i > 7:
				break
			if board[i][j]:
				if board[i][j].player == self.player:
					piece = board[i][j]
					piece.protected_by.append(self)
					self.protects.append(piece)
				break
		for j in range(position[1] - 1, -1):
			i = position[0] - (position[1] - j)
			if i < 0:
				break
			if board[i][j]:
				if board[i][j].player == self.player:
					piece = board[i][j]
					piece.protected_by.append(self)
					self.protects.append(piece)
				break

	def unprotect(self):
		for piece in self.protects:
			piece.protected_by.remove(self)
		self.protects = []


	def to_string(self):
		return "b" + ("w" if self.player else "b")

class Knight:
	def __init__(self, player, position, board):
		self.player = player
		self.position = position
		self.board = board

		# check protection for checkmating
		self.protects = []
		self.protected_by = []

	def moves(self):
		position = self.position
		board = self.board
		moves = set()
		i, j = position
		adds = [(-2, 1), (-2, -1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
		for i2, j2 in adds:
			moves.add((i + i2, j + j2))
		new_moves = set()
		for move in moves:
			if move[0] >= 0 and move[0] < 8 and move[1] >= 0 and move[1] < 8:
				new_moves.add(move)
		moves = new_moves
		new_moves = set()
		for move in moves:
			if not (board[move[0]][move[1]] and board[move[0]][move[1]].player == self.player):
				new_moves.add(move)
		moves = new_moves
		return moves

	def validate_move(self, end_position):
		return end_position in self.moves()

	def move(self, end_position):
		self.unprotect()
		board = self.board
		start, end = self.position, end_position
		board[start[0]][start[1]] = None
		board[end[0]][end[1]] = self
		self.position = end_position
		self.protect()

	def attacks(self):
		return self.moves()

	def protect(self):
		position = self.position
		board = self.board
		moves = set()
		i, j = position
		adds = [(-2, 1), (-2, -1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
		for i2, j2 in adds:
			moves.add((i + i2, j + j2))
		new_moves = set()
		for move in moves:
			if move[0] >= 0 and move[0] < 8 and move[1] >= 0 and move[1] < 8:
				new_moves.add(move)
		moves = new_moves
		new_moves = set()
		for move in moves:
			if board[move[0]][move[1]] and board[move[0]][move[1]].player == self.player:
				piece = board[move[0]][move[1]]
				piece.protected_by.append(self)
				self.protects.append(piece)

	def unprotect(self):
		for piece in self.protects:
			piece.protected_by.remove(self)
		self.protects = []

	def to_string(self):
		return "n" + ("w" if self.player else "b")

class Rook:
	def __init__(self, player, position, board):
		self.player = player
		self.position = position
		self.board = board

		# check protection for checkmating
		self.protects = []
		self.protected_by = []

	def moves(self):
		position = self.position
		board = self.board
		moves = set()
		for i in range(position[0] - 1, -1, -1):
			j = position[1]
			if board[i][j]:
				if board[i][j].player != self.player:
					moves.add((i, j))
				break
			moves.add((i, j))
		for i in range(position[0] + 1, 8):
			j = position[1]
			if board[i][j]:
				if board[i][j].player != self.player:
					moves.add((i, j))
				break
			moves.add((i, j))
		for j in range(position[1] + 1, 8):
			i = position[0]
			if board[i][j]:
				if board[i][j].player != self.player:
					moves.add((i, j))
				break
			moves.add((i, j))
		for j in range(position[1] - 1, -1, -1):
			i = position[0]
			if board[i][j]:
				if board[i][j].player != self.player:
					moves.add((i, j))
				break
			moves.add((i, j))
		return moves

	def validate_move(self, end_position):
		return end_position in self.moves()

	def move(self, end_position):
		self.unprotect()
		board = self.board
		start, end = self.position, end_position
		board[start[0]][start[1]] = None
		board[end[0]][end[1]] = self
		self.position = end_position
		self.protect()

	def attacks(self):
		return self.moves()

	def protect(self):
		position = self.position
		board = self.board
		for i in range(position[0] - 1, -1):
			j = position[1]
			if board[i][j]:
				if board[i][j].player == self.player:
					piece = board[i][j]
					piece.protected_by.append(self)
					self.protects.append(piece)
				break
		for i in range(position[0] + 1, 8):
			j = position[1]
			if board[i][j]:
				if board[i][j].player == self.player:
					piece = board[i][j]
					piece.protected_by.append(self)
					self.protects.append(piece)
				break
		for j in range(position[1] + 1, 8):
			i = position[0]
			if board[i][j]:
				if board[i][j].player == self.player:
					piece = board[i][j]
					piece.protected_by.append(self)
					self.protects.append(piece)
				break
		for j in range(position[1] - 1, -1):
			i = position[0]
			if board[i][j]:
				if board[i][j].player == self.player:
					piece = board[i][j]
					piece.protected_by.append(self)
					self.protects.append(piece)
				break

	def unprotect(self):
		for piece in self.protects:
			piece.protected_by.remove(self)
		self.protects = []


	def to_string(self):
		return "r" + ("w" if self.player else "b")

class Pawn:
	def __init__(self, player, position, board):
		self.player = player
		self.position = position
		self.board = board
		self.has_not_moved = True

		# check protection for checkmate
		self.protects = []
		self.protected_by = []

	def moves(self):
		moves = set()
		if self.player:
			moves.add((self.position[0] - 1, self.position[1]))
			if self.has_not_moved:
				moves.add((self.position[0] - 2, self.position[1]))

			new_moves = set()
			for move in moves:
				if move[0] >= 0 and move[0] < 8 and move[1] >= 0 and move[1] < 8:
					new_moves.add(move)
			moves = new_moves
			new_moves = set()
			for move in moves:
				if not (board[move[0]][move[1]] and board[move[0]][move[1]].player == self.player):
					new_moves.add(move)
			moves = new_moves

			if self.position[0] > 0 and self.position[1] > 0 and self.board[self.position[0] - 1][self.position[1] - 1] and \
				self.board[self.position[0] - 1][self.position[1] - 1].player != self.player:
				moves.add((self.position[0] - 1, self.position[1] - 1))
			if self.position[0] > 0 and self.position[1] < 7 and self.board[self.position[0] - 1][self.position[1] + 1] and \
				self.board[self.position[0] - 1][self.position[1] + 1].player != self.player:
				moves.add((self.position[0] - 1, self.position[1] + 1))
		else:
			moves.add((self.position[0] + 1, self.position[1]))
			if self.has_not_moved:
				moves.add((self.position[0] + 2, self.position[1]))

			new_moves = set()
			for move in moves:
				if move[0] >= 0 and move[0] < 8 and move[1] >= 0 and move[1] < 8:
					new_moves.add(move)
			moves = new_moves
			new_moves = set()
			for move in moves:
				if not (board[move[0]][move[1]] and board[move[0]][move[1]].player == self.player):
					new_moves.add(move)
			moves = new_moves

			if self.position[0] < 7 and self.position[1] > 0 and self.board[self.position[0] + 1][self.position[1] - 1] and \
				self.board[self.position[0] + 1][self.position[1] - 1].player != self.player:
				moves.add((self.position[0] + 1, self.position[1] - 1))
			if self.position[0] < 7 and self.position[1] < 7 and self.board[self.position[0] + 1][self.position[1] + 1] and \
				self.board[self.position[0] + 1][self.position[1] + 1].player != self.player:
				moves.add((self.position[0] + 1, self.position[1] + 1))
		return moves

	def validate_move(self, end_position):
		return end_position in self.moves()

	def move(self, end_position):
		self.unprotect()
		board = self.board
		start, end = self.position, end_position
		board[start[0]][start[1]] = None
		board[end[0]][end[1]] = self
		self.position = end_position
		self.has_not_moved = False
		self.protect()

	def attacks(self):
		attacks = set()
		if self.player:
			if self.position[0] > 0 and self.position[1] > 0:
				attacks.add((self.position[0] - 1, self.position[1] - 1))
			if self.position[0] > 0 and self.position[1] < 7:
				attacks.add((self.position[0] - 1, self.position[1] + 1))
		else:
			if self.position[0] < 7 and self.position[1] > 0:
				attacks.add((self.position[0] + 1, self.position[1] - 1))
			if self.position[0] < 7 and self.position[1] < 7:
				attacks.add((self.position[0] + 1, self.position[1] + 1))
		return attacks

	def protect(self):
		if self.player:
			if self.position[0] > 0 and self.position[1] > 0 and self.board[self.position[0] - 1][self.position[1] - 1] and \
				self.board[self.position[0] - 1][self.position[1] - 1].player == self.player:
				piece = self.board[self.position[0] - 1][self.position[1] - 1]
				piece.protected_by.append(self)
				self.protects.append(piece)
			if self.position[0] > 0 and self.position[1] < 7 and self.board[self.position[0] - 1][self.position[1] + 1] and \
				self.board[self.position[0] - 1][self.position[1] + 1].player != self.player:
				piece = self.board[self.position[0] - 1][self.position[1] + 1]
				piece.protected_by.append(self)
				self.protects.append(piece)
		else:
			if self.position[0] < 7 and self.position[1] > 0 and self.board[self.position[0] + 1][self.position[1] - 1] and \
				self.board[self.position[0] + 1][self.position[1] - 1].player != self.player:
				piece = self.board[self.position[0] + 1][self.position[1] - 1]
				piece.protected_by.append(self)
				self.protects.append(piece)
			if self.position[0] < 7 and self.position[1] < 7 and self.board[self.position[0] + 1][self.position[1] + 1] and \
				self.board[self.position[0] + 1][self.position[1] + 1].player != self.player:
				piece = self.board[self.position[0] + 1][self.position[1] + 1]
				piece.protected_by.append(self)
				self.protects.append(piece)

	def unprotect(self):
		for piece in self.protects:
			piece.protected_by.remove(self)
		self.protects = []

	def to_string(self):
		return "p" + ("w" if self.player else "b")

type_decoder = {
	"k": King,
	"q": Queen,
	"b": Bishop,
	"n": Knight,
	"r": Rook,
	"p": Pawn
}
def string_to_piece(s, position, board):
	type, player = s[0], (True if s[1] == "w" else False)
	return type_decoder[type](player, position, board)

def convert_string_board_to_board(string_board):
	board = []
	for i in range(len(string_board)):
		row = string_board[i]
		new_row = []
		for j in range(len(row)):
			if row[j] == "  ":
				new_row.append(None)
			else:
				new_row.append(string_to_piece(row[j], (i, j), board))
		board.append(new_row)
	return board

def convert_board_to_string_board(board):
	string_board = []
	for i in range(len(board)):
		row = board[i]
		new_row = []
		for j in range(len(row)):
			if not row[j]:
				new_row.append("  ")
			else:
				new_row.append(row[j].to_string())
		string_board.append(new_row)
	return string_board

def protect_pieces(board):
	# Call protect on all pieces
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j]:
				board[i][j].protect()
	return board

is_white_turn = True
string_board = [
["rb", "nb", "bb", "kb", "qb", "bb", "nb", "rb"],
["pb", "pb", "pb", "pb", "pb", "pb", "pb", "pb"],
["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
["pw", "pw", "pw", "pw", "pw", "pw", "pw", "pw"],
["rw", "nw", "bw", "kw", "qw", "bw", "nw", "rw"]
]
# is_white_turn = False
# string_board = [
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "kb"],
# ["  ", "  ", "  ", "  ", "  ", "pw", "pw", "  "],
# ["  ", "  ", "  ", "  ", "  ", "kw", "pw", "  "],
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
# ]
# is_white_turn = True
# string_board = [
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "kb"],
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
# ["  ", "  ", "  ", "  ", "  ", "kw", "  ", "  "],
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
# ["  ", "  ", "  ", "  ", "  ", "  ", "qw", "  "]
# ]
# is_white_turn = True
# string_board = [
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "kb"],
# ["  ", "  ", "  ", "  ", "  ", "kw", "  ", "  "],
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "bw"],
# ["  ", "  ", "  ", "  ", "  ", "bw", "  ", "  "],
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
# ]
# is_white_turn = True
# string_board = [
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "kb"],
# ["  ", "  ", "  ", "  ", "  ", "kw", "  ", "  "],
# ["  ", "  ", "  ", "  ", "  ", "nw", "  ", "  "],
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "nw"],
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
# ]
# is_white_turn = True
# string_board = [
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "kb"],
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
# ["  ", "  ", "  ", "  ", "  ", "  ", "kw", "  "],
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
# ["  ", "  ", "  ", "  ", "  ", "rw", "  ", "  "]
# ]
board = convert_string_board_to_board(string_board)
board = protect_pieces(board)

def find_piece(piece_string, board):
	for i in range(len(board)):
		for j in range(len(board)):
			if board[i][j] and board[i][j].to_string() == piece_string:
				return board[i][j]
	return None


def all_in(set1, set2):
	for x in set1:
		if x not in set2:
			return False
	return True

def player_threatens(player, board):
	pieces = []
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] and board[i][j].player == player:
				pieces.append(board[i][j])
	attacks = set()
	for piece in pieces:
		attacks.update(piece.attacks())
	return attacks


def decode_move(move):
	LETTERS = set("abcdefgh")
	NUMBERS = set("12345678")
	if not (len(move) == 5 and (move[0] in LETTERS and move[1] in NUMBERS and move[2] == " " and move[3] in LETTERS and move[4] in NUMBERS)):
		return None, None
	start = (7 - (int(move[1]) - 1), ord(move[0]) - ord('a'))
	end = (7 - (int(move[4]) - 1), ord(move[3]) - ord('a'))
	return start, end

while not (is_white_turn and find_piece("kw", board).position in player_threatens(False, board) and all_in(find_piece("kw", board).moves(), player_threatens(False, board))) and \
		not (not is_white_turn and find_piece("kb", board).position in player_threatens(True, board) and all_in(find_piece("kb", board).moves(), player_threatens(True, board))):
	pprint(convert_board_to_string_board(board))
	move = input()
	if move == "surrender":
		break
	start, end = decode_move(move)
	if start == None:
		continue

	if not board[start[0]][start[1]]:
		continue
	piece = board[start[0]][start[1]]
	if piece.player != is_white_turn:
		continue
	if (is_white_turn and find_piece("kw", board).position in player_threatens(False, board)) or \
		(not is_white_turn and find_piece("kb", board).position in player_threatens(True, board)):
		if not isinstance(piece, King):
			continue

	if not isinstance(piece, King):
		if not piece.validate_move(end):
			continue
		piece.move(end)
	else:
		if not piece.validate_move(end):
			continue
		if end in player_threatens(is_white_turn, board):
			continue
		piece.move(end)

	board = protect_pieces(board)

	if is_white_turn:
		is_white_turn = False
	else:
		is_white_turn = True


pprint(convert_board_to_string_board(board))
if (is_white_turn and find_piece("kw", board).position in player_threatens(False, board) and all_in(find_piece("kw", board).moves(), player_threatens(False, board))):
	print("Black wins!")
elif (not is_white_turn and find_piece("kb", board).position in player_threatens(True, board) and all_in(find_piece("kb", board).moves(), player_threatens(True, board))):
	print("White wins!")
else:
	if is_white_turn:
		print("White wins!")
	else:
		print("Black wins!")
