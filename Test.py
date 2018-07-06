from timeit import default_timer as timer
from sudokucsp import SudokuCSP
from csp import AC3
from csp import backtracking_search, mrv, unordered_domain_values, forward_checking, mac, no_inference


class Test:

    def __init__(self):
        # empty board
        self.original_board = [[0 for j in range(9)] for i in range(9)]

    def set_board(self, difficulty):
        if difficulty == 0:
            self.original_board[0] = [3, 0, 1, 7, 0, 0, 0, 0, 6]
            self.original_board[1] = [9, 0, 0, 0, 0, 0, 0, 0, 0]
            self.original_board[2] = [0, 0, 8, 0, 5, 6, 0, 1, 0]
            self.original_board[3] = [0, 0, 0, 2, 0, 5, 8, 0, 0]
            self.original_board[4] = [2, 8, 3, 0, 0, 0, 6, 5, 1]
            self.original_board[5] = [0, 0, 9, 8, 0, 3, 0, 0, 0]
            self.original_board[6] = [0, 9, 0, 4, 3, 0, 1, 0, 0]
            self.original_board[7] = [0, 0, 0, 0, 0, 0, 0, 0, 2]
            self.original_board[8] = [6, 0, 0, 0, 0, 2, 3, 0, 7]

        elif difficulty == 1:
            self.original_board[0] = [0, 4, 7, 0, 8, 0, 0, 0, 3]
            self.original_board[1] = [0, 0, 0, 0, 0, 1, 0, 0, 0]
            self.original_board[2] = [2, 0, 0, 0, 0, 0, 0, 0, 7]
            self.original_board[3] = [0, 0, 0, 0, 4, 0, 1, 0, 2]
            self.original_board[4] = [0, 1, 0, 0, 0, 2, 0, 9, 0]
            self.original_board[5] = [0, 0, 0, 3, 0, 8, 0, 0, 0]
            self.original_board[6] = [0, 8, 0, 0, 0, 9, 7, 0, 0]
            self.original_board[7] = [0, 3, 6, 0, 0, 4, 0, 0, 0]
            self.original_board[8] = [4, 0, 1, 0, 0, 3, 0, 0, 0]

        elif difficulty == 2:
            self.original_board[0] = [0, 2, 5, 0, 0, 0, 3, 0, 0]
            self.original_board[1] = [1, 0, 0, 4, 0, 9, 0, 0, 0]
            self.original_board[2] = [0, 0, 0, 2, 0, 0, 9, 0, 6]
            self.original_board[3] = [8, 0, 1, 0, 0, 0, 0, 3, 0]
            self.original_board[4] = [0, 3, 7, 0, 1, 0, 0, 5, 0]
            self.original_board[5] = [0, 0, 0, 0, 0, 7, 0, 0, 1]
            self.original_board[6] = [3, 0, 0, 6, 0, 0, 0, 0, 5]
            self.original_board[7] = [0, 1, 0, 0, 5, 0, 0, 0, 7]
            self.original_board[8] = [0, 9, 0, 0, 0, 4, 8, 0, 0]

        if difficulty == 3:
            self.original_board[0] = [0, 0, 0, 0, 2, 0, 0, 0, 5]
            self.original_board[1] = [0, 0, 1, 6, 0, 0, 0, 0, 0]
            self.original_board[2] = [0, 6, 0, 7, 0, 0, 0, 8, 1]
            self.original_board[3] = [0, 0, 0, 3, 0, 0, 5, 0, 0]
            self.original_board[4] = [3, 0, 8, 5, 0, 6, 2, 0, 9]
            self.original_board[5] = [0, 0, 4, 0, 0, 7, 0, 0, 0]
            self.original_board[6] = [7, 4, 0, 0, 0, 9, 0, 1, 0]
            self.original_board[7] = [0, 0, 0, 0, 0, 5, 9, 0, 0]
            self.original_board[8] = [8, 0, 0, 0, 7, 0, 0, 0, 0]

        elif difficulty == 4:
            self.original_board[0] = [2, 0, 0, 0, 0, 0, 0, 4, 3]
            self.original_board[1] = [1, 9, 0, 0, 3, 0, 0, 0, 0]
            self.original_board[2] = [0, 6, 0, 0, 0, 5, 0, 0, 0]
            self.original_board[3] = [0, 5, 0, 2, 6, 0, 0, 0, 8]
            self.original_board[4] = [0, 0, 0, 0, 7, 0, 0, 0, 0]
            self.original_board[5] = [6, 0, 0, 0, 5, 3, 0, 1, 0]
            self.original_board[6] = [0, 0, 0, 6, 0, 0, 0, 2, 0]
            self.original_board[7] = [0, 0, 0, 0, 8, 0, 0, 3, 4]
            self.original_board[8] = [9, 1, 0, 0, 0, 0, 0, 0, 6]

        elif difficulty == 5:
            self.original_board[0] = [8, 0, 0, 0, 0, 0, 0, 0, 0]
            self.original_board[1] = [0, 0, 3, 6, 0, 0, 0, 0, 0]
            self.original_board[2] = [0, 7, 0, 0, 9, 0, 2, 0, 0]
            self.original_board[3] = [0, 5, 0, 0, 0, 7, 0, 0, 0]
            self.original_board[4] = [0, 0, 0, 0, 4, 5, 7, 0, 0]
            self.original_board[5] = [0, 0, 0, 1, 0, 0, 0, 3, 0]
            self.original_board[6] = [0, 0, 1, 0, 0, 0, 0, 6, 8]
            self.original_board[7] = [0, 0, 8, 5, 0, 0, 0, 1, 0]
            self.original_board[8] = [0, 9, 0, 0, 0, 0, 4, 0, 0]

    #at the beginning, reduce the variable's domains with AC3, if the game
    #is not trivial, it starts with backtracking
    def start(self, inf):
        s = SudokuCSP(self.original_board)
        if AC3(s):
            if s.is_solved():
                print(" ")
                print("\nSolution found with AC3")
            else:
                self.start = timer()
                a = backtracking_search(s, select_unassigned_variable=mrv, order_domain_values=unordered_domain_values,
                                        inference=inf)
                self.end = timer()
                if a:
                    print(" ")
                    print("\nSolution found")
                    for i in range(9):
                        print(" ")
                        for j in range(9):
                            name = i * 9 + j
                            print(" " + str(a["CELL"+str(name)]) + " ", end='')
                else:
                    print("\nPlease check the sudoku initial board, solution not found!")
                self.bt = s.n_bt

    def display(self):
        time = round(self.end - self.start, 5)
        print("Time: " + str(time) + " seconds")
        print("N. BT: " + str(self.bt))


def main():
    time = []
    back_track = []
    n_test = 5
    # modify inf to the type of inference that you want to do after assign a value
    # options are no_inference, forward_checking and mac
    inf = no_inference
    # difficulty can assume 6 values: if the number increases, the difficulty increases
    difficulty = 0

    # to add a new board, and add a clause "elif self.difficulty == 6:
    #                                                             self.original_board[0] = first row
    #                                                             ...
    #                                                             self.original_board[8] = last row
    for i in range(n_test):
        t1 = Test()
        t1.set_board(difficulty)
        t1.start(inf)
        back_track.append(t1.bt)
        time.append(round(t1.end - t1.start, 5))

    print("\naverage time:" + str(sum(time) / len(time)))
    print("average bt:" + str(sum(back_track) / len(back_track)))


if __name__ == '__main__':
    main()
