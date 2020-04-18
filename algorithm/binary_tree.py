class Node(object):
    def __init__(self, item):
        self.item = item  # 表示对应元素
        self.left = None  # 表示左节点
        self.right = None  # 表示右节点

    def __str__(self):
        # print 一个 Node 类时会打印 __str__ 的返回值
        return str(self.item)


class Tree(object):
    def __init__(self):
        # 根节点定义为 root 永不删除，作为哨兵使用
        self.root = Node('root')

    def add(self, item):
        node = Node(item)
        # 如果二叉树为空，那么添加的点将插入root结点处
        if self.root is None:
            self.root = node
        else:
            # 在 q 列表中，添加二叉树的根节点
            q = [self.root]
            while True:
                pop_node = q.pop(0)
                # 左子树为空的则将点添加到左子树
                if pop_node.left is None:
                    pop_node.left = node
                    return
                # 右子树为空的则将点添加右子树
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)

    def get_parent(self, item):
        if self.root.item == item:
            # 根节点没有父节点
            return None
        # 在 tmp 列表中，添加二叉树的根节点
        tmp = [self.root]
        while tmp:
            pop_node = tmp.pop(0)
            # 如果点的左子树为要寻找的点
            if pop_node.left and pop_node.left.item == item:
                # 返回这个点，就是目标结点的父节点
                return pop_node
            # 如果结点的右子树为目标结点
            if pop_node.right and pop_node.right.item == item:
                # 返回该结点，就是目标结点的父节点
                return pop_node
            # 添加 tmp 列表中的元素
            if pop_node.left is not None:
                tmp.append(pop_node.left)
            if pop_node.right is not None:
                tmp.append(pop_node.right)
        return None

    def delete(self, item):
        #如果根节点为空结点，返回
        if self.root is None:
            return False

        parent = self.get_parent(item)
        if parent:
            # 确定待删除结点
            del_node = parent.left
            if parent.left.item == item
            else:
                parent.right
            # 待删除结点的左子树为空
            if del_node.left is None:
                # 如果待删除结点为父节点的左孩子结点，将右孩子移动到左孩子的位置
                if parent.left.item == item:
                    parent.left = del_node.right
                # 待删除结点为右孩子的情况
                else:
                    parent.right = del_node.right
                # 删除 del_node
                del del_node
                return True
            # 待删除结点的右子树为空的情况，处理方法同上
            elif del_node.right is None:
                #
                if parent.left.item == item:
                    parent.left = del_node.left
                #
                else:
                    parent.right = del_node.left
                # 删除del_node
                del del_node
                return True
            else:  # 左右子树都不为空的情况，
                tmp_pre = del_node
                # 待删除结点的右子树
                tmp_next = del_node.right

                # 寻找待删除结点右子树中的最左叶子结点并完成替代
                if tmp_next.left is None:
                    # 替代
                    tmp_pre.right = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                else:
                    # 让 tmp_next 指向右子树的最左叶子结点
                    while tmp_next.left:
                        tmp_pre = tmp_next
                        tmp_next = tmp_next.left
                    # 替代
                    tmp_pre.left = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                # 如果待删除结点是父节点的左孩子
                if parent.left.item == item:
                    parent.left = tmp_next
                # 如果待删除结点是父节点的右孩子
                else:
                    parent.right = tmp_next
                del del_node
                return True
        else:
            return False
