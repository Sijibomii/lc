# this soln works
def buildTree(self, inorder, postorder):
    map_inorder = {}
    for i, val in enumerate(inorder): map_inorder[val] = i
    def recur(low, high):
        if low > high: return None
        x = TreeNode(postorder.pop())
        mid = map_inorder[x.val]
        x.right = recur(mid+1, high)
        x.left = recur(low, mid-1)
        return x
    return recur(0, len(inorder)-1)

# keep trying this

# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
def buildTree(inorder, postorder):
    # dic storing data: inorder_idx
    node_to_inorder_idx = {
        data: i for i, data in enumerate(inorder)
    }

    def binary_tree_from_inorder_postorder_helper(inorder_start, inorder_end, postorder_start, postorder_end):
        # stopping cond
        if inorder_start >= inorder_end or postorder_start >= postorder_end:
            return None

        # get the current root. note this is post order
        root_inorder_idx = node_to_inorder_idx[postorder[postorder_end]]

        right_subtree_size = inorder_end - root_inorder_idx

        return TreeNode(
            # val, i.e current root been worked on
            postorder[postorder_end],
            # left node pointing to this root. left subree for this root goes from inorder_start to root_inorder_idx
            binary_tree_from_inorder_postorder_helper(inorder_start, root_inorder_idx - 1, postorder_start, postorder_end - 1 - right_subtree_size),
            # right
            binary_tree_from_inorder_postorder_helper(root_inorder_idx+1, inorder_end, postorder_start, postorder_end - 1)
        )
    
    return binary_tree_from_inorder_postorder_helper(0, len(inorder)-1, 0, len(postorder)-1) 