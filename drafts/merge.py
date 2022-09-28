import os
import re
import sys
import argparse



class Section:


    
    def AllWithMarkdown(sections_array):
        written_main_sections = set()
        output = ""
        for a_sections in sections_array:
            if a_sections.main_section not in written_main_sections:
                output += "# " + a_sections.main_section + "\n\n"
                written_main_sections.add(a_sections.main_section)
            output += a_sections.markdown()
        return output


    def __init__(self, folder_name, content, references_data):
        self.extract_sections(folder_name)
        self.text = content
        self.references = references_data

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

    # returns Section data in markdown format
    def markdown(self):
        s = ""
        if self.is_main_section == False:
            s += "\n## " + self.sub_section + "\n\n"
        s += self.text 
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

# script runs in of src, not pwd.
path = os.path.dirname(os.path.realpath(__file__))

sections = []

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
        sections.append(s)


parser = argparse.ArgumentParser(description="merge.py: A script to merge the contents of the folders and produce one file.")

parser.add_argument("--out", nargs="?", help="Output to a file.")
parser.add_argument("--p", help="Print the output markdown to the console.", action="count")

args = parser.parse_args(sys.argv[1:])
if args.out:
    filename = args.out
    fpath = os.path.join(path, filename)
    try:
        with open(fpath + ".md", "w") as outfile:
             outfile.write(Section.AllWithMarkdown(sections))
             print("Wrote to " +fpath)
    except:
        print("Error writing file.")
elif 'print' in args:
    print(Section.AllWithMarkdown(sections))
else:
    print(parser.print_help())
    
    

