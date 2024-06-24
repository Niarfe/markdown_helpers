"""
Reformat a Markdown table by spacing out the |s according to the largest string per column

function: clean_table(<list<str>>:tlines)

Input:
    tlines    list of strings, where each string is a markdown table row.  Header is treated
                  just like all other rows

Output:
    <list<str>>    a list of strings, where each string is a reformatted row for the Markdown table
"""


def clean_table(tlines):
    if isinstance(tlines, str):
        tlines = tlines.split('\n')
    assert isinstance(tlines, list), "Expecting a list of strings"
    def _update_lengths(_lengths):
        for idx in range(len(_lengths)):
            lengths[idx] = _lengths[idx] if _lengths[idx] > lengths[idx] else lengths[idx]
    def _repack_as_line(_row):
        _words = [word.ljust(lengths[idx]) for idx, word in enumerate(_row)]
        return '| '+' | '.join(_words)+' |'

    escaped_bar = '\\|'
    temp_replace = '$$'

    lengths = None 
    rows = [] 
    for line in tlines:
        line = line.strip().strip('|')
        replace = False
        if escaped_bar in line:
            line = line.replace(escaped_bar, temp_replace)
            replace = True

        if replace:
            words = [word.strip().replace(temp_replace, escaped_bar) for word in line.split('|')]
        else:
            words = [word.strip() for word in line.split('|')]

        if not lengths: lengths = [len(word) for word in words]
        _lengths = [len(word) for word in words]
        _update_lengths(_lengths)
        rows.append(words)

    return [_repack_as_line(row) for row in rows] 


#========== TESTING ==========

table = """| Heading 1|Heading 2| Heading 3|
| :-- | ------ | ---: |
| blah | bab |baaa       aaab|
|a|b|c|"""

def test_smoke():
    result = clean_table(table)
    assert result[0] == "| Heading 1 | Heading 2 | Heading 3       |"
    assert result[1] == "| :--       | ------    | ---:            |"
    assert result[2] == "| blah      | bab       | baaa       aaab |"
    assert result[3] == "| a         | b         | c               |"


table_escaped = """| Heading 1|Heading 2| Heading 3|
| :-- | ------ | ---: |
| bl\|ah | bab |baaa       aaab|
|a|b|c|"""

def test_escaped_bar():
    result = clean_table(table_escaped)
    assert result[0] == "| Heading 1 | Heading 2 | Heading 3       |"
    assert result[1] == "| :--       | ------    | ---:            |"
    assert result[2] == "| bl\|ah    | bab       | baaa       aaab |"
    assert result[3] == "| a         | b         | c               |"


#######################################################################################################################
#    Load a table
#######################################################################################################################

def load_table(fpath):
    lines = open(fpath, 'r').readlines()
    lines = [line.strip() for line in lines]
    return convert_lines_to_rows(lines)

def convert_lines_to_rows(lines):
    keys = lines[0].strip('|').split('|')
    keys = [key.strip() for key in keys]
    n_keys = len(keys)
    rows = []
    for line in lines[2:]:
        cells = line.strip('|').split('|')
        cells = [cell.strip() for cell in cells]
        assert len(cells) == n_keys, f"Expected same length of cells as keys, but got keys={n_keys}, cells={len(cells)} for line = {line}"
        row = {k:v for k,v in zip(keys, cells)}
        rows.append(row)

    return rows

# TEST
def test_convert_lines_to_rows():
    lines = [
            "A|B|C|",
            "|--|--|--|",
            "|one|two|three|",
            "|uno|dos|tres|"
            ]
    rows = [
            {"A":"one", "B":"two", "C":"three"},
            {"A":"uno", "B":"dos", "C":"tres"}
            ]
    assert rows == convert_lines_to_rows(lines)
            
def test_convert_lines_to_rows_spaces():
    lines = [
            "| A   | B   | C     |",
            "| --  |--   | --    |",
            "| one | two | three |",
            "| uno | dos | tres  |"
            ]
    rows = [
            {"A":"one", "B":"two", "C":"three"},
            {"A":"uno", "B":"dos", "C":"tres"}
            ]
    assert rows == convert_lines_to_rows(lines)

def test_load_table_little_vendue():
    got_rows = load_table('markdown_helpers/little_vendue.md')
    exp_rows = [
            {'WORD': 'abasourdi', 'MEANING': 'stunned'},
            {'WORD': 'accablé', 'MEANING': 'overwhelm'},
            ]

    assert exp_rows == got_rows

if __name__=="__main__":
    import sys
    assert len(sys.argv) == 2, "Pass in a file with markdown table, no empty lines"

    lines = open(sys.argv[1], 'r').readlines()
    for row in clean_table(lines):
        print(row)



