import os
import shutil
from file_practice import prettify_list_dir

FOLDER_NAME = 'spam_folder'
FILE_NAME = 'spam.txt'
COPY_NAME = 'renamed_spam.txt'
COPY_FOLDER = 'spam_folder_copy'
FOLDERS = [FOLDER_NAME, COPY_FOLDER]

print(' Note on folder delete '.center(70, "-"))
print("'shutil.rmtree(<dir_name>)' removes non-empty directories")
print("'os.rmdir(<dir_name>)' removes empty directories")
prettify_list_dir()
for folder in FOLDERS:
    if os.path.exists(os.path.join(os.getcwd(), folder)):
        print("\n>>> deleting pre-existing '{}' folder with its content...".format(folder))
        shutil.rmtree(folder)

print(">>> creating '{}' folder...".format(FOLDER_NAME))
os.mkdir("./{}".format(FOLDER_NAME))

if os.path.exists(os.path.join(os.getcwd(), FILE_NAME)):
    print("\n>>> deleting pre-existing '{}' file...".format(FILE_NAME))
    os.remove(FILE_NAME)

print(">>> creating '{}' file...".format(FILE_NAME))

with open(FILE_NAME, 'w') as f:
    f.write("This is not important =(")
print(">>> copying {} to {}".format(FILE_NAME, FOLDER_NAME))
shutil.copy(FILE_NAME, FOLDER_NAME)
print(">>> creating a copy {} of {} '...".format(COPY_NAME, FILE_NAME))
shutil.copy(FILE_NAME, COPY_NAME)
print(">>> moving {} to {}...".format(COPY_NAME, FOLDER_NAME))
shutil.move(COPY_NAME, FOLDER_NAME)
print(">>> renaming {} to 'spam_copy.txt'...".format(COPY_NAME))
shutil.move(
    os.path.join(FOLDER_NAME, COPY_NAME),
    os.path.join(FOLDER_NAME, "spam_copy.txt")
)
print(">>> copying folder {} with its content...".format(FOLDER_NAME))
shutil.copytree(FOLDER_NAME, COPY_FOLDER)

print(">>> walking through current folder content...")
for folder_name, sub_folders, filenames in os.walk(os.getcwd()):
    print("Folder: {}\nSubfolders list: {} \nfiles: {}".format(
        folder_name,
        str(sub_folders),
        str(filenames)
    ))
    print()

