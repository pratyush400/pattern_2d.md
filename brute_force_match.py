__author__ = "Jolie, Emma, Pratyush"

def match(pattern, text):
    pattern_row = len(pattern)
    pattern_column = len(pattern[0])
    text_row = len(text)
    text_column = len(text[0])

    if pattern_row > text_row or pattern_column > text_column:
        return False  # pattern can not be larger than text

    ## checking pattern in a row...

    for i in range(text_row - pattern_row + 1):  ##checks max each row ends if remaining text is too short for pattern
        for j in range(text_column - pattern_column + 1):  ##checks max each column
            match_found = True
            ## checks if there is a match starting and i row and j col
            for r in range(pattern_row): # checks the text's rows for pattern
                for c in range(pattern_column):
                    if text[i + r][j + c] != pattern[r][c]:
                        match_found = False
                        break
                if not match_found:
                    break
            if match_found:
                 return i,j
    return None






