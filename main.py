# DRAW cells generator
    # author GPS
    # 07 07 2022
    
# LOG
    # IT generates a code to be used as formula to read a neighborhood sheet in excel
    # that is previews draws from kino OPAP greece and cyprus
        
# variables

c1 = 61 # = equal sign for excel functions
c2 = 97 # a start of abs function 
c3 = 98 # b 
c4 = 115 # s  
c5 = 40 # open abs function
c6 = 75 # K 
c7 = 33 # !
# PESOS
c8 = 68 # Letter D 
# PESOS
c9 = 4 
c10 = 41 # end abs excel function
PESOS = 36
full = (5124)
half = (full / 2)
quart = (full / 4)
firstrow = (4)

# executable code

for c9 in range(int(firstrow),int(quart)):
    
    for c8 in range(68,88):
        
        print(chr(c1),chr(c2),chr(c3),chr(c4),chr(c5),chr(c6),chr(c7),chr(PESOS),chr(c8),chr(PESOS), c9 , chr(c10), sep = '')
        c8 = c8 + 1
        
    c9 = c9 + 1


