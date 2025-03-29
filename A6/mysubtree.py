

def identity(x):
    return x


def rec(vertex, left, right, colors):
    # vertex is an integer between 1 and n
    # array entry left[j-1] is the index of the left child of node j
    # array entry right[j-1] is the index of the right child of node j
    # array entry colors[j-1] is the color of node j, an integer between 1 and 255
    # left[j-1] and right[j-1] are both zero if node j is a leaf
    vertexidx = vertex - 1
    res = [0] * 3
    
    left_child_id = left[vertexidx]
    right_child_id = right[vertexidx]
    # print(f"parent id: {vertex} | left id: {left_child_id} | right id: {right_child_id}")
    
    # return res
    # if `vertex` is a leaf
    if left[vertexidx] == 0: # if left is nill, then right is nill too
        res[1] = False
        res[2] = 1
        print(f"\t[base case]: ({res})")
        return res
    else:
        parent_col = colors[vertexidx]
        left_col = colors[left_child_id-1]
        right_col = colors[right_child_id-1]
    
        tup_left = rec(left_child_id, left, right, colors)
        tup_right = rec(right_child_id, left, right, colors)

        a = 0
        b = False
        c = 0
        
        if (tup_left[1]):
            pass
        
        if (tup_right[1]):
            pass
        
        elif (parent_col == left_col or parent_col == right_col):   # parent connect's the left and right current sub trees
            c = tup_left[2] + tup_right[2] + 1
            a = max(tup_left[0], tup_right[0], c)   # update max tree size found
        else:
            a = [tup_left[0], tup_right[0]]
            b = True
            c = [tup_left[2], tup_right[2]]
        
        res[0] = max(a, c, tup_left[0], tup_right[0])
        res[1] = b
        res[2] = c
        # if (left_tup[1]):
        #     if (parent_col != left_col):
        #         a = max(left_tup[0][0], left_tup[0][1])
        #         b = False
        #         c = 0
        #     else:   # root_col == left_col
        #         c = left_tup[2][0] + left_tup[2][1] + 1
        #         a = max(c, left_tup[0][0], left_tup[0][1])
        # if (right_tup[1]):
        #     if (parent_col != right_col):
        #         a = max(right_tup[0][0], right_tup[0][1], a)
        #         b = False
        #         c = 0
        #     else:   # root_col == right_col
        #         c1 = right_tup[2][0] + right_tup[2][1] + 1
        #         a = max(c1, right_tup[0][0], right_tup[0][1], a, c)
            
        # elif (parent_col == left_col or parent_col == right_col):
        #     c = left_tup[2] + right_tup[2] + 1
        #     a = max(left_tup[0], right_tup[0], c)
        #     b = False
        # elif ((parent_col != left_col or parent_col != right_col) and (left_tup[2] > 0 or right_tup[2] > 0)):  # or?
        #     a = [left_tup[0], right_tup[0]]
        #     b = True
        #     c = [left_tup[2], right_tup[2]]
        
        print(f"parent id: {vertex} | left id: {left_child_id} | right id: {right_child_id}\n\ttup:{res}")
        # print(f"tup: {res}")
        return res
    
    

def selected(n, root, left, right, colors):
    res = rec(root, left, right, colors)
    sz_subtree = res[0]
    # Output an integer sz_subtree -- insert here --
    # This is the computation of sz_subtree from res
    return sz_subtree

if __name__ == '__main__':
    n = 21
    root = 11
    left = [2,0,0,17,0,4,0,0,0,0,16,3,0,0,0,21,15,19,0,12,10]
    right = [14,0,0,5,0,9,0,0,0,0,18,7,0,0,0,1,8,6,0,13,20]
    colors = [1,3,2,2,3,2,2,1,2,4,3,3,1,1,4,1,4,4,1,4,4]
    # res = [0] * 3
    # print (res)
    # identity()
    val = selected(n, root, left, right, colors)
    print(val if val > 1 else 0)
    
    root = 1
    print(f"root id({root-1}) | left id({left[root-1]-1}) | right id({right[root-1]-1})")
    root = 1
    print(f"root({root}, col[{colors[root-1]}]) | left({left[root-1]}) | right({right[root-1]})")


# The following input is code for the tree shown on the right in the assignment. The nodes are
# always labeled 1 through n. In this test case, the root is node 11, the left child of node 1 is node
# 2, the right child of node 1 is node 14. The fifth entry in both arrays is zero since node 5 is a
# leaf. The colors of nodes 3 and 7 are the same; both color 2, which is shown as a red color in the
# figure.
# n = 21
# root = 11
# left = [2,0,0,17,0,4,0,0,0,0,16,3,0,0,0,21,15,19,0,12,10]
# right = [14,0,0,5,0,9,0,0,0,0,18,7,0,0,0,1,8,6,0,13,20]
# colors = [1,3,2,2,3,2,2,1,2,4,3,3,1,1,4,1,4,4,1,4,4]
# # In figure: 1 = yellow, 2 = red, 3 = purple, 4 = blue
# # colors = [y,p,r,r,p,r,r,y,r,b,p,p,y,y,b,y,b,b,y,b,b]
# The code mysubtree.selected(n,root,left,right,colors) is used to test examples such as
# the above. Insert your recurrences at the three code locations shown above.

        # left_child = left[vertexidx] - 1
        # right_child = right[vertexidx] - 1
        # left_max_size, left_parent_check, left_curr_subtree_size = rec(left_child, left, right, colors)   # call on left child
        # right_max_size, right_parent_check, right_curr_subtree_size = rec(right_child, left, right, colors)   # call on right child

        # if (left_parent_check): # parent needs to check if its child should be included to the  `current_tree`
        #     if (colors[vertexidx] == colors[left_child]):
        #         left_curr_subtree_size += 2 # add parent and child to sub_tree
                
        # elif (colors[vertexidx] == colors[left_child]): # if parent is same color as left child
        #     left_curr_subtree_size += 2 # add parent and child to sub_tree
            
        # if (right_parent_check):
        #     if (colors[vertexidx] == colors[right_child]):
        #         right_curr_subtree_size += 2 # add parent and child sub_tree
        # elif (colors[vertexidx] == colors[right_child]):
        #     right_curr_subtree_size += 2 # add parent and child sub_tree
        
        # if (colors[vertexidx] != colors[left_child] or colors[vertexidx] != colors[right_child]):
        #     res[1] = True
        # else:
        #     res[1] = False
            
        # res[0] = max(res[0], left_curr_subtree_size, right_curr_subtree_size, left_max_size, right_max_size)
        # res[2] = max(left_curr_subtree_size, right_curr_subtree_size)