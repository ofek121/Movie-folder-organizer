import os
import shutil

moviePath='.\movies'

def orderFolder(path):
    listdir = os.listdir(path)
    movie_list = []
    for folder in listdir:
        folderPath=os.path.join(path,folder)
        listSubDir=os.listdir(folderPath)
        for subFolder in listSubDir:
            subfolderPath=os.path.join(folderPath,subFolder)
            if(len(subFolder)>1):
                print(subFolder)
                folderToMove=os.path.join(folderPath,subFolder[0])
                shutil.move(subfolderPath, folderToMove)
            else:
                new_folder_Path=os.path.join(folderPath,subFolder)
                listSubDir=os.listdir(new_folder_Path)
                for subFolder in listSubDir:
                    movie_list.append(subFolder)
    return movie_list


if __name__ == '__main__':
    orderFolder(moviePath)
