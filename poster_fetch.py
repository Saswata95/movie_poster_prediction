import numpy as np
import pandas as pd
import requests

movies = pd.read_csv("./MovieGenre.csv", encoding="ISO-8859-1")

#print(movies.columns)

length = len(movies)
print("Total Number Of Movies:" + str(length))


#try:
#    os.makedirs("/Movie_Posters")
#except OSError:
#    print("Creation of path failed")
#else:
#    print("Folder successfully created!")

for i in range(0, length+1):
    try:
        img_data = requests.get(movies.loc[i]['Poster']).content
    except:
        print('No URL Provided')
    else:
        img_name = './Movie_Posters/' +str(movies.loc[i]['imdbId'])+'.jpg'
        print(str(i)+" "+"Saving Image" + img_name)
        with open(img_name, 'wb') as handler:
            handler.write(img_data)