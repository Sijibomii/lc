# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
def buildTree(preorder, inorder):
    node_to_inorder_idx = {
        data: i for i, data in enumerate(inorder)
    }
    #build the subtree with preorder[preorder_start:preorder_end] and
    # inorder[inorder_start:inorder_end]
    def binary_tree_from_preorder_inorder_helper(preorder_start, preorder_end, inorder_start, inorder_end):
        if preorder_end <= preorder_start or inorder_end <= inorder_start:
            return None
        # preorder_start gives you the node to the current subtree been worked on
        # this is used to retreive the inorder idx 
        root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
        # everything to the left of the inorder_root is on the left subtree
        left_subtree_size = root_inorder_idx - inorder_start
        
        return TreeNode(
            preorder[preorder_start],
            #Recursively builds the left subtree
            binary_tree_from_preorder_inorder_helper(
            preorder_start + 1, preorder_start + 1 + left_subtree_size, inorder_start,
        root_inorder_idx
            ),
            # Recursively builds the right subtree
            binary_tree_from_preorder_inorder_helper(
            preorder_start + 1+ left_subtree_size, preorder_end, root_inorder_idx + 1,
        inorder_end
            ))
        
    return binary_tree_from_preorder_inorder_helper(0, len(preorder), 0, len(inorder)) 