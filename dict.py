import json
from difflib import get_close_matches

data = json.load(open('dictionary.json'))



def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) >0:
        yn= input("Do you mean the word %s, Y for yes and N for no. "% get_close_matches(w,data.keys())[0])
        yn = yn.lower()
        
        if yn == 'y':
            return data[get_close_matches(w,data.keys())[0]]
        elif yn== 'n':
            return "The word doesnt exist"
        else:
            return "sorry, I didnt understand"
    else:
        return "The word doesnt exist"
    
    
    
word=input("Enter the word ")
ans=translate(word)



if type(ans)== list:
    for item in ans:
        print(item)
else:
    print(ans)
    
input("enter to exit")
