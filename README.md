This repository contains my implementation of a Singly Linked List using Python.
The assignment includes:
	•	Creating a Node class
	•	Creating a LinkedList class
	•	Implementing the following methods:
	•	insert_at_beginning(data)
	•	insert_at_end(data)
	•	delete_node(key)
	•	display_list()
	•	Testing the linked list with at least 5 inserted values and 1 deletion
	•	Providing answers to short and discussion questions on Linked Lists, Arrays, ADTs, Stacks, and Queues.

⸻

📌 Linked List Code Description

The Python program includes:
	1.	A Node Class that stores:
	•	data
	•	next pointer
	2.	A LinkedList Class that includes:
	•	Insert at beginning
	•	Insert at end
	•	Delete a node by key
	•	Display the list

At the bottom of the code, the list is tested with insertions, deletion, and printed output.

⸻

🧪 Testing Performed
	•	Inserted 5 values:
40, 20, 10, 30, 50
	•	Deleted value:
30
	•	Displayed the list before and after deletion.

⸻

❓ Short Answer Questions

1. Difference between arrays and linked lists
	•	Arrays have fixed size and elements are stored contiguously in memory.
	•	Linked lists are dynamic and each node is stored anywhere in memory, connected using pointers.
	•	Arrays allow fast access by index, while linked lists require traversal.

2. Time complexity of insertion in a linked list
	•	Insertion at beginning → O(1)
	•	Insertion at end → O(n) (unless a tail pointer is used)

⸻

💬 Discussion Questions

1. Key differences between primitive data types and ADTs
	•	Primitive types store single values (int, float, char).
	•	ADTs (Stacks, Queues, Lists) store collections of data with defined operations.

2. Why arrays are static and linked lists dynamic
	•	Arrays have fixed memory allocation.
	•	Linked lists allocate memory node-by-node, so they grow or shrink at runtime.

3. When to prefer a linked list over an array
	•	When frequent insertions or deletions are needed.
	•	When the size of the data is unknown or changes often.

4. Real-world examples
	•	Stack:
	•	Undo operation in MS Word
	•	Browser back button
	•	Function call stack
	•	Queue:
	•	Printer job queue
	•	Customer service queue
	•	Task scheduling
	•	Linked List:
	•	Music playlist
	•	Image slideshow
	•	Train compartments linked together
