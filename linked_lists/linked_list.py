class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "Node(%s)" % str(self.data)

class SortedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.next

        return count

    def add(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def search(self, data):
        current = self.head

        while current != None:

            if current.data == data:
                print(current.data)
                return True

        return False

    def delete(self, data):
        current = self.head
        previous = None

        while current != None:
            if current.data == data:
                if previous == None: # at head of linked list
                    self.head = current.next
                else:
                    previous.next = current.next
                current.next = None # detach node from linked list
            else:
                previous = current
                current = current.next

        raise ValueError("Data was not found in list")

    def reverse(self):
        previous = None
        current = self.head

        while current != None:
            next = current.next
            current.next = previous
            previous = current
            current = next

        self.head = previous

    def list_to_data(self):
        data_list = []
        current = self.head

        while current != None:
            data_list.append(current.data)
            current = current.next

        return data_list

    def data_to_list(self, data_list):
        self.head = Node(data_list[0])
        current = self.head

        for data in data_list[1:]:
            current.next = Node(data)
            current = current.next

    def __repr__(self):
        data_list = self.list_to_data()
        return "LinkedList(%s)" % str(data_list)

mylist = SortedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(22)

print(mylist.search(93))
print(mylist.search(100))

print(mylist)
print(mylist.size())

mylist.reverse()
print(mylist)

print(mylist.is_empty())

