
a = [1, 2, 3]
b = [1, 3, 3]

a == b # True
a is b # False
id(a) # 140539840

array = [1, 2, 3, 4, 3] # array mutabile
tupla = (1, 2, 3, 4, 5) # array non mutabile
insieme = {1, 2, 3, 4, 5} # insieme non ordinato

# primo incluso secondo escluso 
s = "Hello world"
s[0] # H
s[1:5] # ello

# try-except
try: input 
except NameError: pass