#given a sentence, rearrange the 
#words in the sentence in order of length

def arrangeWords(text):
  text = text[0].lower() + text[1:]
  words = text.split()
  words = sorted(words,key= lambda x: len(x))
  ret = ' '.join(words)
  return ret[0].upper() + ret[1:]



t = "To be or not to be"
print(arrangeWords(t))