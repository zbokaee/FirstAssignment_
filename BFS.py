from queue import Queue

class BFS:
    def __init__(self, N):
        self.N = int(N)
        self.chessboard = Queue()

    def isLegal(self, chessboard):
        for yi_idx in range(len(chessboard)):
            # column
            for xi_idx in range(yi_idx + 1, len(chessboard)): 
                if chessboard[xi_idx] == chessboard[yi_idx]: 
                    return False
                if abs(chessboard[yi_idx] - chessboard[xi_idx]) == abs(yi_idx - xi_idx): 
                    return False
        return True

    def isGoal(self, chessboard):
        if len(chessboard) == self.N:
            return True
        else:
            return False

    def bfs(self):

        self.chessboard.put([0]) 

        while not self.chessboard.empty():
            queue = self.chessboard.get()

            if self.isGoal(queue):
                queue = [i+1 for i in queue]
                return queue

            for row_pos in range(self.N):
                new_queue = queue + [row_pos]
                if self.isLegal(new_queue):
                    self.chessboard.put(new_queue)
