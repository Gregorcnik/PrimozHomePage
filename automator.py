def oklepaj(string, tag, zamik, Class='', Id=''):
    if not(Class==''):
        Class = ' '+Class
    if not(Id==''):
        Id = ' '+Id
    return f'{(zamik-1)*"  "}<{tag}{Class}{Id}>\n{zamik*"  "}{string}\n{(zamik-1)*"  "}</{tag}>'

f = open('indexTest.html', 'r')
index=[];
for vrstica in f:
    index.append(vrstica)
f.close()

f = open('vsebina.txt', 'r')
vsebina=[];
for vrstica in f:
    vsebina.append(vrstica.replace('\n', ''))
f.close()

dodatek=''
for i in range(0, len(vsebina), 2):
    dodatek+=oklepaj(oklepaj(vsebina[i], 'summary', 0)+'\n'+oklepaj(vsebina[i+1], 'p', 0), 'details', 0)+'\n'
dodatek+='\n'

print(dodatek)

dodajaj = index.index('<!-- dodajaj -->\n')
index.insert(dodajaj, dodatek)

indexStr=''
for i in range(0, len(index)):
    indexStr+=index[i]

f=open('indexTest.html', 'w')
f.write(indexStr)
f.close();
