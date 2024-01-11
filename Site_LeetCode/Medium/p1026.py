
max_diff = 0 #global variable

class Solution(object):

    def maxAncestorDiff(self, root):
        global max_diff #global variable
        max_diff = 0

        def divide_sub(node, min_val, max_val):
            global max_diff #global variable

            if not node: # base case
                return

            min_val = min(min_val, node.val) #update min value
            max_val = max(max_val, node.val) #update max value

            max_diff = max(max_diff, max_val - min_val) #update max_diff

            divide_sub(node.left, min_val, max_val) #DFS to left
            divide_sub(node.right, min_val, max_val) #DFS to right
 
        divide_sub(root, root.val, root.val) #start

        return max_diff #return