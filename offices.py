class Solution(object):
    def numOffices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited_coordinates = list()
        offices = list()
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if (i, j) in visited_coordinates:
                    continue
                visited_coordinates.append((i, j))
                if grid[i][j] == "1":
                    actual_office = list()
                    actual_office.append((i, j))
                    spaces_pending_to_visit = list()
                    spaces_pending_to_visit.append((i, j + 1))
                    spaces_pending_to_visit.append((i + 1, j))
                    while spaces_pending_to_visit:
                        actual_i, actual_j = spaces_pending_to_visit.pop(0)
                        try:
                            if grid[actual_i][actual_j] == "1":
                                spaces_pending_to_visit.append((actual_i, actual_j + 1))
                                spaces_pending_to_visit.append((actual_i + 1, actual_j))
                                actual_office.append((actual_i, actual_j))
                            visited_coordinates.append((actual_i, actual_j))
                        except IndexError:
                            pass
                    offices.append(actual_office)

        return len(offices)


def get_matrix():
    row = int(input())
    col = int(input())
    grid = [["0"] * col] * row

    for i in range(row):
        line = input()
        grid[i] = list(line)[0:col]
    return grid


if __name__ == "__main__":
    sol = Solution()
    matrix = get_matrix()
    offices = sol.numOffices(matrix)
    print(offices)
