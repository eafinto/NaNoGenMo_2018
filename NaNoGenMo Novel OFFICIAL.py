import random 
import markovify 
import dominate 
from dominate.tags import *
import pdfkit

novel = ' '

with open("Stories.txt") as f:
    text = f.read()

text_model = markovify.Text(text)

for i in range(3500):
    novel += str(text_model.make_sentence()) 
    
    r = random.randint(0,100)
    
    if (r < 36):
        novel += "\n\n"

sectioned = novel.split("\n\n")
doc = dominate.document(title='A Fantastical Dream')
with doc.head: 
    style("body {background-color: white; color: black; font-size: 25pt}")
    
with doc: 
    
    h1("A Fantastical Dream")
    p("A NaNoGenMo Novel by Elizabeth Finto")
    
    for s in sectioned: 
        p(s)

pdfkit.from_string(str(doc.render()), 'a_fantastical_dream.pdf')

print(doc)

len(novel.split(" "))
