import requests
from bs4 import BeautifulSoup

user_input = input("Enter a link from where you want to parse data from: ")

data = requests.get(user_input)
# print(data.content) #parses the HTML

soup = BeautifulSoup(data.content, features = "html.parser" )

print(soup.html.head.title)  # parses the title
