# -*- coding: utf-8 -*-
import os
import re
import glob
import os.path
from note_content import NoteContent
from note_group import NoteGroup

# TODO: How to deal with duplicate file names

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


def get_file_names(): #lists all text files in a directory
    save_path = os.path.join(os.path.expanduser('~'),'Documents')
    os.chdir(save_path)
    list_of_files = glob.glob('*.txt')
    return (list_of_files)


def search():

    # filename = input('Which .txt file would you like to open?')
    # print (read_file)
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
        # print (mentions)
        # print (references)
        print("Url(s) found:", urls)
        print("Mention(s) found:", mentions)

    compilation=NoteGroup(notes)
    containingMentions=compilation.with_mentions()

    # TODO: Case statement
    print("\nThese are the notes containing mentions: \n")
    # for mention in containingMentions:
    #     print(mention)
    for mention in compilation.mentions:
        # print(mention)

        for note in compilation.with_mention(mention):

            print(note, ':', mention)

    print("\nThese are the notes containing topics: \n")
    for topic in compilation.topics:
        # print (topic)

        for note in compilation.with_topic(topic):

            print (note,':', topic)

    contine_search = input("Would you like to do another task?")
    if contine_search in ('y', 'yes'):
            os.system('clear')
            main()

    else:
            print ('Program terminating')
            os.system('clear')

def main():
    def write():
        save_path = os.path.join(os.path.expanduser('~'),'Documents')
        name_of_file = input("What is the name of the note: ")
        completeName = os.path.join(save_path, name_of_file+".txt")
        file1 = open(completeName, "w")
        toFile = input("Beginning of your note: ")
        file1.write(toFile)
        file1.close()
        contine_search = input("Would you like to do another task?")
        if contine_search in ('y', 'yes'):
                os.system('clear')
                main()

        else:
                print ('Program terminating')
                os.system('clear')

    def read():
        save_path = os.path.join(os.path.expanduser('~'),'Documents')
        files=get_file_names()
        print("Current saved notes:", files)
        fileName = input("What is the name of the note you would like to read?")
        file = open(save_path + '/' + fileName + '.txt',"r" )
        read_file = file.read()
        file.close()
        print (read_file)
        contine_search = input("Would you like to do another task?")
        if contine_search in ('y', 'yes'):
                os.system('clear')
                main()

        else:
                print ('Program terminating')
                os.system('clear')

    def delete():
        delete_note = input ("Enter the title of the note you would like to remove: ")
        dn = '/' + delete_note + '.txt'
        note_directory_name = os.path.join(os.path.expanduser('~'),'Documents')
        os.remove(note_directory_name + dn)
        contine_search = input("Would you like to do another task?")
        if contine_search in ('y', 'yes'):
            os.system('clear')
            main()
        else:
            print ('Program terminating')
            os.system('clear')

    def edit():
        save_path = os.path.join(os.path.expanduser('~'),'Documents')
        files=get_file_names()
        print("Current saved notes:", files)
        fileName = input("What is the name of the note you would like to edit?")
        f = open(save_path + '/' + fileName + '.txt','a')
        change = input("Add your changes:")
        f.write('\n' + change)
        f.close()

    print ("Welcome to our note taking system!")
    sys = input("Would you like to create, read, edit, delete, or search notes? ")
    if sys == "create":
        write()
    elif sys == "read":
        read()
    elif sys == "edit":
        edit()
    elif sys == "delete":
        delete()
    elif sys == 'search':
        search()

main()
