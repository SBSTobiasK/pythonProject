def myFunc_1(par1, par2):
  tmp = []
  tmp.append(par1+par2)
  tmp.append(par1*par2)
  tmp.append(par1-par2)
  tmp.append(par1/par2)
  return tmp

lst1 = [[10, 2], [15, 4]]

for x, y in lst1:
  erg = myFunc_1(x,y)
  print(erg)