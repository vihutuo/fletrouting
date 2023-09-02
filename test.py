import random
def GetRandomWord(file_name):
    with open(file_name,"r") as f:
        L1=f.read().splitlines()
    return random.choice(L1)
  secret_word = GetRandomWord("7-letter-popular-words.txt")
  print(secret_word)