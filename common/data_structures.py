from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(set)

    def add_edge(self, u, v):
        if u == v:
            raise ValueError("Cannot add an edge between the same vertex")
        self.graph[u].add(v)

    def remove_edge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)

    def get_graph(self):
        return self.graph


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Cannot dequeue from an empty queue")

    def __str__(self):
        return str(self.items)


class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._items[-1]

    def size(self):
        return len(self._items)
