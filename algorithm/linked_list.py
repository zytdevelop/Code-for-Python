class Node:
    '''
    创建一个Node类,作为单链表的基础数据结构:节点,并初始化对应的内参
    '''
    def __init__(self, data):
        self.data = data  # 表示对应的元素值
        self.next = None  # 表示下一个节点

class Linked_list:
    '''
    创建单链表类,并初始化对应内参
    '''
    def __init__(self, head=None):  # 链表初始化函数
        self.head = head  # 表示链表的头节点元素

    def append(self, new_element):
        '''
        向链表添加新的节点
        '''
        current = self.head  # 将头节点指向临时变量
        if self.head:    # 当头部节点存在时
            while current.next:    # 循环遍历到链表的最后一个元素
                current = current.next
            current.next = new_element
        else:    # 头部节点不存在
            self.head = new_element

    def is_empty(self):
        '''
        判断是否为空链表
        '''
        return not bool(self.head)

    def insert(self, position, new_element):
        '''
        向链表指定位置插入新节点
        '''
        if position < 0 or position > self.get_length():
            raise IndexError('超出链表索引范围')
        temp = self.head
        if position == 0:
            new_element.next, self.head = temp, new_element
            return
        i = 0
        while i < position:
            pre, temp = temp, temp.next
            i += 1
        pre.next, new_element.next = new_element, temp

    def print_list(self):
        '''
        遍历链表
        '''
        print("linked_list: ")
        temp = self.head
        new_list = []
        while temp is not None:
            new_list.append(temp.data)
            temp = temp.next
        print(new_list)
        return

    def remove(self, position):
        '''
        删除指定索引的链表元素
        '''
        if position < 0 or position > self.get_length():
            raise IndexError('删除元素的位置超出范围')

        i = 0
        temp = self.head
        while temp != None:
            if position == 0:
                self.head = temp.next
                temp.next = None
                return True
            pre, temp = temp, temp.next

            i += 1
            if i == position:
                pre.next, temp.next = temp.next, None
                return

    def reverse(self):
        '''
        反转链表
        '''
        prev = None
        current = self.head
        while current:
            next_node, current.next = current.next, prev
            prev, current = current, next_node
        self.head = prev

    def initlist(self, data_list):
        '''
        将列表转换为链表
        '''
        self.head = Node(data_list[0])
        temp = self.head
        for i in data_list[1:]:
            node = Node(i)
            temp.next = node
            temp = temp.next



