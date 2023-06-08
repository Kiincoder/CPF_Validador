CPF = ""

ValiCODE = CPF[9] + CPF[10]

count_FirstVali01 = 10
sum_Vali01 = 0
count_FirstVali02 = 11
sum_Vali02 = 0

for number in range(0, len(CPF)-2):  
  for caracter in CPF[number]:
      caracter = int(caracter)    
      result = caracter * count_FirstVali01
      count_FirstVali01 -= 1
      sum_Vali01 = result + sum_Vali01

for number in range(0, len(CPF)-1):  
  for caracter in CPF[number]:
      caracter = int(caracter)  
      resultt = caracter * count_FirstVali02
      count_FirstVali02 -= 1 
      sum_Vali02 = resultt + sum_Vali02

CharCODE1 = sum_Vali01 % 11 
CharCODE1 -= 11
CharCODE1 = abs(CharCODE1) 

if CharCODE1 >= 10:
   CharCODE1 = 0

CharCODE1 = str(CharCODE1)

CharCODE2 = sum_Vali02 % 11 
CharCODE2 -= 11
CharCODE2 = abs(CharCODE2)

if CharCODE2 >= 10:
   CharCODE2 = 0

CharCODE2 = str(CharCODE2)


if CharCODE1 + CharCODE2 == ValiCODE:   
   print('True')
else:
   print('False')