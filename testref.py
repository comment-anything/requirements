import re
import time


s = """-- Terms

- Application Domain

The specific environment in which the product is to operate. [1]

Can be an organization, a department within an organization, or a single workspace. [2]




-- References

[1] Schach, Stephen R., Object-Oriented and Classical Software Engineering, 8th edition.

[2] Züllighoven, Heinz, Object-Oriented Construction Handbook, Chapter 6.3, 2005. https://www.sciencedirect.com/topics/computer-science/application-domain

"""

class Reference:
    def __init__(self, reftext):
        self.reftext = reftext


class Term:
    def __init__(self, name, definition_array):
        self.name = name
        self.definition = definition_array

def parse_terms_txt(s):
    """
    Parses a terms.txt file.

    Returns two dictionaries, one of references, with the local number as the key and string as a value
    And one of terms, with the term as a key and a list as a value.
    """
    lines = re.split("\n", s)
    references = {}
    terms = {}
    adding_to = "terms"
    current_term = None
    current_term_text = []
    for line in lines:
        # dont worry about empty lines
        if len(line) == 0 or re.match("^\s*$", line):
            continue
        is_term_delimiter = re.search("\s*--\s*Terms\s*", line)
        # finding a line like "-- Terms" sets the parser to term reading mode
        if is_term_delimiter:
            adding_to = "terms"
            continue
        is_references_delimiter = re.search("\s*--\s*Ref\w*\s*", line)
        # finding a line like "-- References " sets the parser to reference reading mode
        if is_references_delimiter:
            adding_to = "references"
            # if we just switched from terms to references, save the last term.
            if current_term:
                terms[current_term] = current_term_text
                current_term_text = []
                current_term = None
            continue
        # if we didn't find a new section delimiter then we parse according to the current reading mode
        if adding_to == "terms":
            match = re.match("\s*-\s*\w*", line)
            # finding a line like "- <name>" indicates its time to start reading data for term "name"
            if match:
                # if we were already reading a term, save that term
                if current_term:
                    terms[current_term] = current_term_text
                current_term = re.sub("\s*-\s*", "", line)
                current_term_text = []
                continue
            else:
            # if we didnt find a new term than this line belongs to the last term

                current_term_text += extract_citations(line)
                continue
        if adding_to == "references":
            # references are all on one line, we just need to extract the number and the text data from it
            matches = re.search("\s*\[(\d)\]\s*-*\s*(\w.*)", line)    
            if matches:
                if len(matches.groups()) >= 2:
                    n = int(matches.group(1))
                    txt = matches.group(2)
                    references[n] = txt
                    continue
            else:
                # skip an invalid reference
                continue

    return (references, terms)



def extract_citations(ts):
    """
    Takes a string that may contain interpolated cites in the format 
    
    'sometext [1]'
    
    Returns an array of those strings and numbers parsed as integers.

    ['sometext', 1]
    """
    parts = []
    while len(ts) > 0:
        # match any character up until "[" is found
        match = re.match("([^[]*)", ts)
        if match and len(match.group()) > 0:
            sent = match.group()
            parts.append(sent)
            ts = ts[len(sent):]
            continue
        # match e.g. [1] [ 2 ] [   3 ] etc. Extract the number part only
        match = re.search("\s*\[\s*(\d+)\s*\]\s*", ts) 
        if match:
            # remove e.g. [1] [ 2  ] etc. from the front of the string
            ts = re.sub("^\s*\[\s*\d+\s*\]\s*", "", ts)
            n = match.group(1)
            parts.append(int(n))
    return parts

print(parse_terms_txt(s))