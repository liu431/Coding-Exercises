## Notes of Python Operations Functions 

### Time
> "Mysterious thing, Time. Powerful, and when meddled with, dangerous." ― J.K. Rowling

 `time` package
```python
import time
startTime = time.time()
# Process
time.sleep(60) # Delay process
endTime = time.time()
print('Minutes:',round(((endTime - startTime)/60),0))
```
 `datetime` package
```python
from datetime import datetime, timedelta
yesterday = datetime.now() - timedelta(days=1) # Get yesterday's date
# Create a date object
x = datetime(2021, 1, 2)
x2 = datetime(2021, 1, 1)
x > x2 # True
# Format date objects into readable strings
x.strftime("%B") # January
x.strftime("%m") # 01
x.strftime("%Y") # 2021
x.strftime("%d") # 02

# Convert between month name and month number
## Abbreviated month name
month_name = "Jan"
month_number = datetime.strptime(month_name, "%b").month # 1

## Full month names
month_name = "January"
month_number = datetime.strptime(month_name, "%B").month # 1
```

#### Waiting week days
```python
from datetime import datetime
def WeekDays(Days):
    '''Calculate the waiting week days by excluding the weekends'''
    if Days >= 5:
        Days = Days - 2 * (Days // 5)
    else:
        # When time clock starts from late last week or during the weekend
        if Days > datetime.today().weekday():
            if Days >= 2:
                Days -= 2
            else:
                Days = 0
    return Days
WeekDays(1) # Work done by last Sunday -> 0
WeekDays(2) # Work done by last Saturday -> 0
WeekDays(3) # Work done by last Friday -> 1
WeekDays(4) # Work done by last Thursday -> 2
WeekDays(5) # Work done by last Wednesday -> 3
```


### Run .py file
#### Pass argument
```python
import sys
def func(a, b):
    pass

if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    func(a, b)
```


### Keyword
* [Iterables](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Iterables.html): object capable of returning its members one at a time, permitting it to be iterated over in a for-loop
* Generators: functions that return an iterable generator object; contains one or more `yield` statements; generate the values on the fly
* [`yield`](https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do): used like `return`, except the function will return a generator
* `next()`: iterate through the items
* `StopIteration`: raised when there are no values to be returned 

### Path
```python
import os
os.getcwd() # get current directory
os.mkdir(foldername) # create new directory that doesn't exist 
cwd = os.chdir(path) # change to a new directory
os.listdir(cwd) # get the list of all files and directories in the specified directory
```

### File operations
#### File open/write/close
```python
f= open(filepath,"w+")
f.write(data.to_string(header = False, index = False))
f.close() 
```

#### Edit files
```python
a_file = open(filename, "r")
list_of_lines = a_file.readlines()
list_of_lines[2] = "New data" # Edit line data

a_file = open(filename, "w")
a_file.writelines(list_of_lines)
a_file.close()
```

#### Create new line based on file template
```python
with open("existingfile.txt", "r+") as f:
    with open("newfile.txt", "w+") as f2:
        for linects, line in enumerate(f):
            if condition1:
                line = line.replace('X', 'XX')
             else:
                pass
            f2.write(line)
```



#### Combine files in the directory
```python
for file in os.listdir(path):
    df = pd.concat(df, pd.read_excel(file, header=None))
```

### Copy files with [shutil](https://www.geeksforgeeks.org/python-shutil-copy2-method/) and folder with [copy_tree](https://www.kite.com/python/docs/distutils.dir_util.copy_tree)
```python
# Copy folder
from distutils.dir_util import copy_tree
copy_tree(src, des)

# Copy files
import shutil
shutil.copy2(file_copy_from, file_copy_to)
```

### Delete files
```python
os.remove(filepath)
```

### [Subprocess management](https://docs.python.org/3/library/subprocess.html)
* Allow you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes
* Run shell command with Python

```python
import subprocess
process = subprocess.Popen(arg, shell=True)
process.terminate()
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

### Letters
#### [Letters and numbers conversion](https://www.kite.com/python/answers/how-to-convert-letters-to-numbers-in-python)
```python
# Letters -> Numbers
ord('a') - 97 #0
ord('A') - 65 #0
# Numbers -> Letters
chr(97) #'a'
chr(65) #'A'
```


### Bit and Bytes (1 byte = 8 bits)
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

```python
# Int to bytes
## If byteorder is "big", the most significant byte is at the beginning of the byte array
var = 1024.to_bytes(2, byteorder='big')
# Bytes to int
int.from_bytes(var, "big") # 1024
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

### Applications
[pyinstaller](https://pyinstaller.readthedocs.io/en/stable/usage.html): bundle a Python application and all its dependencies into a single package. The user can run the packaged app without installing a Python interpreter or any modules.

```shell
#pip install pyinstaller
cd filepath
pyinstaller --onefile program.py
```

### Process mails
#### [Outlook](https://www.codeforests.com/2020/06/04/python-to-read-email-from-outlook/)
```python
import win32com.client
import os
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
folder = outlook.Folders("MailboxName")
inbox = folder.Folders("Inbox")
messages = inbox.Items
for message in list(messages):
    try:
      print(message.Sender, ',', message.Subject, ',', message.ReceivedTime, message.Body, message.SentOn)
    except:
      pass
```




