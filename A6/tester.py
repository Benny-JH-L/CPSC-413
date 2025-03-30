import mysubtree
import A6.myleaves_draft as myleaves_draft

if __name__ == '__main__':

    n = 21
    root = 11
    left = [2,0,0,17,0,4,0,0,0,0,16,3,0,0,0,21,15,19,0,12,10]
    right = [14,0,0,5,0,9,0,0,0,0,18,7,0,0,0,1,8,6,0,13,20]
    colors = [1,3,2,2,3,2,2,1,2,4,3,3,1,1,4,1,4,4,1,4,4]
    largest_subtree_size = mysubtree.selected(n, root, left, right, colors)
    print(largest_subtree_size if largest_subtree_size > 1 else 0)  # size 1 is not a valid subtree, so we output 0 for it
    
    # debug
    # root = 1
    # print(f"root id({root-1}) | left id({left[root-1]-1}) | right id({right[root-1]-1})")
    # root = 1
    # print(f"root({root}, col[{colors[root-1]}]) | left({left[root-1]}) | right({right[root-1]})")

    n = 21
    root = 11
    left = [2,0,0,17,0,4,0,0,0,0,16,3,0,0,0,21,15,19,0,12,10]
    right = [14,0,0,5,0,9,0,0,0,0,18,7,0,0,0,1,8,6,0,13,20]
    
    num_leaves = myleaves_draft.selected(n, root, left, right)
    print(num_leaves)
