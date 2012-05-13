import urllib

def get_page(url):
    doc = urllib.urlopen(url).read()
    #print doc
    return doc
  
def get_next_target(page):
    start_link = page.find('<a href="')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote
  
def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while len(tocrawl) > 0:
        page = tocrawl.pop()
        if page not in crawled:
            crawled.append(page)
            tocrawl.extend(get_all_links(get_page(page)))
    return crawled
    
print crawl_web('http://www.udacity.com/cs101x/index.html')