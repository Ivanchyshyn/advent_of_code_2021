class TreeNode:
    def __init__(self, value, depth, left=None, right=None, before=''):
        self.value = value
        self.depth = depth
        self.left = left
        self.right = right
        self.before = before

    def __str__(self):
        return f'TreeNode({self.value}, {self.depth})'

    def to_string(self):
        cur = self
        depth = 0
        result = ''
        while cur:
            result += cur.before + str(cur.value)
            depth = cur.depth
            cur = cur.right

        result += ']' * depth
        return result

    def __add__(self, other):
        if not isinstance(other, TreeNode):
            return NotImplemented

        self.before = '[' + self.before
        current = self
        added_other = False
        while current:
            if not added_other and not current.right:
                current.right = other
                other.left = current
                other.before = ']' * current.depth + ',' + other.before
                added_other = True
            current.depth += 1
            current = current.right
        return self

    __iadd__ = __add__
