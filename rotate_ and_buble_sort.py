class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.start_node = None

    # Печать списка
    def traverse_list(self):
        if self.start_node is None:
            print("Список пуст")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.ref


    # Вставка в начало
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node

    # Вставка в конец
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node;


    # Построение списка
    def make_new_list(self):
        nums = int(input("Количество элементов для вставки: "))
        if nums == 0:
            return
        for i in range(nums):
            value = int(input("Значение элемента:"))
            self.insert_at_end(value)


    # реверс списка
    def reverse_linkedlist(self):
        prev = None
        n = self.start_node
        while n is not None:
            next = n.ref
            n.ref = prev
            prev = n
            n = next
        self.start_node = prev

    # Сортировка пузырьком
    def buble_sort(self):
        end = None
        while end != self.start_node:
            p = self.start_node
            while p.ref != end:
                q = p.ref
                if p.item > q.item:
                    p.item, q.item = q.item, p.item
                p = p.ref
            end = p


new_linked_list = LinkedList()
new_linked_list.insert_at_end(5)
new_linked_list.insert_at_end(15)
new_linked_list.insert_at_end(10)
new_linked_list.insert_at_end(6)
new_linked_list.insert_at_end(2)

print('Исходный список')
new_linked_list.traverse_list()

new_linked_list.reverse_linkedlist()
print('Реверс списка')
new_linked_list.traverse_list()

new_linked_list.buble_sort()
print('Сортировка списка')
new_linked_list.traverse_list()

