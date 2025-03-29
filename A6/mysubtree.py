

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
        res[0] = 0      # a = 0
        res[1] = False  # b = False
        res[2] = 1      # c = 1
        print(f"\t[base case]: ({res})")
        return res
    else:
        parent_col = colors[vertexidx]
        left_col = colors[left_child_id-1]
        right_col = colors[right_child_id-1]
    
        left_a, left_b, left_c = rec(left_child_id, left, right, colors)
        right_a, right_b, right_c = rec(right_child_id, left, right, colors)

        a = 0
        b = False
        c = 0
        include_parent = False  # should we count the parent in the current valid sub tree size
        
        # case for left child
        if (left_col == parent_col):
            include_parent = True
            c += left_c
            if (left_b):    # This child was not included in the current sub tree size, becuase it needed to be checked,
                c += 1      # add it to the sub tree size
        # Left child may not be the same color as its parent but we could potentially still add the left child's current sub tree
        # size to this current sub tree size, thus we need to ask this left child's grandparent (parent of parent) if its parent 
        # can be included to the current sub tree size
        elif (left_col != parent_col and left_c > 1 and (not left_b)):
            c += left_c
            b = True
        
        # case for right child, will be similar case to left child
        if (right_col == parent_col):
            include_parent = True
            c += right_c
            if (right_b):
                c += 1
        elif (right_col != parent_col and right_c > 1 and (not right_b)):
            c += right_c
            b = True
        
        if (include_parent):
            c += 1              # add parent to current valid sub tree
            b = False           # if the parent was added to current subtree then no need to ask its parent (parent of parent) to check if can be included to the current tree
        
        # case, need to check parent of parent whether or not parent is included to current subtree
        if (b):
            a = max(left_a, right_a)
            res[0] = a
            res[1] = b
            res[2] = c
            return res
        
        a = max(left_a, right_a, c)
        c = max(c, 1)   # case where a parent can make no valid sub tree (ie, both children are leaves and are different color to the parent)
        res[0] = a
        res[1] = b
        res[2] = c
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
        
        
# rec() PSUEDO CODE (most recent, Mar 28 9;07pm):
# a = 0
# b = false
# c = 0
# c_arr = []
# include_parent = false

# if (left color = parent color):
#     //c++
#     include_parent = true
#     c += left.c
#     //if (left.a = 0 and left.c = 1)// for parent with leaf child
#         //c++
#     if (left.b)
#         c++
# // left child may not be same color but its subtree 
# // could still be added to curr_tree, need parent check
# else if (left color != parent color & left.c > 1 & !left.b):
#     //c_arr[0] = left.c
#     c += c.left
#     b = true

# if (right color = parent color):
#     include_parent = true

#     //if (right.b = true):
#         // // c += right.b[1]
#         // c += right.c
#     c += right.c
#     if (right.b)
#         c++
#     //else if (right.a = 0 and right.c = 1)// for parent with leaf child
#         //c++ 
# // right child may not be same color but its subtree 
# // could still be added to curr_tree, need parent check
# else if (right color != parent color & right.c > 1 & !right.b):
#     // c_arr[1] = right.c
#     c += c.right
#     b = true
   
# if (include_parent) // add parent to curr_tree
#     c++
#     b = false // if the parent was added to curr_subtree then no need to ask its parent to check if it can be included to curr_subtree

# if (b = True):
#     a = max(left.a, right.a)
#     return [a,b,c] // [a, b, c_arr]

# a = max(left.a, right.a, c)
# return [a, False, c]
