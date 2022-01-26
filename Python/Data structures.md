## Notes on Data Structure 

[Real Python - Common Python Data Structures](https://realpython.com/python-data-structures/)


### String

#### [isalnum()](https://www.programiz.com/python-programming/methods/string/isalnum)
##### Ex. (Leetcode 125) Valid Palindrome
```python
def isPalindrome(self, s: str) -> bool:
    # convert all uppercase letters into lowercase letters and remove all non-alphanumeric characters
    s = [i.lower() for i in s if i.isalnum()]
    return s == s[::-1]
```



### List

#### List comprehension
```python
# 243. Shortest Word Distance
def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
    # Get all indexes of word occurrences
    w1_ind = [i for i in range(len(wordsDict)) if wordsDict[i] == word1] 
    w2_ind = [i for i in range(len(wordsDict)) if wordsDict[i] == word2]

    # Find closest indexes as the shortest distance
    return min([abs(i1-i2) for i1 in w1_ind for i2 in w2_ind])
```

##### [Use a dictionary to count the items in a list](https://stackoverflow.com/questions/3496518/using-a-dictionary-to-count-the-items-in-a-list)
```python
# Use Counter
from collections import Counter
Counter(s)

# Use .get method in dictionary
counts = dict()
for i in s:
  counts[i] = counts.get(i, 0) + 1
  
# Use count method in list
{x : s.count(x) for x in set(s)}

# For loop
counts = {}
for i in s:
    if i not in s:
        s[i] = 1
     else:
        s[i] += 1
```


##### [Sort a list according to the second element in sublist](https://www.geeksforgeeks.org/python-sort-list-according-second-element-sublist/)
```python
a = [[1,2],[2,3],[3,1]]
sorted(a, key=lambda x: x[1], reverse=True) # [[2,3],[1,2],[3,1]]
```

##### [Sort a list by multiple attributes](https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes/4233482)
```python
# Use lambda function that returns a tuple
s = sorted(s, key = lambda x: (x[1], x[2]))

# Use itemgetter 
import operator
s = sorted(s, key = operator.itemgetter(1, 2))
s.sort(key = operator.itemgetter(1, 2))
```


##### Remove vowels from a letter
```python
letter = 'abcdEFGH'
''.join([i for i in letter if i.lower() not in 'aeiou']) # 'bcdFGH'
```

### Linked list


### Heap
#### [Binary heap](https://www.geeksforgeeks.org/binary-heap/)


### Stack and Queues

### Maps
