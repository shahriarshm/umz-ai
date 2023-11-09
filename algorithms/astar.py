WIDTH = 4
ACTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Up, Down


class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other) -> bool:
        return other.position == self.position

    def __repr__(self) -> str:
        return f"Node(position={self.position})"


def make_maze(width):
    maze = []
    for _ in range(width):
        row = []
        for _ in range(width):
            row.append(0)
        maze.append(row)
    return maze


def draw_maze(maze):
    for i in range(len(maze)):
        for j in range(len(maze)):
            print(maze[i][j], end=" ")
        print()


def draw_path_on_maze(maze, start, end, path):
    for i in range(len(maze)):
        for j in range(len(maze)):
            p = (i, j)
            if p == start:
                print("S", end=" ")
            elif p == end:
                print("E", end=" ")
            elif p in path:
                print("#", end=" ")
            else:
                print(maze[i][j], end=" ")
        print()


def astar_search(maze, start, end):
    path = []
    open_list = []
    closed_list = []

    start_node = Node(None, start)
    end_node = Node(None, end)

    open_list.append(start_node)

    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0

        # Find the open node with the least f value
        for i, node in enumerate(open_list):
            if node.f < current_node.f:
                current_node = node
                current_index = i

        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the end. Now construct the path
        if current_node == end_node:
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        # Expand all possible moves
        children = []
        for action in ACTIONS:
            new_x, new_y = (
                current_node.position[0] + action[0],
                current_node.position[1] + action[1],
            )
            if (
                (new_x >= 0)
                and (new_y >= 0)
                and (new_x < len(maze))
                and (new_y < len(maze))
            ):
                if maze[new_x][new_y] == 0:
                    child = Node(current_node, (new_x, new_y))
                    children.append(child)

        # Calculate f value for each possible move
        for child in children:
            # If the child is already closed, skip it
            if child in closed_list:
                continue

            child.g = current_node.g + 1
            child.h = ((end_node.position[0] - child.position[0]) ** 2) + (
                (end_node.position[1] - child.position[1]) ** 2
            )
            child.f = child.g + child.h

            # If the node is already opened, skip it
            if child in open_list:
                continue

            open_list.append(child)


def main():
    # maze = make_maze(WIDTH)
    maze = [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    print("Maze:")
    draw_maze(maze)
    print()

    start = (0, 0)
    end = (3, 3)
    print("Start:", start)
    print("End:", end)

    print()
    path = astar_search(maze, start, end)
    print("Result:")
    draw_path_on_maze(maze, start, end, path)


if __name__ == "__main__":
    main()
