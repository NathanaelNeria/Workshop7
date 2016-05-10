from programminglanguage import Language

ruby = Language("Ruby", "Dynamic", True, 1995)
python = Language("Python", "Dynamic", True, 1991)
vb = Language("Visual Basic", "Static", False, 1991)
c = Language('C++', 'Static', False, 1983)
java=Language('Java', 'Static', False, 1995)

print(ruby)
print(python)
print(vb)
print(c)
print(java)

programminglanguage_list={ruby, python, vb, c, java}

print('The dynamically typed languages are:')
for each in programminglanguage_list:
    if each.is_dynamic():
        print(each.name)