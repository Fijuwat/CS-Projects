# CS 303E Quiz 5D
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1: Going Up
def goingUp(matrix, row, col):
    
    highest = []
    highest.append(matrix[row][col])
    highest.append(matrix[row-1][col-1])
    highest.append(matrix[row][col-1])
    highest.append(matrix[row+1][col-1])
    highest.append(matrix[row-1][col])
    highest.append(matrix[row+1][col])
    highest.append(matrix[row-1][col+1])
    highest.append(matrix[row][col+1])
    highest.append(matrix[row+1][col+1])
    going = max(highest)
    return going
    pass



# Problem 2: First Punctuation Locations
def firstPunctuationLocations(strings):
    # replace pass with your solution to problem 2
    final_result = {}
    def test(word):
      result = False
      sentence = ".!?"
      for x in sentence:
          if word == x:
              result = True
      return result

    for item in strings:
        count = 0
        for word in item:
            if test(word):
                break
            count += 1
        final_result[item] = count

    return final_result
    
    



if __name__ == '__main__':
    # uncomment the following lines to run the given test cases
    # note that the output will look slightly different
    # due to how the expected output is formatted

    # grid = [[3939, 4344, 4070, 3218, 2743, 1775, 1973, 1835, 2953], [3825, 3563, 3909, 3592, 2607, 2832, 2837, 2606, 1685], [2960, 2826, 3226, 2169, 3334, 2305, 2901, 1462, 1595], [2829, 2352, 1744, 3672, 3008, 2729, 3001, 1495, 1443], [2496, 3275, 2349, 1844, 1678, 2042, 1880, 2357, 1036], [3188, 2562, 1941, 1583, 1041, 1436, 2329, 1224, 1186], [1605, 2401, 3070, 1968, 2075, 2428, 1844, 2449, 2391], [1097, 2133, 1301, 2780, 1425, 1654, 2227, 1398, 2307], [1001, 2277, 1144, 1333, 1765, 1499, 1498, 897, 1705]]
    # print(goingUp(grid, 1, 2))
    # print(goingUp(grid, 7, 1))
    # grid2 = [[900, 987, 878, 1500], [891, 1000, 771, 1200], [221, 347, 486, 1001]]
    # print(goingUp(grid2, 1, 1))

    # print(firstPunctuationLocations({'!!!!!', 'is for me?', 'interesting... very interesting'}))
    # print(firstPunctuationLocations({'Panic! At The Disco', '5! = 120', '3.14'}))
    # print(firstPunctuationLocations(set()))

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT