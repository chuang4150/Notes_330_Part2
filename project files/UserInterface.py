class UserInterface:
    '''
    The user can enter a command, either search, create, edit,
    delete, or quit. If they are searching, they can search by
    mentions (@), topics(#), or references(^). They may also 
    return to the initial menu. The program can be quit at any 
    time.
    '''
        
    
    running = True
    while running:
        userCommand = input("Please enter a command: ")
        if userCommand.lower().startswith("s"):
            searching = True
            while searching:
                searching = False
                searchCommand = input("Please enter something to search for: ")
                if searchCommand.startswith("@"):
                    print("This searches for mentions")
                elif userCommand.startswith("#"):
                    print("This searches for topic")
                elif searchCommand.startswith("^"):
                    print("This searches for references")
                elif userCommand.lower().startswith("q"):
                    quit()
                else:
                    print("Please enter a valid search")
                    searching = True
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
