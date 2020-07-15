#The elements in the example arrays above can be accessed by indexing like lists in Python such that:
a[0] = 6,  a[3] = 9, b[0, 0] = 1 , b[1, 2] = 6 c[0, 1] = 8.  

#Elements in arrays  can also be retrieved by slicing rows and columns or a combination of indexing and slicing.
d[1,  0:2] = array([9., 8.])

e = np.array([[10, 11, 12],[13, 14, 15], 
              [16, 17, 18],[19, 20, 21]])

# slicing
e[:3, :2] = array([[10, 11], [13, 14],[16, 17]])

#There are other advanced methods of indexing which are shown below.
# integer indexing
e[[2, 0, 3, 1],[2, 1, 0, 2]] = array([18, 11, 19, 15])

# boolean indexing meeting a specified condition
e[e>15] = array([16, 17, 18, 19, 20, 21])
