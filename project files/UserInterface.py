# -*- coding: utf-8 -*-
import os
from note_content import NoteContent
from note_group import NoteGroup

class UserInterface:
    '''
    The user can enter a command, either search, create, edit,
    delete, view, or quit. If they are searching, they can search
    by mentions and topics. The program can be quit at any time.
    '''
    save_path = os.path.join(os.getcwd(),'note_library')

    notes=[]
    folders = []
    for root, dirs, files in os.walk(save_path, topdown = False):
        for name in files:
            if name.endswith(".txt"):
                note = open(os.path.join(root, name), "r")
                body = note.read()
                note.close()
                notes.append(NoteContent(name[:-4], body))
        for name in dirs:
            folders.append(name)

    compilation=NoteGroup(notes)

    running = True
    while running:
        userCommand = input("\ns: search\n"
                            "t: topological sort\n"
                            "n: navigate files\n"
                            "c: create note\n"
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

        #navigation
        elif userCommand.lower().startswith("n"):
            nav = True
            print("Available folders:")
            for folder in folders: print(folder)
            folder = input("\nEnter folder name: ")
            print("Notes in " + folder + ":")
            available_notes = []
            curr_folder = os.path.join(save_path, folder)
            for item in os.listdir(curr_folder):
                if item.endswith(".txt"):
                    available_notes.append(item[:-4])
            for note in available_notes: print(note)
            while nav:
                nav_com = input("v: view\n"
                                "e: edit\n"
                                "d: delete\n"
                                "m: move\n"
                                "r: return to main menu\n"
                                "Please enter a command: ")
                #view note
                if nav_com.lower().startswith("v"):
                    #TODO: add support for navigating references
                    note = input("Enter name of note to view: ")
                    if note in available_notes:
                        print("\nBody:")
                        print(compilation.with_id(note).body)
                    else: print("\nNote does not exist")
                #edit note
                elif nav_com.lower().startswith("e"):
                    fileName = input("What is the name of the note you would like to edit? ")
                    f = open(os.path.join(curr_folder, fileName) + '.txt', 'a')
                    change = input("Add your changes:")
                    f.write('\n' + change)
                    f.close()
                    print("\nNote Saved")
                    compilation.edit_note(NoteContent(fileName, compilation.with_id(fileName).body + " " + change))
                #delete note
                elif nav_com.lower().startswith("d"):
                    delete_note = input ("Enter the title of the note you would like to remove: ")
                    os.remove(os.path.join(curr_folder, delete_note + ".txt"))
                    print("\nNote Deleted")
                    compilation.delete_note(compilation.with_id(delete_note))
                #move note
                elif nav_com.lower().startswith("m"):
                    note = input("Enter note to move: ")
                    note_folder = "default"
                    new_folder = input("Enter folder to place note. If folder doesn't exist,\n"
                                       "it will be created. Press enter for default folder: ")
                    if new_folder != "": note_folder = new_folder
                    note_path = os.path.join(save_path, note_folder)
                    if os.path.exists(note_path) == False:
                        os.mkdir(note_path)
                        folders.append(new_folder)
                        print("New folder created")
                    os.rename(os.path.join(curr_folder, note + ".txt"),
                              os.path.join(note_path, note + ".txt"))
                elif nav_com.lower().startswith("r"):
                    nav = False
                elif nav_com.lower().startswith("q"):
                    nav = False
                    running = False
        #create note
        elif userCommand.lower().startswith("c"):
            note_folder = "default"

            folder_name = input("Enter name of folder to save new note in. If folder name doesn't\n"
                                "currently exist, it will be created. Press enter for default: ")
            if folder_name != "": note_folder = folder_name
            note_path = os.path.join(save_path, note_folder)
            if os.path.exists(note_path) == False:
                os.mkdir(note_path)
                folders.append(folder_name)
                print("New folder created")
            
            name_of_file = ""
            not_valid = name_of_file == "" or name_of_file in compilation.ids()
            while not_valid:
                name_of_file = input("What is the name of the note: ")
                not_valid = name_of_file == "" or name_of_file in compilation.ids()
                if not_valid:
                    print("Please enter a unique name for this note")
            completeName = os.path.join(note_path, name_of_file+".txt")
            file1 = open(completeName, "w")
            toFile = input("Beginning of your note: ")
            file1.write(toFile)
            file1.close()
            print("\nNote Created")
            compilation.add_note(NoteContent(name_of_file, toFile))
        #quit
        elif userCommand.lower().startswith("q"):
            running = False
        else:
            print("Please enter a valid command")
    quit()
