# -*- coding: utf-8 -*-
import os
from note_content import NoteContent
from note_group import NoteGroup

'''
The user can enter a command, either search, topological sort,
navigate, or create. If they are searching, they can search
by mentions and topics. If they are navigating, they can list
notes, view, edit, delete, or move notes contained in a folder,
or remove the folder. The program can be quit at any time.
'''
#path where all notes are saved
save_path = os.path.join(os.getcwd(),'note_library')
default_path = os.path.join(save_path, "default")

#find initial notes and folders in program, initialize NoteGroup
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

def view_note(note):
    #view a note and its references
    #supports navigating through references
    print("\nBody:")
    print(compilation.with_id(note).body + "\n")
    references = compilation.referenced_notes(compilation.with_id(note))
    if len(references) > 0:
        print("References:")
        for reference in references:
            print(reference)
        nav_ref = input("Enter reference to view. To skip viewing references, press enter: ")
        if nav_ref == "":
            print()
        elif compilation.with_id(nav_ref) in references:
            view_note(nav_ref)
        else:
            print("This is not a note referenced by " + note + "\n")

#user interaction
running = True
while running:
    userCommand = input("\ns: search topics and mentions\n"
                        "t: topological sort\n"
                        "n: navigate files\n"
                        "c: create note\n"
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
        
        print("\nAvailable folders:")
        for folder in folders: print(folder)
        folder = ""
        not_valid = folder not in folders
        while not_valid:
            folder = input("\nEnter folder name: ")
            not_valid = folder not in folders
            if not_valid:
                print("Please enter a valid folder name.")

        print("\nNotes in " + folder + ":")
        available_notes = []
        curr_folder = os.path.join(save_path, folder)
        for item in os.listdir(curr_folder):
            if item.endswith(".txt"):
                available_notes.append(item[:-4])
        for note in available_notes: print(note)
        print()
        
        while nav:
            nav_com = input("current folder: " + folder + "\n"
                            "l: list notes\n"
                            "v: view note\n"
                            "e: edit note\n"
                            "d: delete note\n"
                            "m: move note\n"
                            "r: remove current folder\n"
                            "b: back to main menu\n"
                            "Please enter a command: ")
            #list notes
            if nav_com.lower().startswith("l"):
                print("\nNotes in " + folder + ":")
                for note in available_notes: print(note)
                print()
                
            #view note
            elif nav_com.lower().startswith("v"):
                #TODO: add support for navigating references
                note = input("Enter name of note to view: ")
                if note in available_notes:
                    view_note(note)                       
                else: print("\nNote does not exist in this folder.\n")
                
            #edit note
            elif nav_com.lower().startswith("e"):
                fileName = input("What is the name of the note you would like to edit? ")
                if fileName in available_notes:
                    f = open(os.path.join(curr_folder, fileName) + '.txt', 'a')
                    change = input("Add your changes:")
                    f.write('\n' + change)
                    f.close()
                    print("\nChanges Saved\n")
                    compilation.edit_note(NoteContent(fileName, compilation.with_id(fileName).body + " " + change))
                else: print("\nNote does not exist\n")
                
            #delete note
            elif nav_com.lower().startswith("d"):
                delete_note = input ("Enter the title of the note you would like to remove: ")
                if delete_note in available_notes:
                    os.remove(os.path.join(curr_folder, delete_note + ".txt"))
                    print("\nNote Deleted")
                    compilation.delete_note(compilation.with_id(delete_note))
                    available_notes.remove(delete_note)
                else: print("\nNote does not exist\n")
                
            #move note
            elif nav_com.lower().startswith("m"):
                note = input("\nEnter note to move: ")
                if note in available_notes:
                    note_path = default_path
                    new_folder = input("Enter folder to place note. If folder doesn't exist,\n"
                                       "it will be created. Press enter for default folder: ")
                    if new_folder != "": note_path = os.path.join(save_path, new_folder)
                    if os.path.exists(note_path) == False:
                        os.mkdir(note_path)
                        folders.append(new_folder)
                        print("New folder created")
                    os.rename(os.path.join(curr_folder, note + ".txt"),
                              os.path.join(note_path, note + ".txt"))
                    print("Note has been moved.\n")
                    available_notes.remove(note)
                else: print("\nNote does not exist\n")
                
            #remove current folder
            elif nav_com.lower().startswith("r"):
                if curr_folder == default_path:
                    print("\nYou may not remove the default folder.\n")
                else:
                    confirm = input("\nAll notes contained in this folder will be moved to default. Confirm Y or N: ")
                    print()
                    if confirm.lower().startswith("y"):
                        for note in available_notes:
                            os.rename(os.path.join(curr_folder, note + ".txt"),
                                      os.path.join(default_path, note + ".txt"))
                        os.rmdir(curr_folder)
                        folders.remove(folder)
                        nav = False
            elif nav_com.lower().startswith("b"):
                nav = False
            elif nav_com.lower().startswith("q"):
                nav = False
                running = False
            else:
                print("Please enter a valid command")

    #create note
    elif userCommand.lower().startswith("c"):
        note_path = default_path
        folder_name = input("Enter name of folder to save new note in. If folder name doesn't\n"
                            "currently exist, it will be created. Press enter for default: ")
        if folder_name != "": note_path = os.path.join(save_path, folder_name)
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
        toFile = input("Body of your note: ")
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
