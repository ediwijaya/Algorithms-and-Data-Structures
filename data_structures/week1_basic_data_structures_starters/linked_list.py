class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node

    def insert_at_index(self, data, index):
        new_node = Node(data)
        curr_node = self.head
        position = 0
        if position == index:
            self.insert_at_beginning(data)
        else:
            while (curr_node is not None) and (position + 1 != index):
                position += 1
                curr_node = curr_node.next
            if curr_node is not None:
                new_node.next = curr_node.next
                curr_node.next = new_node
            else:
                print('Index not available')

    def print(self):
        values = []
        curr_node = self.head
        while curr_node:
            values.append(curr_node.data)
            curr_node = curr_node.next
        print(values)
    
    def get_size(self):
        curr_node = self.head
        size = 0
        while curr_node is not None:
            size += 1
            curr_node = curr_node.next
        return size
    
    def pop_front(self):
        curr_node = self.head
        self.head = curr_node.next
        return curr_node.data
    
    def pop_back(self):
        # handle when empty:
        if self.head is None:
            return
        # handle when len is more than one
        try:
            curr_node = self.head
            while curr_node.next.next:
                curr_node = curr_node.next
            result = curr_node.next
            curr_node.next = None
        # case when len is one
        except:
            result = curr_node
            self.head = None
        finally:
            return result.data

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_beginning(1)
    # linked_list.insert_at_beginning(2)
    # linked_list.insert_at_beginning(3)
    # linked_list.insert_at_end(4)
    # linked_list.insert_at_end(5)
    # linked_list.insert_at_index(6, 1)
    # linked_list.print()
    # print(linked_list.get_size())
    # print(linked_list.pop_front())
    linked_list.print()
    print(linked_list.pop_back())
    linked_list.print()