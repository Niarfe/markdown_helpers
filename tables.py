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



    lengths = None 
    rows = [] 
    for line in tlines:
        line = line.strip().strip('|')
        words = [word.strip() for word in line.split('|')]
        if not lengths: lengths = [len(word) for word in words]
        _lengths = [len(word) for word in words]
        _update_lengths(_lengths)
        rows.append(words)

    return [_repack_as_line(row) for row in rows] 


#========== TESTING ==========

sample = """| Heading 1|Heading 2| Heading 3|
| :-- | ------ | ---: |
| blah | bab |baaa       aaab|
|a|b|c|"""

def test_smoke():
    result = clean_table(sample)
    assert result[0] == "| Heading 1 | Heading 2 | Heading 3       |"
    assert result[1] == "| :--       | ------    | ---:            |"
    assert result[2] == "| blah      | bab       | baaa       aaab |"
    assert result[3] == "| a         | b         | c               |"




if __name__=="__main__":
    import sys
    assert len(sys.argv) == 2, "Pass in a file with markdown table, no empty lines"

    lines = open(sys.argv[1], 'r').readlines()
    for row in clean_table(lines):
        print(row)



