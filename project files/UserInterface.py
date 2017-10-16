# -*- coding: utf-8 -*-
import os
import re
import glob
import os.path
from note_content import NoteContent
from note_group import NoteGroup

class find(object):
    def __init__ (self, body, author, title):
        self.body = body
        self.author = author
        self.title = title

    def find_identifiers(self, symbol):
        if(symbol!="^"):
            pattern = r'[' + symbol + ']\S*'
        else:
            pattern= r'[' '\^' + ']\S*'
        return re.findall(pattern, self.body)

    def find_urls(self):
        return re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', self.body)

class UserInterface:
    '''
    The user can enter a command, either search, create, edit,
    delete, or quit. If they are searching, they can search by
    mentions (@), topics(#), or references(^). They may also
    return to the initial menu. The program can be quit at any
    time.
    '''
def get_file_names(): #lists all text files in a directory
    save_path = os.path.join(os.path.expanduser('~'),'Documents')
    os.chdir(save_path)
    list_of_files = glob.glob('*.txt')
    return (list_of_files)

files=get_file_names()
print("Files that will be analyzed: ",files)

# symbol = input('Enter the symbol you are searching for:')
notes=[]
for fileName in files:
    file = open(fileName,"r" )
    read_file = file.read()
    file.close()
    notes.append(NoteContent(fileName))
    searched_note = find( body = read_file
                         ,author = ""
                         ,title = fileName + '.note')
    mentions=find.find_identifiers(searched_note, '@')
    topics=find.find_identifiers(searched_note, '#')
    references=find.find_identifiers(searched_note,'^')
    unique_id=find.find_identifiers(searched_note,'!')
    urls=find.find_urls(searched_note)
    if len(unique_id) > 0:
        notes[len(notes)-1].create_id(unique_id[0][1:])
        print ("\nUnique Note ID:" + unique_id[0][1:])


    notes[len(notes)-1].add_mentions(*[e[1:] for e in mentions])
    notes[len(notes)-1].add_topics(*[e[1:] for e in topics])
    notes[len(notes)-1].add_references(*[e[1:] for e in references])
    notes[len(notes)-1].add_urls(*urls)

    compilation=NoteGroup(notes)

    running = True
    while running:
        userCommand = input("Please enter a command: ")
        if userCommand.lower().startswith("s"):
            searching = True
            while searching:
                searching = False
                searchCommand = input("Please enter something to search for: ")
                if searchCommand.startswith("m"):
                    mention = input("Enter mention to search for: ")
                    for note in compilation.with_mention(mention): print(note)
                elif searchCommand.startswith("t"):
                    topic = input("Enter topic to search for: ")
                    for note in compilation.with_topic(topic): print(note)
                elif searchCommand.startswith("r"):
                    print("This searches for references")
                elif searchCommand.lower().startswith("q"):
                    quit()
                else:
                    print("Please enter a valid search")
                    searching = True
        elif userCommand.lower().startswith("t"):
            print("This will be where topological sort goes")
        elif userCommand.lower().startswith("c"):
            print("This will be where code goes to create files")
        elif userCommand.lower().startswith("e"):
            print("This will be where code goes to edit files")
        elif userCommand.lower().startswith("d"):
            print("This will be where the code goes to delete files")
        elif userCommand.lower().startswith("q"):
            quit()
        else:
            print("Please enter a valid command")
