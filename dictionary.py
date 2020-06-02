'''
Question:
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count = dict()
words = list()
for lines in handle:
    line = lines.rstrip()
    if line.startswith('From:'):
        wordss = line.split()
        words.append(wordss[1])
        #print('words',words)
#print('words',words)
for word in words:
    count[word] = count.get(word,0)+1
#print(count)
        
bigword = None
bigcount = None
for key,value in count.items():
    if bigcount is None or value > bigcount:
        bigword = key
        bigcount = value
        
print(bigword,bigcount)
