# Notes_330_Part2
 Our note-taking project has the ability to report notes that have selected mentions and topics. It can also sort the notes in topological order. The current version of the project has five updated features.

### Features of NoteTaking System:
  
     #1- Create and Save new notes:	
	      User is able to create a new file by selecting the apprpriate option. Before the note is created, the user is able to save it in a particular folder. 
            
     #2- Edit and view existing notes, including deleting of notes:
          By selecting the appropraite option for the prompt, the user is able to add to an existing note. The user is also able to view the particular note or a list of existing notes in a folder.         
            
     #3- Navigating the system by using Refernces:
          User is able to use references in notes to navigate between notes, that is, accessing refernced notes directly. The system displays the list of all the referenced notes and gives the user the option to quickly view one of them. For example, if note A references B and C, these notes can be accessed directly from note A with no need to navigate through all other notes.             
          
     #4- Interactive UserInterface:
          The system has an interactive User-Interface to access the feaatures on the notetaking system. The user has more control over what is reported to them.
	  
     #5- Organizing Files/notes:
         The system is able to organize text files into smaller sub-folders based on the user's choosing. User can save a note in a desired folder or can move a file to another folder as well. A default folder is also provided.

### Note format:
The body of each note may contain three special characteristics:

	#1- mentions: beginning with the @ symbol, these are useful for mentioning other users
	#2- topics: beginning with the # symbol, these allow topics to be discovered quickly and efficiently
	#3- references: use the ^ symbol before the name of an existing note to link it to your new note


### User instructions:
Run "UserInterface.py" and follow the prompts.

 User have to run "UserInterface.py" file which can be found under "project files" folder. The intial prompt will ask the user to enter the following letters (not case-sensitive) to do the desired tasks:

		s: search topics and mentions		
		t: topological sort
		n: navigate files
		c: create note
		q: quit program

  #Details:
   	
	s: search topics and mentions

	  When user enter "s" letter, the system prompts user to enter one of the two search options:

			t: to search notes with respect to selected topic
			m: to search notes with respect to selected mentions

 then user will be asked to enter a mention or topic to search. The system will display the list of all notes that has certain mention or topic. 

	t: topological sort

	   This selection will sort all the notes and display the sorted list of all notes. 

	n: navigate files

	   It will display the list of existing folders. The system will prompt user to eneter the name of the folder that he wants to navigate into. The system will return the list of all existing notes in that selected folder, and prompt the user with a list of tasks that user wants to choose in that folder. The list of prompt is as follows:

			current folder: ----
			l: list notes
			v: view note
			e: edit note
			d: delete note
			m: move note
			r: remove current folder
			b: back to main folder	
		
		l:
	 	  displays the list of all existing notes in current folder
		v:
	 	  By entering the name of the note. This option will allow user to view the contents of selected note.
		e:
		  It allows user manipulate the contents of that note, like adding or deleting the data. 
		d:
	 	  User can delete a note by enetering the title of the note.
		m:
		  It prompts user to enter the name of the note that he needs to move. Then it will ask the user to enter the folder to place the note, If the folder doesn't exit, it will create a new folder of the entered name.
 
		  Note:::: If user wants to move the note in default folder, he can just press "enter" to move note in default folder. 

		r:
	 	  By selecting this option, user will be prompted to confirm his selection by entering "y" for yes or "N" for no. When the selected has been removed, the existing notes in that folder will be copied to "default" folder. So, the user will only loose the selected folder he wanted to remove, not its content.		
	   	   Note:::: User cannot delete "default" folder. 
		b: 
	 	  This option will take the user back to the main menu.

The rest of the main menu options are as follows:
	
	c: create note
	   This option will prompt the user to enter a folder name in which he wants to save new note. The user will be asked to type the name of the note, and then user will be prompted to typpe the body of the note. (see Note Format)

	    Note:::: if the folder name doesnot currently exits, it will create a new folder of that new name. To save new note in 'default' folder, user can press 'enter' without typing any folder name. 	

	q: quite program
	   Enter 'q' letter to exit the userInterface. 



NOTE:::: All the folders and notes will be created and/or manipulated in the "note_library" folder of our note-taking project.
		 
  
	
	
