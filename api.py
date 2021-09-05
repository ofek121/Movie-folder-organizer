import os
import requests
import json
from pathlib import Path
import shutil

path ='..\movies'
unarranged_movie_path=os.path.join(path,'Unarranged movies')
arranged_movie_path=os.path.join(path,'Arranged movies')
API_KEY ='k_d8n17mxo'


def get_movie_info(moive_folder:str):
            movie_name= moive_folder.split('(')[0][:-1]
            movie_year= moive_folder.split('(')[1].split(')')[0]
            return movie_name, movie_year


def get_movie_id(movie_name,movie_year):
    
    url = f'https://imdb-api.com/en/API/SearchMovie/{API_KEY}/{movie_name}'

    response = requests.request("GET", url)
    
    results = json.loads(response.text)['results']
    
    if(results[0]['description'].split('(')[1].split(')')[0] == movie_year): 
        return results[0]['id']
    else:
        print(results[0])
        raise Exception('error in api.py line 26')


def get_movie_gener(movie_id):

    url = f'https://imdb-api.com/en/API/Title/{API_KEY}/{movie_id}'
    headers = {'accept': 'text/plain'}

    response = requests.request("GET", url, headers=headers)

    genre = json.loads(response.text)['genres'].split(',')[0]
    return genre    


def order_by_alphabet(path):
    ganer_folder_list = os.listdir(path)
    movie_list = []
    for ganer_folder in ganer_folder_list:
        ganer_folder_path=os.path.join(path,ganer_folder)
        letter_folder_list=os.listdir(ganer_folder_path)
        for letter_folder in letter_folder_list:
            letter_folder_path=os.path.join(ganer_folder_path,letter_folder)
            if(len(letter_folder)>1):
                folderToMove=os.path.join(ganer_folder_path,letter_folder[0])
                shutil.move(letter_folder_path, folderToMove)
            else:
                new_folder_Path=os.path.join(ganer_folder_path,letter_folder)
                letter_folder_list=os.listdir(new_folder_Path)
                for letter_folder in letter_folder_list:
                    movie_list.append(letter_folder)
    return movie_list



def write_to_movie_list(movie_list):
    with open('./movie_list.txt','r+') as file:
        file.write('\n'.join(movie_list))
    
    return


def main():
    Unarranged_Movie_Folder_list = os.listdir(unarranged_movie_path)
    if(len(Unarranged_Movie_Folder_list)>0):
        for movie_folder_name in Unarranged_Movie_Folder_list:

            movie_name,movie_year = get_movie_info(movie_folder_name)
            movie_id = get_movie_id(movie_name,movie_year)
            movie_gener = get_movie_gener(movie_id)

            gener_path = os.path.join(arranged_movie_path,movie_gener)
            Path(gener_path).mkdir(parents=True, exist_ok=True)

            movie_path = os.path.join(unarranged_movie_path,movie_folder_name)
            shutil.move(movie_path, gener_path) 
    movie_list = order_by_alphabet(arranged_movie_path)
    write_to_movie_list(movie_list)

if __name__ == '__main__':
    main()