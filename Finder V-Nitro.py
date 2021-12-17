# Version 0.2
import time, os, sys


# Performing google search using Python code
version = ("0.2")
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
print("V-Nitro " + version + " running on ",sys.version)
time.sleep(1.5)

Lastname=input("Nom de famille précis : ")
City=input("Ville : ")


if __name__=='__main__':
   gs = Gsearch_python(Lastname + City)
   gs.Gsearch()

anwser=input("Refaire une recherche Y/N : ")
yesanwser="Y"
noanwser="N"
os.system("cls")

while anwser == yesanwser:
    print("V-Nitro " + version + " running on ",sys.version)

    time.sleep(1.5)
    Lastname=input("Nom de famille précis : ")
    City=input("Ville : ")
    if __name__=='__main__':
        gs = Gsearch_python(Lastname + City)
        gs.Gsearch()
    
    anwser=input("Refaire une recherche Y/N : ")

os.system("cls")    
print("Bye!")