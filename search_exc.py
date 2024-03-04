import re 

s = 'GeeksforGeeks: A computer science portal for geeks'

match = re.search(r'portal', s) #r'portal' -> Search pattern, s -> string

print('Start Index:', match.start()) 
print('End Index:', match.end()) 
