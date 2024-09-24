class Node:
    def __init__(self, a_number):
        self.data = a_number
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)

    def show_elements(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def length(self):
        result = 0
        current = self.head
        while current is not None:
            result += 1
            current = current.next
        return result

    def get_element(self, position):
        i = 0
        current = self.head
        while current is not None:
            if i == position:
                return current.data
            current = current.next
            i += 1
        return None


list1 = LinkedList()
list1.head = Node(2)
list1.head.next = Node(3)
list1.head.next.next = Node(4)
print(list1.head.data, list1.head.next.data, list1.head.next.next.data)
print('==================================')
print(list1.head.next.next.next)
print('==================================')
print(list1.get_element(2))
print('==================================')
print(list1.length())
list1.append(5)
print('==================================')
list1.show_elements()
print('==================================')
print(list1.length())
