
# CPSC 413 Winter 2025 - Assignment 6 Problem 1
# Ivan Agalakov, Benny Liang
# DRAFT

def identity(x):
    return x


def rec(vertex, left, right):
    # vertex is an integer between 1 and n
    # array entry left[j-1] is the index of the left child of node j
    # array entry right[j-1] is the index of the right child of node j
    # left[j-1] and right[j-1] are both zero if node j is a leaf
    vertexidx = vertex - 1
    res = [0] * 4
    if left[vertexidx] == 0: # if left is nill, then right is nill too
        # Your base case goes here -- insert here --
        res[0] = 0 # distance 0, we are closest to ourselves
        res[1] = 1 # size of one, we are the only leaf node added
        return res
    else:
        # Your recurrences go here -- insert here --
        l = rec(left[vertex-1], left, right)
        r = rec(right[vertex-1], left, right)
        
        leftNum = l[0]+1
        rightNum = r[0]+1

        # if (leftNum + rightNum >= 5): # the distance between left and right is valid, so combine
        #     res[0] = min(leftNum, rightNum) # return the closest node of the two most recently added for further calculations
        #     res[1] = l[1] + r[1] # combine the number of nodes!
        # else:   # otherwise the two of them don't match
        #     if l[1] == r[1]: # if there are the same number of nodes in the left and right subtrees, and we are in a tie, pick the tree based on which one has the furthest closest node
        #         res[0] = max(leftNum, rightNum) # choose furthest leaf of the two
        #         res[1] = l[1] + r[1] - 1
        #     else: # otherwise choose the one with the most leaves
        #         res[0] = leftNum if l[1] > r[1] else rightNum 
        #         res[1] = l[1] + r[1] - 1
        if (leftNum + rightNum >= 5): # the distance between left and right is valid, so combine
            res[0] = min(leftNum, rightNum) # return the closest node of the two most recently added for further calculations
            res[1] = l[1] + r[1] # combine the number of nodes!
        else:   # otherwise the two of them don't match
            res[0] = max(leftNum, rightNum)
            res[1] = l[1] + r[1] - 1

        return res

def selected(n, root, left, right):
    res = rec(root, left, right)
    no_leaves = res[1]
    # Output an integer no_leaves -- insert here --
    # This is the computation of no_leaves from res
    return no_leaves


if __name__ == "__main__":
    identity()

