# -*- coding: utf-8 -*-
import os
import re
import glob
import os.path
from note_content import NoteContent
from note_group import NoteGroup

class UserInterface:
    '''
    The user can enter a command, either search, create, edit,
    delete, or quit. If they are searching, they can search by
    mentions and topics. The program can be quit at any
    time.
    '''
    save_path = os.path.join(os.getcwd(),'note_library')
    
    def get_file_names(directory): #lists all text files in a directory
        os.chdir(directory)
        list_of_files = glob.glob('*.txt')
        return (list_of_files)

    files=get_file_names(save_path) #will need to walk through all folders

    def create_note_content(name, body):

        def find_identifiers(symbol):
            if(symbol!="^"):
                pattern = r'[' + symbol + ']\S*'
            else:
                pattern= r'[' '\^' + ']\S*'
            return re.findall(pattern, body)

        def find_urls():
            return re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', body)

        
        note = NoteContent(name)
        #searched_note = find(body = body, author = "", title = name + '.note')
        mentions=find_identifiers('@')
        topics=find_identifiers('#')
        references=find_identifiers('^')
        urls = find_urls()

        note.add_mentions(*[e[1:] for e in mentions])
        note.add_topics(*[e[1:] for e in topics])
        note.add_references(*[e[1:] for e in references])
        note.add_urls(*urls)

        return note
    
    notes=[]
    for fileName in files:
        file = open(fileName,"r" )
        read_file = file.read()
        file.close()
        notes.append(create_note_content(fileName[:-4], read_file))

    compilation=NoteGroup(notes)

    #TODO: view body of a note, include option to view references
    #TODO: organize into folders

    running = True
    while running:
        userCommand = input("\ns: search\n"
                            "t: topological sort\n"
                            "c: create note\n"
                            "e: edit note\n"
                            "d: delete note\n"
                            "q: quit program\n"
                            "Please enter a command: ")
        #searching
        if userCommand.lower().startswith("s"):
            searching = True
            while searching:
                searching = False
                searchCommand = input("Please enter topic (t) or mention (m): ")
                if searchCommand.startswith("m"):
                    mention = input("Enter mention to search for: ")
                    print("\nResults:")
                    for note in compilation.with_mention(mention): print(note)
                elif searchCommand.startswith("t"):
                    topic = input("Enter topic to search for: ")
                    print("\nResults:")
                    for note in compilation.with_topic(topic): print(note)
                elif searchCommand.lower().startswith("q"):
                    running = False
                else:
                    print("Please enter a valid search")
                    searching = True
                    
        #topological sort
        elif userCommand.lower().startswith("t"):
            print("\nResults:")
            for note in compilation.topo_sort(): print(note)

        #create note
        elif userCommand.lower().startswith("c"):
            name_of_file = ""
            not_valid = name_of_file == "" or name_of_file in compilation.ids()
            while not_valid:
                name_of_file = input("What is the name of the note: ")
                not_valid = name_of_file == "" or name_of_file in compilation.ids()
                if not_valid:
                    print("Please enter a unique name for this note")
            completeName = os.path.join(save_path, name_of_file+".txt")
            file1 = open(completeName, "w")
            toFile = input("Beginning of your note: ")
            file1.write(toFile)
            file1.close()
            print("\nNote Created")
            compilation.add_note(create_note_content(name_of_file, toFile))

        #edit note
        elif userCommand.lower().startswith("e"):
            files=get_file_names(save_path)
            print("Current saved notes:", files)
            fileName = input("What is the name of the note you would like to edit?")
            f = open(save_path + '/' + fileName + '.txt','a')
            change = input("Add your changes:")
            f.write('\n' + change)
            f.close()
            print("\nNote Saved")
            #compilation.edit_note(create_note_content(fileName, this currently poses an issue...
        #delete note
        elif userCommand.lower().startswith("d"):
            delete_note = input ("Enter the title of the note you would like to remove: ")
            dn = '/' + delete_note + '.txt'
            os.remove(save_path + dn)
            print("\nNote Deleted")
            compilation.delete_note(compilation.with_id(delete_note))

        #quit
        elif userCommand.lower().startswith("q"):
            running = False
        else:
            print("Please enter a valid command")
    quit()
