# zync

zync is a utility tool for python operations.

[![zync-ci](https://github.com/tjbredemeyer/zync/actions/workflows/ci.yml/badge.svg)](https://github.com/tjbredemeyer/zync/actions/workflows/ci.yml)

## INSTALLATION

```bash
pip install zyncify
```

## Usage

### 1. IMPORT

```python
from zync import *
```

### 2. FUNCTIONS

#### logger

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

#### bugger

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

#### wegger

wegger takes in a string and logs it with an ERROR level.  

```python
from zync import wegger

# logging a string ERROR
wegger("error message")

# logging a variable ERROR
message = "error message"
wegger(message)

###
# returns: ERROR debug message
```  

#### Slugger  

Slugger converts a string to slug while maintaining capitalization.  

```python
from zync import Slugger

# Slugging a string with Caps
Slugger("Test String")

# Slugging a variable with caps
string = "Test String"
Slugger(string)

###
# returns: Test-String
```  
  
#### slugger  

slugger converts a string to a slug with no capitalization.

```python
from zync import slugger

# Slugging a string without Caps
slugger("Test String")

# Slugging a variable without caps
string = "Test String"
slugger(string)

###
# returns: test-string
```  

### 3. TAIL LOG FILE

```bash
tail -f ./.zync.log
```

## Author

TJ Bredemeyer  
twitter: @tjbredemeyer
