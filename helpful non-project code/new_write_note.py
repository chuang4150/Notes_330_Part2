import os.path
import os
import glob




def write():
    save_path = os.path.join(os.path.expanduser('~'),'Documents')
    name_of_file = input("What is the name of the note: ")
    completeName = os.path.join(save_path, name_of_file+".txt")
    file1 = open(completeName, "w")
    toFile = input("Beginning of your note: ")
    file1.write(toFile)
    file1.close()

def read():
    save_path = os.path.join(os.path.expanduser('~'),'Documents')
    fileName = input("What is the name of the note you would like to read? ")
    file = open(save_path + '/' + fileName + '.txt',"r" )
    read_file = file.read()
    file.close()
    print (read_file)

def delete():
    delete_note = input ("Enter the title of the note you would like to remove: ")
    dn = '/' + delete_note + '.txt'
    note_directory_name = os.path.join(os.path.expanduser('~'),'Documents')
    os.remove(note_directory_name + dn)

# def edit():
#     save_path = os.path.join(os.path.expanduser('~'),'Documents')
#     fileName = input("What is the name of the note you would like to read?")
#     file = open(save_path + '/' + fileName + '.txt',"r" )
#     read_file = file.read()
#     TODO:how to edit the actual textfile

print ("Welcome to our note taking system!")
sys = input("/nWould you like to Create, read, or delete a note? ")
if sys == "create":
    write()
elif sys == "read":
    read()
elif sys == "delete":
    delete()
