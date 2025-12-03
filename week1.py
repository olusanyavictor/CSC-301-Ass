# Node class
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

# LinkedList class
class LinkedList:
    def _init_(self):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Delete a node by key
    def delete_node(self, key):
        temp = self.head

        # If head node itself holds the key
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        # Search for the key
        prev = None
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next

        # Key not found
        if temp is None:
            print(f"Node with data {key} not found.")
            return

        # Unlink the node
        prev.next = temp.next
        temp = None

    # Display the linked list
    def display_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Testing the LinkedList
llist = LinkedList()

# Insert at beginning and end
llist.insert_at_end(10)
llist.insert_at_beginning(20)
llist.insert_at_end(30)
llist.insert_at_beginning(40)
llist.insert_at_end(50)

print("Linked List after insertion:")
llist.display_list()

# Delete a node
llist.delete_node(30)
print("Linked List after deleting 30:")
llist.display_list()