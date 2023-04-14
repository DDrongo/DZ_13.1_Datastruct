import unittest
from Class.Node_and_Stack import Stack

class TestStack(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.top.data, 3)
        self.assertEqual(stack.top.next_node.data, 2)
        self.assertEqual(stack.top.next_node.next_node.data, 1)
