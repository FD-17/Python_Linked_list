class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

#append
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            cur=self.head
            while cur.next:
                cur=cur.next
            cur.next=new_node
#insert
    def insert(self,data,pos):
        if pos>self.count():
            print("Error")
        elif pos==0:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
        elif pos==self.count():
            return self.append(data)
        else:
            cur=self.head
            new_node=Node(data)
            count=1
            while count<pos:
                count+=1
                cur=cur.next
            new_node.next=cur.next
            cur.next=new_node
#count
    def count(self):
        total=0
        cur=self.head
        while cur:
            cur=cur.next
            total+=1
        return total

 #display       
    def display(self):
        cur=self.head
        while cur:
            print (cur.data)
            cur=cur.next
            
#Delete
    def delete(self,index):
        count=0
        if index>=self.count():
            print("Error")
        elif index==0:
            cur=self.head
            self.head=cur.next
        else:
            cur=self.head
            i=1
            while i<index:
                cur=cur.next
                i+=1
            cur.next=cur.next.next
            
  #Search
    def Search(self,data):
        cur=self.head
        i=0
        while cur and i<self.count():
            if cur.data==data:
                print('{} is found at index {}'.format(data,i))
                return
            else:
                cur=cur.next
                i+=1
        print('{} is not present'.format(data))

#Setvalue
    def Set(self,data,pos):
        index=0
        cur=self.head
        while cur:
            if index==pos:
               cur.data=data
               return
            cur=cur.next
            index+=1

list=LinkedList()
list.append(9)
list.append(8)
list.append(3)
print(list.count())
list.display()
list.insert(6,3)
list.delete(0)
list.display()
list.Set(0,0)
list.display()
list.Search(4)
