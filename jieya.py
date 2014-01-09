__author__ = 'jiahuixing'
import os
import sys

def tar():
    print("----begin work----")
    command_tar = "tar xvf "
    length = len(sys.argv)
    print("len(sys.argv)=%d"%length)
    if length < 2:
        print("pls add the file to tar.")
    else:
        file_name = sys.argv[1]
        command_tar = "%s%s" % (command_tar, file_name)
        print("command_tar=%s"%command_tar)
        os.system(command_tar)
        command_rm = "rm -r " + file_name
        print("command_rm=%s"%command_rm)
        os.system(command_rm)
        folder_name = walk(os.getcwd())
        folder_name += "/flash_all_except_storage.sh"
        command_chmod = "chmod a+x "
        command_chmod += folder_name
        print("command_chmod=%s"%command_chmod)
        os.system(command_chmod)

    print("----work done----")

def walk(path):
    for item in os.listdir(path):
        sub_path = os.path.join(path,item)
        if os.path.isdir(sub_path):
            if "images" in sub_path:
                return sub_path


if __name__=='__main__':
    tar()