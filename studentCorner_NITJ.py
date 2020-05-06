import requests
from bs4 import BeautifulSoup
scwp = requests.get('https://www.nitj.ac.in/#section-2')
soup = BeautifulSoup(scwp.content, 'html.parser')
seplst = soup.get_text('|')
seplst1 = seplst.split('''GIAN|
|
|
|
|
|''')
seplst2 = seplst1[1]
seplst3 = seplst2.split('|\n|\n|\n|\n|\n|\n|')
stc1 = seplst3[1]
stclst = stc1.split('''|
|''')
fir = stclst[0] 
stclst = [i[2:] for i in stclst[1:]]   # ultimate student corner list.(sclst)
stclst.insert(0,fir)
# print(len(stclst))                  #print of stclst
# print(stclst)
prev = 'Notice regarding Registration in Google Classroom | '    #this was on top at the time of app making
new = stclst[0]
if(prev!=new):
    print('You have got a new message on student corner.')
    print(stclst[0])
    prev = seplst[0]
else:
    print('No new information.')    
print('press any key to exit')
exitkey = input()

