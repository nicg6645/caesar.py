def wordrando(): 
  f = open('1-1000.txt', 'r') #https://gist.github.com/deekayen/4148741
  wordlist = f.read()
  f.close()
  return wordlist.split() #https://www.reddit.com/r/Python/comments/3aajez/how_to_convert_a_txt_file_into_a_list/
import random
def cesarshift(x):
  foo = wordrando()
  tootlist = []
  weewee = (random.choice(foo))
  woowoo = list(weewee)
  for entry in woowoo:
    a = (ord(entry) -97) + x
    b = chr(a + 97)
    tootlist.append(b)
  return ''.join(tootlist)

