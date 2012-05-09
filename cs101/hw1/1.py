doc = """<html xmlns="http://www.w3.org/1999/xhtml"><br/> <head><br/><title>Udacity</title> <br/></head><br/><br/><body> <br/><h1>Udacity</h1><br/><br/> <p><b>Udacity</b> is a private institution of <a href="http://www.wikipedia.org/wiki/Higher_education"> higher education founded by</a> <a href="http://www.wikipedia.org/wiki/Sebastian_Thrun">Sebastian Thrun</a>, David Stavens, and Mike Sokolsky with the goal to provide university-level education that is "both high quality and low cost".<br/>It is the outgrowth of a free computer science class offered in 2011 through Stanford University. Currently, Udacity is working on its second course on building a search engine. Udacity was announced at the 2012 <a href="http://www.wikipedia.org/wiki/Digital_Life_Design">Digital Life Design</a> conference.</p><br/></body><br/></html>"""


link = doc.find("<a href=")
start_quote = doc.find('"', link)
end_quote = doc.find('"', start_quote+1)
print doc[start_quote+1:end_quote]

link = doc.find("<a href=", end_quote)
start_quote = doc.find('"', link)
end_quote = doc.find('"', start_quote+1)
print doc[start_quote+1:end_quote]

link = doc.find("<a href=", end_quote)
start_quote = doc.find('"', link)
end_quote = doc.find('"', start_quote+1)
print doc[start_quote+1:end_quote]

link = doc.find("<a href=", end_quote)
start_quote = doc.find('"', link)
end_quote = doc.find('"', start_quote+1)
print doc[start_quote+1:end_quote]
