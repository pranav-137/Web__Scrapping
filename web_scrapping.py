import requests
from bs4 import BeautifulSoup
url=input("enter website")
r=requests.get(url)
htmlcontent=r.content
#print(htmlcontent)
soup=BeautifulSoup(htmlcontent,'html.parser')
print(soup.prettify)
'''
                                         Commonly used type of objects in website
                                          1> tag
                                          2> navigable string
                                          3> beautifulsoup object
                                          4> comment
'''
title=soup.title
print(type(soup))#for type of soup
print(type(title))
print(type(title.string))
paras=soup.find_all('p') #get all paras
print(paras)
print(soup.find('p'))
print(soup.find('p')['class'])#get class of any element in html page
print(soup.find_all("p",class_="lead"))#find all element in html page
print(soup.find('p').get_text())#get the text from the tags/soup
print(soup.get_text())#get the text of whole html page

anchors=soup.find_all('a') #get all anchors
all_links=set()
print(anchors)

#get all the links on the page
for link in anchors:
    if (link.get('href')!='#'): 
        linktext = url+link.get('href')  
        all_links.add(link) 
        print(linktext)

#              for tree traversal        
ul = soup.find("ul")#getting the children from tree
for i in ul.children:
	print(i)

print("parent class")#getting parent from tree
#https://github.com/pranav-137
ul = soup.find("ul")
print(ul.parent)

#to get parent of parent, write:
print("parent of parent")
print(ul.parent.parent)

#to get next sibling and then next sibling 
ul = soup.find(id="li")
#for next sibling
for j in ul.next_siblings:
    print(j)
print("previous sibling")
# for previous sibling
print(ul.previous_sibling.previous_sibling)