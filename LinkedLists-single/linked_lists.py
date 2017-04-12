"""
LINKED LISTS
Adventures in Algorithms
"""

# singly-linked list


class Node(object):
    """A basic node class to populate a singly-linked list.
        Deliberately not using "tail", as an exercise.
    """

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


class S_linked_list(object):
    """a robust class for singly-linked lists.
    """

    def __init__(self, head=None):
        self.head = head

    def add_node(self, node):
        """append a new node to the end of the list.
        """

        if self.head:
            # check if list has cycle to prevent infinite while loop
            if self.has_cycle():
                print "error - list has a cycle"
            else:
                current = self.head
                prev = None

                #traverse to the last node in the list so far
                while current:
                    prev = current
                    current = current.next

                prev.next = node

        else:
            self.head = node

    def add_node_by_value(self, value):
        """shortcut for users to create node and append to list in one step.
        """
        node = Node(value)
        self.add_node(node)

    def insert_node_at_index(self, index, node):
        """insert a new node at specific location in list.
        """

        if self.head:
            # check if list has cycle to prevent infinite while loop
            if self.has_cycle():
                print "error - list has a cycle"
                return
            else:
                if index == 0:
                #edge case - inserting at the beginning of list.
                    current = self.head
                    self.head = node
                    node.next = current

                count = 0
                current = self.head
                next_node = current.next

                while next_node:
                    if count == index:
                        current.next = node
                        node.next = next_node
                        return
                    else:
                        current = next_node
                        next_node = current.next
                        count += 1
                return
        else:
            # if list is empty, the only valid case is to insert at 0
            if index == 0:
                self.head = node

        # otherwise, request cannot be completed.
        print "request not valid. out of range"


    def remove_nodes_by_val(self, value):
        """traverse loop. Find any node with the given value
            (may be multiple!) and remove it/them from list.
        """

        if self.head:
            if self.has_cycle():
                print "error - list has a cycle"
                return
            else:
                count = 0
                # if the head itself need to be removed:
                if self.head.data == value:
                    self.head = self.head.next
                    count += 1

                #traverse list
                current = self.head
                prev = current
                
                while current:
                # to correct a cycle???
                    if current.data == value:
                        # make prev point to next, cutting current out of list
                        prev.next = current.next
                        # prev doesn't change, but traverse to next node for evaluation
                        current = current.next
                        count += 1
                    else:
                        #traverse to the next node for evaluation
                        prev = current
                        current = current.next

                print "\n", value, "was found and deleted", count, "time(s)."

    def remove_node_by_index(self, index):
        """remove node at a specific location in list.
        """

        if self.head:
            if index == 0:
                self.head = self.head.next
                return

            count = 1
            # since we've already accounted for removing the head
            # we are staging the loop from the next position.
            prev = self.head
            current = prev.next

            while current:

                if count == index:
                    prev.next = current.next
                    print "deleted node at", index, "with value of", current.data
                    return
                else:
                    prev = current
                    current = current.next
                    count += 1

            print "Request not valid."

        else:
            print "Request not valid. List is empty."

    def print_list(self):

        if self.head:
            # check if list has cycle to prevent infinite while loop
            if self.has_cycle():
                print "error - list has a cycle"
            else:
                current = self.head

                while current:
                    print current.data,
                    current = current.next
                print "\n"
        else:
            print "list is currently empty"

    def has_cycle(self):

        current = self.head
        seen = set()

        while current:
            node_hash = hash(current)

            if node_hash in seen:
                return True

            seen.add(node_hash)

            current = current.next

        return False

    def reverse_list(self):
        
        if self.head:
            if self.has_cycle():
                print "error - list has a cycle"
            else:
                prev = None
                current = self.head

                while current:
                    print current.data

                    next_node = current.next
                    current.next = prev

                    prev = current
                    current = next_node

                self.head = prev

        else:
            return


if __name__ == '__main__':

    ll = S_linked_list()
    ll.print_list()

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

    # next line create cycle in list :(
    # ll.add_node("d")

    ll.print_list()

    ll.remove_nodes_by_val("d")
    ll.print_list()

    ll.add_node_by_value("monkey")
    ll.print_list()

    f = Node("f")

    ll.insert_node_at_index(3, f)
    ll.print_list()

    ll.reverse_list()
    ll.print_list()
