import os
#https://docs.python.org/3/library/os.html#os.makedirs
#trying out a few methods that will be useful
#for creating folders for notes

#create directory if it doesn't already exist
new_dir = 'is_this_successful?'
if os.path.exists(new_dir) == False:
    os.mkdir(new_dir)
    print("directory created")

new_dir = 'is_this_successful?/new'
if os.path.exists(new_dir) == False:
    os.mkdir(new_dir)
    print("folder within folder created")

#move test_file.txt into new folders
os.rename('test_file.txt', 'is_this_successful?/new/test_file.txt')
print("test file moved")

#rename a folder
old_name = 'is_this_successful?'
new_name = 'yes'
if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print('renamed')
else:
    print("directory does not exist")

#remove all folders in cwd and bring all files back to top level
cwd = os.getcwd()
for root, dirs, files in os.walk(cwd, topdown = False):
    for name in files:
        os.rename(os.path.join(root, name), os.path.join(cwd, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))
print("directories removed and test file returned to current working directory")
