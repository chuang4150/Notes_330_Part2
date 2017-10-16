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
    delete, view, or quit. If they are searching, they can search
    by mentions and topics. The program can be quit at any time.
    '''
    save_path = os.path.join(os.getcwd(),'note_library')
    
    def get_file_names(directory): #lists all text files in a directory
        os.chdir(directory)
        list_of_files = glob.glob('*.txt')
        return (list_of_files)

    files=get_file_names(save_path) #will need to walk through all folders
    
    notes=[]
    for fileName in files:
        file = open(fileName,"r" )
        read_file = file.read()
        file.close()
        notes.append(NoteContent(fileName[:-4], read_file))

    compilation=NoteGroup(notes)

    #TODO: add support for folder organization

    running = True
    while running:
        userCommand = input("\ns: search\n"
                            "t: topological sort\n"
                            "v: view note\n"
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

        #view note
        #add support for navigating folders
        #add support for references
        elif userCommand.lower().startswith("v"):
            note = input("Enter name of note to view: ")
            if compilation.with_id(note):
                print("\nBody:")
                print(compilation.with_id(note).body)
            else: print("\nNote does not exist")

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
            compilation.add_note(NoteContent(name_of_file, toFile))

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
            compilation.edit_note(NoteContent(fileName, compilation.with_id(fileName).body + " " + change))
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
