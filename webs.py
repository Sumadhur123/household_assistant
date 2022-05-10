import requests, webbrowser

from bs4 import BeautifulSoup

user_input =input("Enter something to search: ")
print("googling")

google_search = requests.get("https://www.google.com/search?q=" + user_input)

soup= BeautifulSoup(google_search.text, 'html.parser')
print(soup.prettify())

#result = list(soup.find_all('div class= BNeawe tAd8D AP7Wnd'))
#print(soup.div('X7NTVe'))

#print(result)
#print(soup.select('.BNeawe deIvCb AP7Wnd div'))