import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/<name>")
def hello_name(name):
    return "Hello {}!".format(name)

#Actual app
@app.route("/webhook", methods=['POST'])
def webhook():
	character = "Jon Snow"
	
	character = character.title()
	if " " in character:
		character = character.replace(" ", "_")
	print(character)

	content = urlopen('http://gameofthrones.wikia.com/wiki/' + character).read()
	soup = BeautifulSoup(content, "html.parser")

	isPage = soup.find('aside', attrs={"class":"portable-infobox"})

	isNoArticle = soup.find('div', attrs={"class":"noarticletext"})

	if isNoArticle != None:
		newLink = soup.find('a', attrs={"href"})
		print(newLink)

	if isPage == None:
		print("Name is unclear, try again")
	else:
		status =soup.find(text='Alive')

		if status == None:
			print(character + " is dead")
		else:
			print(character + " is alive")
			
	return

			
if __name__ == "__main__":
    app.run()