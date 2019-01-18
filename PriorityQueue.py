import sys

class PriorityQueue:

    def __init__(self, size):
        self.elements = [(0, 99)] * (size + 1)

    def insert(self, target, from_weight): 
        if self.elements[target][1] > from_weight[1]:
            self.elements[target] = from_weight

    def get(self):
        target = self.find_min()
        source = self.elements[target][0]
        self.elements[target] = None
        return target, source

    def find_min(self):
        min = sys.maxsize
        index = None
        for i, element in enumerate(self.elements):
            if element is None:
                continue
            if element[1] < min:
                min = element[1]
                index = i
        return index
