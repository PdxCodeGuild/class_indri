import requests

headers={
    'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'
}


#------------Part 1-----------------------------------
# responses=requests.get('https://favqs.com/api/qotd')
# json_resp=responses.json()
# quote=json_resp['quote']['body']
# author=json_resp['quote']['author']

# print(f'Quate: {quote} Author:{author}')




#-----------------Part 2-------------------

keyword=input('What keyword are looking for?')
page=1
URL_Site=f'https://favqs.com/api/quotes?page={page}&filter={keyword}'
keyword_responses=requests.get(URL_Site, headers=headers)

json_page=keyword_responses.json()


mypage = 1

def print_quotes(json_obj):
    bullet=0
    quote=0
    for quote in range(len(json_obj['quotes'])-1):
        bullet+=1
        quote+=1
        quote_text =json_obj['quotes'][quote]['body']
        print(f'{bullet}. {quote_text}')
        
print_quotes(json_page)

while json_page['last_page']==False:
    page_change=input(f'You are on page {page}. Do you want to go to the next page? (Y/N) ').upper()
    if page_change=='Y':
        page+=1
        keyword_responses=requests.get(f'https://favqs.com/api/quotes?page={page}&filter={keyword}', headers=headers)
        json_page=keyword_responses.json()
        print_quotes(json_page)
    else:
        print('Thank you for visiting')
        break

else:
    print('You are on the last page')


