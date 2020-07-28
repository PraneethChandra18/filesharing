import os

def show_dir(d_list,path):
    print(str(len(d_list))+" directories of "+os.path.abspath(path))
    print("==========================================================")
    for index,dir in enumerate(d_list):
        print(str(index+1)+")"+dir)
        show(os.path.join(path,dir))

def show_files(f_list,path):
    print(str(len(f_list))+" files of "+os.path.abspath(path))
    print("==========================================================")
    for index,f in enumerate(f_list):
        print(str(index+1)+")"+f)

def show(path="."):
    f_list = []
    d_list = []

    try:
        for f in os.listdir(path):
            if os.path.isfile(os.path.join(path,f)):
                f_list.append(f)
            else:
                if os.path.isdir(os.path.join(path,f)):
                    d_list.append(f)
    except:
        print("Error, once check the path")
        return

    show_files(f_list,path)
    show_dir(d_list,path)

show(",/filesharing/fileshare")
