# CPSC 413 Winter 2025 - Assignment 6 Problem 1
# Ivan Agalakov, Benny Liang

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

        if (leftNum + rightNum >= 5): # the distance between left and right is valid, so combine
            res[0] = min(leftNum, rightNum) # return the closest node of the two most recently added for further calculations
            res[1] = l[1] + r[1] # combine the number of nodes!
        else:   # otherwise the two of them don't match
            res[0] = max(leftNum, rightNum) # choose the furthest distance of the two
            res[1] = l[1] + r[1] - 1 # remove the node that is closer and causes the conflict.

        return res
    
def selected(n, root, left, right):
    res = rec(root, left, right)
    # Output an integer no_leaves -- insert here --
    # This is the computation of no_leaves from res
    no_leaves = res[1]
    return no_leaves

if __name__ == '__main__':
    identity()