import os


def rename_files():

    # (1) get files name from a folder
    files_list = os.listdir(r"/Users/charles/Documents/GitHub/Python2-Udacity/Lesson2/prank")
    print(files_list)

    # (2) rename each file in that folder
    saved_path = os.getcwd()
    os.chdir(r"/Users/charles/Documents/GitHub/Python2-Udacity/Lesson2/prank")

    for file_name in files_list:
        new_name = file_name.translate(None, '0123456789')
        os.rename(file_name, new_name)
        print("Old name - " + file_name)
        print("New name - " + new_name)
    os.chdir(saved_path)


rename_files()
