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

    #TODO: view body of a note, include option to view references

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
                elif searchCommand.lower().startswith("q"):
                    quit()
                else:
                    print("Please enter a valid search")
                    searching = True
        elif userCommand.lower().startswith("t"):
            for note in compilation.topo_sort(): print(note)
        elif userCommand.lower().startswith("c"):
            save_path = os.path.join(os.path.expanduser('~'),'Documents')
            name_of_file = input("What is the name of the note: ")
            completeName = os.path.join(save_path, name_of_file+".txt")
            file1 = open(completeName, "w")
            toFile = input("Beginning of your note: ")
            file1.write(toFile)
            file1.close()
            #compilation.add_note
        elif userCommand.lower().startswith("e"):
            save_path = os.path.join(os.path.expanduser('~'),'Documents')
            files=get_file_names()
            print("Current saved notes:", files)
            fileName = input("What is the name of the note you would like to edit?")
            f = open(save_path + '/' + fileName + '.txt','a')
            change = input("Add your changes:")
            f.write('\n' + change)
            f.close()
            #compilation.edit_note
        elif userCommand.lower().startswith("d"):
            delete_note = input ("Enter the title of the note you would like to remove: ")
            dn = '/' + delete_note + '.txt'
            note_directory_name = os.path.join(os.path.expanduser('~'),'Documents')
            os.remove(note_directory_name + dn)
            #compilation.delete_note
        elif userCommand.lower().startswith("q"):
            quit()
        else:
            print("Please enter a valid command")
