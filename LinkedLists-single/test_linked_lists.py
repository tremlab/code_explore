import unittest
from linked_lists import Node, S_linked_list


class LL_tests(unittest.TestCase):

    def test_has_cycle_is_true(self):
        print "1"
        ll.add_node(d)
        self.assertEqual(ll.has_cycle(), True)

    def test_remove_node_by_index_is_valid(self):
        print "2"
        ll.remove_node_by_index(1)
        self.assertEqual(ll.head.next.data, "c")

    def test_has_cycle_is_false(self):
        print "3"
        self.assertEqual(ll.has_cycle(), False)

    def test_insert_node_at_index_is_valid(self):
        print "4"
        ll.insert_node_at_index(1, b)
        self.assertEqual(ll.head.next.data, "b")







if __name__ == "__main__":

    # due to scope, can't declare these in setUp()

    ll = S_linked_list()

    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")

    ll.add_node(a)
    ll.add_node(b)
    ll.add_node(c)
    ll.add_node(d)
    ll.add_node(e)

    # run tests
    unittest.main()
