import webbrowser
import os
term=str(input("Enter what you want to search: "))
tabUrl = "https://www.google.com/search?q="+ term


webbrowser.open(tabUrl)
st= str(input("Enter close to quit"))

if st=='close':
    os.system("taskkill/im chrome.exe")