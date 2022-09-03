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
    
    # s = soup.find_all('div', class_='listTable').find_all('tbody').find_all('tr')
    s = soup.find('div', class_='listTable').find('tbody').find_all('tr')
    new_list=[]
    for i in s:
        title = i.find("td", class_="title").find("a").text
        author = i.find_all("td", class_="author")[0].text
        link = i.find("td", class_="title").find("a").get('href')
        # print(link)
        # print("title="+title,"author="+author,"link"+link)
        url="https://library.uos.ac.kr"+str(link)
            # print(url)    
        html = requests.get(url).text
        # uid = '000000621316'
        isbn = html.split('var isbn="')[1].split('";')[0]
        sysdiv = html.split('var sysdiv = "')[1].split('";')[0]
        controlNo = html.split('var controlno = "')[1].split('";')[0]
        # print(isbn)
        try:
            data = {'isbn': isbn, 'sysdiv': sysdiv, 'ctrl': controlNo,"detail":"DETAILS"}
            print(data)
            json_form = requests.post('https://library.uos.ac.kr/openapi/thumbnail', data=data).json()
            images = json_form["smallUrl"]
        except Exception as e:
            images='https://library.uos.ac.kr/image/ko/solution/local/noCoverImg.jpg'
        var={"smallUrl":images}
        new_list.append({"title":title,"author":author,"image":var})
    print(new_list)
    return render(request,'data.html', {'final_list':new_list})


