class UserInterface:
    #directory = "File path"
    #reader = "Note reader"
    #checker = "regex checker"
        
    running = True
        
    #mentionPattern = "regex code for finding mentions"
    #keywordPattern = "regex code for finding keywords"
    #referencePattern = "regex code for finding references"
        
    while running:
        userCommand = input("Please enter a command")
        if userCommand.lower().startswith("s"):    
            searching = True
            searchCommand = input("Please enter something to search for")
            while searching:
                if searchCommand.startswith("@"):
                    print("This searches for mentions")
                elif userCommand.startswith("#"):
                    print("This searches for keywords")
                elif searchCommand.startswith("^"):
                    print("This searches for references")
                elif searchCommand.lower().startswith("r"):
                    searching = False
                elif userCommand.lower().startswith("q"):
                    quit()
                else:
                    print("Please enter a valid search")
        elif userCommand.lower().startswith("c"):
            creating = True
            while creating:
                print("This will be where code goes to create files")
                creating = False
        elif userCommand.lower().startswith("e"):
            editing = True
            while editing:
                print("This will be where code goes to edit files")
                editing = False
        elif userCommand.lower().startswith("d"):
            deleting = True
            while deleting:
                print("This will be where the code goes to delete files")
                deleting = False
        elif userCommand.lower().startswith("q"):
            quit()   
        else:
            print("Please enter a valid command")
