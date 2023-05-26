# markdown_helpers
Reformatting functions to help me maintain/export/import markdown in code files

## Install it
`pip install git+http://github.com/Niarfe/markdown_helpers@main`

## Example script and sample table are in `example` folder. The table contains markdown table sloppily formatted.
```python
from markdown_helpers import clean_table

lines = open('example/arrow_table.md', 'r').readlines()

for line in clean_table(lines):
    print(line)
```


