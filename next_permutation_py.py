"""
[1,2,3,4,5]
1. find the first entry from the right that is smaller than the entry immediately after it. here that equals 4. i.e from the right only 5 is sorted in desc order
2. Swap the smallest entry after index inversion_point that is greater than perm[inversion_point]. Since entries after the inversion point are in decreasing order,
   if we search in reverse order, the first entry that is greater than perm[inversion_point] is the entry to swap with.
3. Entries in perm are now currently arranged in decreasing order after inversion_point, so we simply reverse these entries to get thee smallest dictionary order
   i.e sort in acscending order
"""

# [1,2,3,7,6,5,4] -> [1,2,4,7,6,5,3]
def next_permutation(perm):
    #1
    inversion_point = len(perm) - 2
    while (inversion_point >= 0 and perm[inversion_point] >= perm[inversion_point + 1]):
        inversion_point -= 1
    if inversion_point == -1:
        #perm is the last
        return perm.sort()
    #2
    for i in reversed(range(inversion_point+1, len(perm))):
        if perm[i] > perm[inversion_point]:
            perm[inversion_point], perm[i] = perm[i], perm[inversion_point]
            break
    
    #3
    perm[inversion_point + 1:] = reversed(perm[inversion_point + 1:])
    return perm

print(next_permutation([1,2,3,4,5]))
print(next_permutation([1,2,3,7,6,5,4]))