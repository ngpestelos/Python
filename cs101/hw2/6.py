# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def _find_last(search, target):
  index = 0
  while True:
    if search == "":
      break
    
    new_index = search.find(target, index)
    print "found? ", index
    
    if new_index == -1:
      break
    else:
      index = new_index
    
    search = search[index+1:]
    print "new search ", search
  
  return index

def find_last(search, target):
  last = -1
  while True:
    pos = search.find(target, last + 1)
    if pos == -1:
      break
    last = pos
  
  return last

print find_last('aa', 'a')

#print find_last('aaaa', 'a')
#>>> 3

#print find_last('aaaaa', 'aa')
#>>> 3

#print find_last('aaaa', 'b')
#>>> -1

#print find_last("111111111", "1")
#>>> 8

print find_last("222222222", "")
#>>> 9

print find_last("", "3")
#>>> -1

print find_last("", "")
#>>> 0
