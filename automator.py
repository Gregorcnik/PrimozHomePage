def oklepaj(string, tag, zamik, Class='', Id=''):
    if not(Class==''):
        Class = ' '+Class
    if not(Id==''):
        Id = ' '+Id
    return f'{(zamik-1)*"  "}<{tag}{Class}{Id}>\n{zamik*"  "}{string}\n{(zamik-1)*"  "}</{tag}>'

summary = input()
text = input()
print(oklepaj(oklepaj(summary, 'summary', 2)+'\n'+oklepaj(text, 'p', 2), 'details', 0))
