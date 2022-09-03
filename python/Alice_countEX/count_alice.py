
with open("alice.txt","r") as file:
    for w in file:
     words= w.split();                     #full list with the duplicated words in the files    
     dic= dict.fromkeys(set(words),0);     # getting unique words and saving as a pair with initial value 0. dic={word:0}


#looping in the words and encrease the count num in the set list.
for word in words:
  dic[word]= dic[word] +1;
 

print(max(dic,key=dic.get),max(dic.values()));








