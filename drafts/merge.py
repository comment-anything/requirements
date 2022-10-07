import re
import os 
import argparse
import sys

class ParseDirectory:
    def __init__(self):
        self.sections = []
        self.references = []
        self.terms = {}
        path = os.path.dirname(os.path.realpath(__file__))
        self.path = path
        for a_directory in os.listdir(path):
            dir_path = os.path.join(path, a_directory)
            if os.path.isdir(dir_path):
                content_path = os.path.join(dir_path, "current.md")
                content_data = ""
                try:

                    with open(content_path, "r") as file_object:
                        content_data = file_object.read()
                except:
                    print("content data not read from " + content_path)
                    content_data = ""
                
                terms_path = os.path.join(dir_path, "terms.txt")
                terms_data = ""
                try:
                    with open(terms_path, "r") as file_object:
                        terms_data = file_object.read()
                except:
                    print("terms data not read from " + terms_path)
                    terms_data = ""

                s = Section(a_directory, content_data, terms_data)
                self.sections.append(s)        

        self.merge_references()
        self.merge_terms()

    def merge_references(self):
        self.references = []
        for section in self.sections:
            for key in section.references.keys():
                ref = section.references[key]
                ref.num = len(self.references) + 1
                self.references.append(ref)

    def merge_terms(self):
        self.terms = {}
        for section in self.sections:
            for key in section.terms.keys():
                term_data = section.terms[key]
                if key in self.terms:
                    existing = self.terms[key]
                    existing.append("\n\n")
                    existing + term_data
                else:
                    self.terms[key] = term_data
        for key in self.terms.keys():
            t = Term(key, self.terms[key])
            self.terms[key] = t
        self.terms = self.alphabetical_terms()

    def alphabetical_terms(self):
        order = list(self.terms.keys())
        order.sort()
        as_list = []
        for key in order:
            as_list.append(self.terms[key])
        return as_list

    def as_markdown(self):
        output = ""
        written_main_sections = set()
        for a_sections in self.sections:
            if a_sections.main_section not in written_main_sections:
                output += "\n# " + a_sections.main_section + "\n\n"
                written_main_sections.add(a_sections.main_section)
            output += a_sections.markdown()
            if a_sections.is_terms:
                for term in self.terms:
                    output += term.md()
            elif a_sections.is_references:
                for reference in self.references:
                    output += reference.mdRef()
        return output

    # TODO: Add a try-except?
    def write_file(self, filename):
        fpath = os.path.join(self.path, filename)
        # try:
        with open(fpath + ".md", "w") as outfile:
            outfile.write(self.as_markdown())
            print("Wrote to " +fpath)
        # except Exception as e:
        #     print("Error writing file: ", e.with_traceback(None))

class Reference:
    def __init__(self, num, reftext):
        self.num = num
        self.reftext = reftext

    def mdCite(self):
        return " [" + str(self.num) + "] "
    
    def mdRef(self):
        return "\n\n [" + str(self.num) + "] - " + self.reftext


class Term:
    def __init__(self, name, definition_array):
        self.name = name
        self.definition = definition_array

    def md(self):
        s = "\n\n**" + self.name + "**\n\n"
        for part in self.definition:
            if type(part) == str:
                s += part
            elif type(part) == Reference:
                s += part.mdCite()
        return s

class Section:

    def __init__(self, folder_name, content, references_data):
        self.is_references = False
        self.is_terms = False
        self.extract_sections(folder_name)
        self.text = self.extract_citations(content)
        self.references, self.terms = self.extract_terms_and_references(references_data)
        self.link_references()

    # takes the folder name and extracts the main and sub section.
    def extract_sections(self, s):
        s = re.sub("\d\d\s-\s", "", s)
        s = re.sub("\s-\s\d\d\s", "", s)
        parts = re.split("\s-\s", s)
        self.main_section = parts[0]
        if len(parts) <= 0 or len(parts) > 2:
            raise "Badly formatted folder: " + s
        elif len(parts) < 2:
            self.is_main_section = True
            self.sub_section = ""
        else:
            self.is_main_section = False
            self.sub_section = parts[1]

    def extract_terms_and_references(self, s):
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
                        terms[current_term.strip()] = current_term_text
                    current_term = re.sub("\s*-\s*", "", line)
                    current_term_text = []
                    continue
                else:
                # if we didnt find a new term than this line belongs to the last term

                    current_term_text += self.extract_citations(line)
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

    # returns Section data in markdown format
    def markdown(self):
        s = ""
        if self.is_main_section == False:
            s += "\n## " + self.sub_section + "\n\n"
        for piece in self.text:
            if type(piece) == str:
                s += piece
            elif type(piece) == Reference:
                s += piece.mdCite()
        return s


    # for debug purposes. Works with print(section)
    def __str__(self):
        s = ""
        suffix = ""
        if self.is_main_section:
            s += "<< Section (Main) >> : "
        else:
            s += "<< Section >> : "
            suffix += " - " + self.sub_section
        s += self.main_section
        return s + suffix

    def __repr__(self):
        s = "< Section: " + self.main_section
        if not self.is_main_section:
            s += " :: " + self.sub_section
        return s + " >"

    def extract_citations(self, ts):
        """
        Takes a string that may contain interpolated cites in the format 
        
        'sometext [1]'
        
        Returns an array of those strings and numbers parsed as integers.

        ['sometext', 1]
        """
        parts = []
        has_template = re.search("\s*\{\{\s*(\w*)\s*\}\}\s*", ts)
        if has_template:
            found = has_template.groups()[0]
            if found.lower() == "terms":
                self.is_terms = True
            elif found.lower() == "references":
                self.is_references = True
            ts = re.sub("^\s*\{\{\s*\w*\s*\}\}\s*","", ts)
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


    def link_references(self):
        for ref_num in self.references.keys():
            ref_text = self.references[ref_num]
            ref_ob = Reference(ref_num, ref_text)
            self.references[ref_num] = ref_ob
        for term_name in self.terms.keys():
            term_text_data = self.terms[term_name]
            tt_with_refs = []
            for part in term_text_data:
                if type(part) == int:
                    tt_with_refs.append(self.references[part])
                else:
                    tt_with_refs.append(part)
            self.terms[term_name] = tt_with_refs
        txt_with_refs = []
        for part in self.text:
            if type(part) == int:
                txt_with_refs.append(self.references[part])
            else:
                txt_with_refs.append(part)
        self.text = txt_with_refs
        


d = ParseDirectory()

parser = argparse.ArgumentParser(description="merge.py: A script to merge the contents of the folders and produce one file.")

parser.add_argument("--out", nargs="?", help="Output to a file.")

args = parser.parse_args(sys.argv[1:])
if args.out:
    d.write_file(args.out)
else:
    print(parser.print_help())