import os
from platform import python_version


def decoding():

    print "*********************************"
    print 'Python', python_version()
    print "Initiate decoding program"
    ch = '*'

    ini_count = 1
    while ini_count <11:
        sec_count = 1
        while sec_count <= ini_count:
            print ch,
            sec_count = sec_count + 1
        print ""
        ini_count = ini_count + 1

    current_dir = os.getcwd() + "/secret message"
    files_list = os.listdir(current_dir)
    saved_path = os.getcwd()
    os.chdir(current_dir)

    for file_name in files_list:
        new_name = file_name.translate(None, '0123456789~!@#$%^&*()_+-=')
        os.rename(file_name, new_name)
    os.chdir(saved_path)

    print "Decoding",
    count = 1
    while count < 54:
        print ".",
        count = count + 1
    print ""
    print "Decode complete!!!"
    print "*********************************"


decoding()
