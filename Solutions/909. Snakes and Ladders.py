class Solution(object):
    def snakesAndLadders(self, board):
        # because there is only one way to traverse besides a special condidtion we can just slap all the arrays together
        new_board = []
        cur_pos, exit = None, None

        for i, row in enumerate(reversed(board)):
            if i % 2 == 0:
                new_board = new_board + row
            else:
                new_board = new_board + list(reversed(row))

        # now set up the game loop
        cur_pos = 0
        exit = len(new_board) - 1

        # because there is the potential to go back to old pos, set up a set to keep track and avoid infinite loop
        # have a queue for places to visit

        potential = collections.deque()
        potential_set = set()
        turn = 0

        potential_set.add(0)
        potential.append((cur_pos, turn))

        while potential:
            cur_pos, turn = potential.popleft()
            turn += 1

            max_move = None
            for move in range(1, 7):
                if cur_pos + move > exit:
                    break

                if cur_pos + move == exit or new_board[cur_pos + move] - 1 == exit:
                    return turn

                if new_board[cur_pos + move] != -1 and new_board[cur_pos + move] - 1 not in potential_set:
                    potential_set.add(new_board[cur_pos + move] - 1)
                    potential.append((new_board[cur_pos + move] - 1, turn))

                elif new_board[cur_pos + move] == -1:
                    max_move = cur_pos + move

            if max_move and max_move not in potential_set:
                potential_set.add(max_move)
                potential.append((max_move, turn))

        return -1













