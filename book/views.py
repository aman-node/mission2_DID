from unicodedata import name
from urllib import response
from django.shortcuts import render
import requests
import html_to_json
from bs4 import BeautifulSoup
def index(request):
    r = requests.get('https://library.uos.ac.kr/statistics/popularloanList')
 
# Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')
    
    s = soup.find_all('td', class_='title',)
    final_list=[]
    
    for i in s:
        new_lists = []
        lines = str(i.find_all('a')[0])
        # print(type(lines))
        list1 = {}
        link = lines.split("\"")[1]
        title = lines.split(">")[1].split("<")[0]
        list1['link']=link
        list1['title']=title
        new_lists.append(list1)
        print(len(new_lists))
        for i in new_lists:
            url="https://library.uos.ac.kr"+str(i['link'])
            # print(url)    
            html = requests.get(url).text
            # uid = '000000621316'
            isbn = html.split('var isbn="')[1].split('";')[0]
            sysdiv = html.split('var sysdiv = "')[1].split('";')[0]
            controlNo = html.split('var controlno = "')[1].split('";')[0]
            # print(isbn)
            data = {}
            data['title'] = i['title']
            try:
                json_form = requests.post('https://library.uos.ac.kr/openapi/thumbnail', data={'isbn': isbn, 'sysdiv': sysdiv, 'ctrl': controlNo,"detail":"DETAILS"}).json()

                data['sysDiv'] = sysdiv
                data['isbn'] = isbn
                data['image'] = json_form
                
                # final_list.append(data)
                # print(data)
            except:
                nocover_image={'smallUrl':'https://library.uos.ac.kr/image/ko/solution/local/noCoverImg.jpg'}
                data['image']=nocover_image
            final_list.append(data)
    print(final_list)
    return render(request,'data.html', {'final_list':final_list})


