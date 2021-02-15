import requests
import smtplib
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
prev="Additional Information regarding |Registration of PG Students| in the 2nd Semester | "
new=stclst[0]
#email-automation-starts
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('rishabcandy@gmail.com', 'umarani19')
#---
if(prev!=new):
    print('You have got a new message on student corner.')
    print(stclst[0])
    #prev = seplst[0]
    server.sendmail('rishabcandy@gmail.com', 's.hashwanth531@gmail.com',stclst[0])
    #prev = seplst[0]
else:
    print('No new information.')     
def updateCount():
    x=y='"'
    fin = open('main.py', 'r')
    code = fin.read()
    fin.close()
    second_line = code.split('\n')[21]
    second_line_parts = second_line.split('=')
    second_line_parts[1] = x+stclst[0][:]+y
    
    second_line = '='.join(second_line_parts)
    lines = code.split('\n')
    lines[21] = second_line
    code = '\n'.join(lines)

    fout = open('main.py', 'w')
    fout.write(code)
    fout.close()      
updateCount()
