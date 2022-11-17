#Part 1--------------------------------

import requests
header={
'accept': 'application/json'
}

response=requests.get('https://icanhazdadjoke.com/', headers= header)
#response.encoding = 'utf-8'
dict_daddy_joke=response.json()
dad_joke=dict_daddy_joke['joke']
dady_joke=response['joke']
print(dad_joke)

#  Part 2-----------------------------------------------------------------------

param={
 'term' : ''
}

key_value=input('What dady joke do you want to look for?')
param['term']=key_value
search=requests.get('https://icanhazdadjoke.com/search', params=param, headers=header) 
search_json=search.json()


joke_number=0
while True:
    print(search_json['results'][joke_number]['joke'])
    answer=input('Is this the joke that your looking for? (Y/N)').upper()
    if answer=='Y':
        break
    else:
        joke_number+=1
        continue

