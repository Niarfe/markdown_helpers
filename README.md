# markdown_helpers
Reformatting functions to help me maintain/export/import markdown in code files

## Install it
`pip install git+http://github.com/Niarfe/markdown_helpers@main`

## Example script and sample table are in `example` folder. The table contains markdown table sloppily formatted.
```python
import sys
from markdown_helpers import clean_table                                                                                
assert len(sys.argv) == 2, "Usage: bin/format.py <path to table file to clean>"                                         

file_path = sys.argv[1]

lines = open(file_path, 'r').readlines()                                                                              
                                                                                                                        
for line in clean_table(lines):                                                                                         
    print(line) 
```


