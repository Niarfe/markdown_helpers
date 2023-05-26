from markdown_helpers import clean_table

lines = open('example/arrow_table.md', 'r').readlines()

for line in clean_table(lines):
    print(line)
