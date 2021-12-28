#Made by Lincoln#6812 aka github.com/FM9442
# Version 0.4
import time, os, sys, lxml, requests, json, duckduckgo_search
from serpapi import GoogleSearch
from duckduckpy import query
from selenium import webdriver
from urllib.parse import urlencode, urlunparse
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from colorama import init
from colorama import Fore, Back, Style
init()

print(Fore.LIGHTRED_EX + "Bienvenue sur Finder V-Nitro!")
print(Fore.WHITE + "https://github.com/FM9442/FinderV-Pro")
print(Fore.BLUE + "Discord : Lincoln#6812")
print(Style.RESET_ALL)
time.sleep(1)
print("")
input("Press Enter to launch Finder V-Nitro...")
os.system("cls")
print("Launched!")
time.sleep(1)
os.system("cls")

Lastname=input(Fore.MAGENTA + "Nom de famille précis : ")
City=input(Fore.MAGENTA + "Ville : ")
print(Style.RESET_ALL)

# Performing google search using Python code
version = ("0.4")
class Gsearch_python:
   def __init__(self,name_search):
      self.name = name_search
   def Gsearch(self):
      count = 0
      try :
         from googlesearch import search
      except ImportError:
         print("No Module named 'google' Found, Please try again")
      for i in search(query=self.name,tld='fr',lang='fr',num=10,stop=3,pause=2):
         count += 1
         print (count)
         print(i + '\n')
print(Fore.BLUE + "V-Nitro " + version + " running on ",sys.version)
print(Style.RESET_ALL)

print(Fore.BLUE + "G" + Fore.RED + "o" + Fore.YELLOW + "o" + Fore.BLUE + "g" + Fore.GREEN + "l" + Fore.RED + "e")
print(Style.RESET_ALL)
if __name__=='__main__':
   gs = Gsearch_python(Lastname + City)
   gs.Gsearch()

time.sleep(2)
print(Fore.CYAN + "Bing")
print("Non disponible")
#Using Bing
#query=Lastname + City
#url = urlunparse(("https", "www.duckduckgo.com", "/", "", urlencode({"q": query}), ""))
#custom_user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
#req = Request(url, headers={"User-Agent": custom_user_agent})
#page = urlopen(req)
# Further code I've left unmodified
#soup = BeautifulSoup(page.read())
#links = soup.findAll("a")
#for link in links:
#    print(link["href"])
print(Style.RESET_ALL)

time.sleep(2)
print(Fore.CYAN + "Yahoo")
print("Non disponible")

time.sleep(2)
print(Fore.CYAN + "DuckDuckGo")
print("Non disponible")
print("")

anwser=input(Fore.MAGENTA + "Refaire une recherche Y/N : ")
yesanwser="Y"
noanwser="N"
os.system("cls")

while anwser == yesanwser:
    print(Fore.BLUE + "V-Nitro " + version + " running on ",sys.version)

    time.sleep(1.5)
    Lastname=input(Fore.MAGENTA + "Nom de famille précis : ")
    City=input(Fore.MAGENTA + "Ville : ")
    if __name__=='__main__':
        gs = Gsearch_python(Lastname + City)
        gs.Gsearch()
    
    anwser=input("Refaire une recherche Y/N : ")
print(Style.RESET_ALL)
os.system("cls")
print("Bye!")
