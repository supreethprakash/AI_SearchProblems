import random

# Class represents playing desk
class Desk(object):

    SHUFFLE_NUMBER = 20 # changing to 200 and higher ruins everything
    def __init__(self, width, height):
        self.matrix =[]
        for i in range(height):
            row = [x + 1 for x in range(i * width, (i+1) * width)]
            self.matrix.append(row)
        self.matrix[height - 1][ width - 1] = 0

    def height(self):
        return len(self.matrix)

    def width(self):
        return len(self.matrix[0])

    def __str__(self):
        str_list = []
        for r in self.matrix:
            for c in r:
                str_list.append(str(c) + "\t")
            str_list.append("\n")
        str_list.pop()
        return "".join(str_list)

    def __eq__(self, other):
        if (self.width() != other.width() or self.height() != other.height()):
            return False
        for r in range(self.height()):
            for c in range(self.width()):
                if self.matrix[r][c] != other.matrix[r][c]:
                    return False;
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.__str__())

    def shuffle(self):
        #for i in range(Desk.SHUFFLE_NUMBER):
            #self.matrix = self.neighbors()[random.randint(0, len(self.neighbors()) - 1)].matrix
        self.matrix = [[5,7,8,1],[10,2,4,3],[6,9,11,12],[15,13,14,0]]


    def get_element(self, row, col):
        return self.matrix[row][col]

    def set_element(self, row, col, value):
        self.matrix[row][col] = value

    def copy(self):
        newDesk = Desk(self.width(), self.height())
        for r in range(self.height()):
            for c in range(self.width()):
                newDesk.set_element(r, c, self.matrix[r][c])
        return newDesk

    def heuristic_cost(self):
        totalSum = 0
        for r in range(self.height()):
            for c in range(self.width()):
                n = self.matrix[r][c] - 1
                if (n == -1):
                    n = self.width() * self.height() - 1
                r_solved = n / self.height()
                c_solved = n % self.width()
                totalSum += abs(r - r_solved)
                totalSum += abs(c - c_solved)
        return totalSum

    def swap(self, r1, c1, r2, c2):
        term = self.matrix[r1][c1]
        self.matrix[r1][c1] = self.matrix[r2][c2]
        self.matrix[r2][c2] = term

    def neighbors(self):
        neighbors = []
        w = self.width()
        h = self.height()
        for r in range(h):
            for c in range(w):
                if (self.matrix[r][c] == 0):
                    if (r != 0):
                        neighbor = self.copy()
                        neighbor.swap(r, c, r - 1, c)
                        neighbors.append(neighbor)
                    if (r != h - 1):
                        neighbor = self.copy()
                        neighbor.swap(r, c, r + 1, c)
                        neighbors.append(neighbor)
                    if (c != 0):
                        neighbor = self.copy()
                        neighbor.swap(r, c, r, c - 1)
                        neighbors.append(neighbor)
                    if (c != w - 1):
                        neighbor = self.copy()
                        neighbor.swap(r, c, r, c + 1)
                        neighbors.append(neighbor)
        return neighbors


# Class represents the game
class Puzzle15(object):

    def __init__(self, width=4, height=4):
        self.desk = Desk(width, height)
        self.desk.shuffle()
        self.steps = 0

    def __str__(self):
        return str(self.desk)

    def __repr__(self):
        return str(self.desk)

    def lowest_score_element(self, openset, score):
        min_score = 2**30
        min_elem = None

        for elem in openset:
            if (elem in score.keys()):
                if (score[elem] < min_score):
                    min_elem = elem
                    min_score = score[elem]

        return min_elem

    def get_solution(self):
        start = self.desk.copy()
        goal = Desk(self.desk.width(), self.desk.height())

        closed_set = []
        openset = [start]
        came_from = {}

        g_score = { start: 0 }
        f_score = { start: g_score[start] + start.heuristic_cost()}

        while len(openset) != 0:
            current = self.lowest_score_element(openset, f_score)
            if (current == goal):
                return self.reconstruct_path(came_from, current)

            openset.remove(current)
            closed_set.append(current)
            neighbors = current.neighbors()
            for neighbor in neighbors:
                tentative_g_score = g_score[current] + 1
                tentative_f_score = tentative_g_score + neighbor.heuristic_cost()

                if neighbor in closed_set and f_score.has_key(neighbor) and tentative_f_score >= f_score[neighbor]:
                    continue

                if neighbor not in openset or (f_score.has_key(neighbor) and tentative_f_score < f_score[neighbor]):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_f_score
                    if neighbor not in openset:
                        openset.append(neighbor)
                self.steps += 1
        return None

    def reconstruct_path(self, came_from, current_node):
        if (came_from.has_key(current_node)):
            p = self.reconstruct_path(came_from, came_from[current_node])
            return p + [current_node]
        else:
            return [current_node]



if __name__ == '__main__':

    puzzle = Puzzle15(4,4)
    solution = puzzle.get_solution()
    print puzzle.steps
    for s in solution:
        print s
        print