###  Miscellaneous operating system interfaces

#### File open/write/close
```python
f= open(filepath,"w+")
f.write(data.to_string(header = False, index = False))
f.close() 
```

#### Path
```python
import os
os.getcwd() # Get current directory
os.chdir(path) # Change to a new directory
```

#### Combine files in the directory
```python
for file in os.listdir(path):
    df = pd.concat(df, pd.read_excel(file, header=None))
```

### Runtime
#### Warnings
```python
# Ignore warnings
import warnings
warnings.filterwarnings("ignore")
```
#### Print error type
```python
try: ###
except Exception as e: 
    print(e)
```

#### [Traceback](https://www.geeksforgeeks.org/python-traceback/)
```python
import traceback
# print_exc() method
try: ###
except:
    traceback.print_exc()
# print_exception() method
import sys
try: ###
except:
    traceback.print_exception(*sys.exc_info())
```


### List

#### [Sort a list according to the second element in sublist](https://www.geeksforgeeks.org/python-sort-list-according-second-element-sublist/)
```python
a = [[1,2],[2,3],[3,1]]
sorted(a, key=lambda x:x[1], reverse=True) # [[2,3],[1,2],[3,1]]
```

### Bit
#### [Binary equivalent string of a given integer](https://www.programiz.com/python-programming/methods/built-in/bin)
```python
# Int to binary
bin(3) #'0b11'
bin(3)[2:] #'11'

# Binary to int
## Syntax: int(x=0, base=10); 2 for binary
int('11', 2) #3

# Add binary
a = "11"
b = "1"
bin(int(a, 2) + int(b, 2))[2:] #"100"
```

#### [Bitwise Operators](https://wiki.python.org/moin/BitwiseOperators)
```python
# Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.
x << y
# Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.
x >> y
# Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
x & y
# Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.
x | y
# Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.
~ x
# Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.
x ^ y
```
