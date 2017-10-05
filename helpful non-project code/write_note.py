import os
import pickle
#An extremely simple and bare minimum for writing and reading in user created notes
#using python and the pickle library.

#make sure to create a folder named note_library in the same directory so the program can actually save the notes

class Note(object):
    def __init__ (self, pbody, author, title):
        self.body = pbody
        self.author = author
        self.title = title

cwd = os.getcwd()
note_directory_name = '/note_library/'

def writing():
    def write_note(note):
        filename = cwd + note_directory_name + note.title + '.pickle'
        with open (filename, 'wb') as f:
             pickle.dump(note, f, pickle.HIGHEST_PROTOCOL)

    mynote = Note(title = input('Title:'),
    author = input('Author:'),
    pbody = input('Body:'))

    write_note(mynote)


def reading():
    reading_notes = input('input the title of the note you would like to open')

    def read_note (note):
        filename = cwd + note_directory_name + note + '.pickle'
        with open (filename, 'rb') as f:
            return (pickle.load(f))

    (read_note(reading_notes))
    

print("Welcome to our note taking system")

right = input("enter write or read:")
if right == 'write':
    writing()
elif right == 'read':
    reading()
