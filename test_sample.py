if __name__ == "__main__":
    l1 = Node()
    ListNode_1 = Node_handle()
    l1_list = [1, 8, 3]
    for i in l1_list:
        l1 = ListNode_1.add(i)





class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

if __name__='__main__':
    nodelist=[TreeNode(i)for i in [4,2,7,1,3,5,8]]
    nodelist[0].left=nodelist[1]
    nodelist[0].right=nodelist[2]
    nodelist[1].left=nodelist[3]
    nodelist[1].right=nodelist[4]
    nodelist[2].left=nodelist[5]
    nodelist[2].right=nodelist[6]
    root = nodelist[0]
    print('二叉树根节点为：',root)
    print('前序遍历',preOrder(root))
    print('前序遍历',inOrder(root))