# LAB4
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return f"Node({self.value})"

    __repr__ = __str__
                        
                          
class SortedLinkedList:
    '''
        >>> x=SortedLinkedList()
        >>> x.add(8.76)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(5)
        >>> x.add(3)
        >>> x.add(-7.5)
        >>> x.add(4)
        >>> x.add(9.78)
        >>> x.add(4)
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 1 -> 1 -> 3 -> 4 -> 4 -> 5 -> 8.76 -> 9.78
        >>> x.removeDuplicates()
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 3 -> 4 -> 5 -> 8.76 -> 9.78
        >>> sub1, sub2 = x.split()
        >>> sub1
        Head:Node(-7.5)
        Tail:Node(4)
        List:-7.5 -> 1 -> 3 -> 4
        >>> sub2
        Head:Node(5)
        Tail:Node(9.78)
        List:5 -> 8.76 -> 9.78
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 3 -> 4 -> 5 -> 8.76 -> 9.78
    '''

    def __init__(self):   # You are not allowed to modify the constructor
        self.head=None
        self.tail=None

    def __str__(self):   # You are not allowed to modify this method
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out) 
        return f'Head:{self.head}\nTail:{self.tail}\nList:{out}'

    __repr__=__str__


    def isEmpty(self):
        return self.head is None

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            current = current.next
            count += 1
        return count

                
    def add(self, value):
        # --- YOUR CODE STARTS HERE
        x = Node(value)
        if self.isEmpty():
            self.head = x
            self.tail = x
        elif x.value <= self.head.value:
            x.next = self.head
            self.head = x
        else:
            y = self.head
            while y.next is not None and y.next.value < x.value:
                y = y.next
            if y.next is None:
                self.tail = x
            x.next = y.next
            y.next = x
        pass


    def split(self):
        # --- YOUR CODE STARTS HERE
        first = SortedLinkedList()
        second = SortedLinkedList()
        x = self.head
        if len(self)%2 == 1:
            length = int(len(self)/2) + 1
        else:
            length = int(len(self)/2)       
        for val in range(length):
            first.add(x.value)
            x = x.next
        while x is not None:
            second.add(x.value)
            x = x.next
        return first, second
        pass


    def removeDuplicates(self):
        # --- YOUR CODE STARTS HERE
        x = self.head
        while x is not None and x.next is not None:
            if x.value == x.next.value:
                x.next = x.next.next
            else:
                x = x.next
        pass

if __name__=='__main__':
    import doctest
    doctest.testmod()