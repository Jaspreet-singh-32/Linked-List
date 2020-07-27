class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_end(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node

    def view(self):
        if self.head == None:
            print("Linked List is empty...")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=' -> ')
                if temp.next == None:
                    print(temp.next)
                temp = temp.next

    def add_start(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            self.head = node
            node.next = temp

    def add_given_pos(self, data, pos):
        if pos == 0:
            self.add_start(data)
        elif self.head == None:
            node = Node(data)
            self.head = node
        else:
            node = Node(data)
            temp = self.head
            count = 1
            while temp.next != None:
                if count == pos:
                    node.next = temp.next
                    temp.next = node
                    print(f'{data} Added Successfully...')
                    return
                temp = temp.next
                count += 1
            print('Index out of range...')

    def delete_first(self):
        if self.head == None:
            print('Linked List is empty...')
        else:
            temp = self.head
            self.head = temp.next
            print('First Element Deleted Successfully')

    def delete_last(self):
        if self.head == None:
            print('Linked List is empty...')
        elif self.head.next == None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            temp.next = None
            # print('Last Element Deleted Successfully')

    def delete_given_pos(self, pos):
        if self.head == None:
            print('Linked List is empty...')
        if pos == 0:
            self.delete_first()
        else:
            temp = self.head
            count = 1
            while temp.next != None:
                if count == pos:
                    temp.next = temp.next.next
                    return
                temp = temp.next
                count += 1
            print('Index out of range...')

    def delete_given_data(self, data):
        if self.head == None:
            print('Linked List is empty...')
        elif self.head.data == data:
            self.head = self.head.next
        else:
            temp = self.head
            while temp.next != None:
                if temp.next.data == data:
                    temp.next = temp.next.next
                    return
                temp = temp.next
            print('Data Not Found!')

    def search(self, data):
        if self.head == None:
            print('Linked List is empty...')
        else:
            temp = self.head
            while temp:
                if temp.data == data:
                    print('Data found...')
                    return
                temp = temp.next
            print('Data not found!')


linkedlist = LinkedList()
linkedlist.add_end(6)
linkedlist.add_end(4)
linkedlist.add_end(1)
linkedlist.add_end(3)
linkedlist.add_end(89)
linkedlist.view()
# linkedlist.add_given_pos(10, 1)
# linkedlist.delete_first()
# linkedlist.delete_last()
# linkedlist.delete_given_pos(1)
# linkedlist.delete_given_data(4)
# linkedlist.view()
# linkedlist.add_start(0)
# linkedlist.add_start(10)
# linkedlist.add_end(20)
# linkedlist.view()
# linkedlist.search(83)
