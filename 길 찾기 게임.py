#부모의 자식을 찾는 것보다 자식을 부모에 소속시켜주는 게 낫다
#level에 따라 분류(y값 사용), level을 통일했을 때 순서를 리스트로 만들었을 때 리스트에서의 인덱스를 기록(x값 사용)
#
import sys
sys.setrecursionlimit(10**6)


# class TreeNode():
#     def __init__(self, idx, x, y):
#         self.idx = idx
#         self.x = x
#         self.y = y
#         self.child = []

        
# class PreTree():
#     def __init__(self, root_node):
#         self.route = []
#         self.root = root_node
        
#     def visit(self, node:TreeNode):
#         self.route.append(node.idx)
        
#     def __dfs_pre(self, curNode:TreeNode):
#         if curNode == None:
#             return
#         self.visit(curNode)
#         for childNode in curNode.child:
#             self.__dfs_pre(childNode)
            
#     def dfs(self):
#         self.__dfs_pre(self.root)
#         return self.route
        
        
# class PostTree():
#     def __init__(self, root_node):
#         self.route = []
#         self.root = root_node
        
#     def visit(self, node:TreeNode):
#         self.route.append(node.idx)
        
#     def __dfs_post(self, curNode:TreeNode):
#         if curNode == None:
#             return
#         for child in curNode.child:
#             self.__dfs_post(child)
#         self.visit(curNode)
            
#     def dfs(self):
#         self.__dfs_post(self.root)
#         return self.route

# # def solution(nodeinfo):
# #     node_list = sorted([TreeNode(index + 1, node[0], node[1]) for index, node in enumerate(nodeinfo)], key = lambda node: (node.y, node.x), reverse = True)
# #     levels = sorted(list(set([n[1] for n in nodeinfo])))
# #     level_list_dict = {level : [] for level in levels}
                        
# #     for node in node_list:
# #         level_list_dict[node.y].append(node)
# #     level_list = list(level_list_dict.values())
# #     node_xsort = sorted([n for n in node_list], key = lambda n: n.x)
# #     node_xsort_dict = {node : idx for idx, node in enumerate(node_xsort)}
    
# #     for level_idx, level in enumerate(level_list):
# #         if level == level_list[-1]:
# #             continue
# #         for node in level:
# #             parent_node = min(level_list[level_idx + 1], key = lambda p_node: (abs(node_xsort_dict[p_node] - node_xsort_dict[node]), p_node.x))
# #             parent_node.child.append(node)
    
# #     for node in node_list:
# #         node.child = sorted(node.child, key = lambda child: child.x)
        
# #     Pre = PreTree(node_list[0]).dfs()
# #     Post = PostTree(node_list[0]).dfs()
# #     answer = [Pre, Post]
# #     return answer

# def add_node(parent, child):
#     if child.x < parent.x:
#         if parent.child and parent.child[0].x < parent.x:
#             add_node(parent.child[0], child)
#         else:
#             parent.child.insert(0, child)
#     else:
#         if len(parent.child) > 1 and parent.child[1].x > parent.x:
#             add_node(parent.child[1], child)
#         else:
#             if len(parent.child) == 0:
#                 parent.child.append(child)
#             else:
#                 parent.child.append(child)

# def solution(nodeinfo):
#     node_list = sorted([TreeNode(index + 1, node[0], node[1]) for index, node in enumerate(nodeinfo)], key=lambda node: (-node.y, node.x))
#     root = node_list[0]

#     for i in range(1, len(node_list)):
#         add_node(root, node_list[i])

#     Pre = PreTree(root).dfs()
#     Post = PostTree(root).dfs()
#     return [Pre, Post]

class TreeNode:
    def __init__(self, idx, x, y):
        self.idx = idx
        self.x = x
        self.y = y
        self.left = None
        self.right = None

class PreTree:
    def __init__(self, root_node):
        self.route = []
        self.root = root_node
        
    def visit(self, node: TreeNode):
        self.route.append(node.idx)
        
    def __dfs_pre(self, curNode: TreeNode):
        if curNode is None:
            return
        self.visit(curNode)
        self.__dfs_pre(curNode.left)
        self.__dfs_pre(curNode.right)
            
    def dfs(self):
        self.__dfs_pre(self.root)
        return self.route

class PostTree:
    def __init__(self, root_node):
        self.route = []
        self.root = root_node
        
    def visit(self, node: TreeNode):
        self.route.append(node.idx)
        
    def __dfs_post(self, curNode: TreeNode):
        if curNode is None:
            return
        self.__dfs_post(curNode.left)
        self.__dfs_post(curNode.right)
        self.visit(curNode)
            
    def dfs(self):
        self.__dfs_post(self.root)
        return self.route

def add_node(parent, child):
    if child.x < parent.x:
        if parent.left is None:
            parent.left = child
        else:
            add_node(parent.left, child)
    else:
        if parent.right is None:
            parent.right = child
        else:
            add_node(parent.right, child)

def solution(nodeinfo):
    nodes = [TreeNode(idx+1, x, y) for idx, (x, y) in enumerate(nodeinfo)]
    nodes.sort(key=lambda n: (-n.y, n.x))
    
    root = nodes[0]
    for node in nodes[1:]:
        add_node(root, node)
    
    pre_order = PreTree(root).dfs()
    post_order = PostTree(root).dfs()
    
    return [pre_order, post_order]




    
        