def levenshtein_distance(s1, s2):
    # s2 is the shortest one
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    """ We are computing the value of the matrix of the optimal editing values row by row,
    keeping in memory just the previous row and the current one.
    Row 0 and column 0 are for the trivial cases (transforming an empty string into the other one).
    Then, note that the matrix size is (len(s1)+1) * (len(s2)+1):
        the character in the first position (i.e., at position 0) in any string is considered
        when the value with index 1 is computed, and so on and so forth  """

    previous_row = range(len(s2) + 1)
    #debug
    print('row',0,':',previous_row)
    
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            #value of the matrix if we add a char and consider this same position/column j+1 in the previous row i
            insertions = previous_row[ j+1 ] + 1
            #value of the matrix if we delete a char and consider the previous position j in the current row i+1
            deletions  = current_row[ j ] + 1
            #value of the matrix if we change a character or do not modify, and consider the previous position j in the previous row i
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        #debug
        print('row',i+1,':',current_row)
        
        previous_row = current_row
    
    return previous_row[-1]

# Test the function with some example strings
s1 = "a cat!"
s2 = "the cats!"
d = levenshtein_distance(s1, s2)
print("Edit distance is ",d)

s1 = "kitten"
s2 = "sitting"
d = levenshtein_distance(s1, s2)
print("Edit distance is ",d)


