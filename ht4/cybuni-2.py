import math

class Vector:
    def __init__(self, components):
        self.components = components

    def __str__(self):
        return '(' + ','.join(map(str, self.components)) + ')'

    def equals(self, other_vector):
        return self.components == other_vector.components

    def add(self, other_vector):
        if len(self.components) != len(other_vector.components):
            raise ValueError("need same len")
        result = [x + y for x, y in zip(self.components, other_vector.components)]
        return result

    def subtract(self, other_vector):
        if len(self.components) != len(other_vector.components):
            raise ValueError("need same len")
        result = [x - y for x, y in zip(self.components, other_vector.components)]
        return result

    def dot(self, other_vector):
        if len(self.components) != len(other_vector.components):
            raise ValueError("need same len")
        result = sum(x * y for x, y in zip(self.components, other_vector.components))
        return result

    def norm(self):
        return math.sqrt(sum(x ** 2 for x in self.components))