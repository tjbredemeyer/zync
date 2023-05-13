# zync

zync is a utility tool for python operations.

## INSTALLATION

```bash
pip install zync
```

## Usage

### 1. IMPORT

```python
from zync import *
```

### 2. FUNCTIONS

#### 1. logger

logger takes in a string and logs it with an INFO level.  

```python
from zync import logger

# logging a string INFO
logger("info message")

# logging a variable INFO
message = "info message"
logger(message)

###
# returns: INFO info message
```  

#### 2. bugger

bugger takes in a string and logs it with a DEBUG level.  

```python
from zync import bugger

# logging a string DEBUG
bugger("debug message")

# logging a variable DEBUG
message = "debug message"
bugger(message)

###
# returns: DEBUG debug message
```  

#### 3. Slugger  

Slugger converts a string to slug while maintaining capitalization.  

```python
from zynce import Slugger

# Slugging a string with Caps
Slugger("Test String")

# Slugging a variable with caps
string = "Test String"
Slugger = (string)

###
# returns: Test-String
```  
  
#### 4. slugger  

slugger converts a string to a slug with no capitalization.

```python
from zynce import Slugger

# Slugging a string without Caps
slugger("Test String")

# Slugging a variable without caps
string = "Test String"
slugger = (string)

###
# returns: test-string
```  

## Author

TJ Bredemeyer  
twitter: @tjbredemeyer
