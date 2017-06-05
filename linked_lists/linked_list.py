class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self,newdata):
        self.data = newdata

    def set_next(self,newnext):
        self.next = newnext


class SortedList:
    def __init__(self):
        self.head = None

    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()

        return found

    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def delete(self, data):
        current = self.head
        previous = None

        while current != None:
            if current.data == data:
                if previous == None: # at head of linked list
                    self.head = current.next
                else:
                    previous.next = current.next
                current.next = None # detatch node from linked list
            else:
                previous = current
                current = current.next

        raise ValueError("Data was not found in list")

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()

        return count

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

print(mylist.size())
print(mylist)
print(mylist.search(93))
print(mylist.search(100))

mylist.reverse()
print(mylist)

mylist.delete(77)
print(mylist)
