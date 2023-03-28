import re
def sentence_count(Fstr):
    f = open(Fstr,"r")
    wholeFile = f.read()
    f.close()
    delimiters = ".","!","?","..."
    regexPattern = '|'.join(map(re.escape, delimiters))
    wordArray = re.split(regexPattern,wholeFile)
    return len(wordArray)
