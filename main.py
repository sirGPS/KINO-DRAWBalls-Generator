# DRAW cells generator
    # author : GPS
    # DATE   : 07 07 2022


# variables

c1 = 61 # = equal sign for excel functions

c2 = 97 # a start of abs function 
c3 = 98 # b 
c4 = 115 # s  

c5 = 40 # open abs function

# c6 = 75 # K 

c61 = (922) # K
c62 = (921) # I 
c63 = (925) # N 
c64 = (927) # O 

c7 = 33 # !
# PESOS
c8 = 68 # Letter D 
# PESOS
c9 = 4 
c10 = 41 # end abs excel function

# spesial variables

PESOS = 36

# split the range 
 
full = (6000)
half = (full / 2)
quart = (full / 4)

# where to start

firstrow = (4)

# executable code

f = open("drawBalls.csv",'w')
fw = f.write

for c9 in range(int(firstrow),int(full)):
    
    for c8 in range(68,88):
        
        #print(chr(c1),chr(c2),chr(c3),chr(c4),chr(c5),chr(c61),chr(c62),chr(c63),chr(c64),chr(c7),chr(PESOS),chr(c8),chr(PESOS), c9 , chr(c10), sep = '')
        
        
        fw(chr(c1))
        fw(chr(c2))
        fw(chr(c3))
        fw(chr(c4))
        fw(chr(c5))
        fw(chr(c61))
        fw(chr(c62))
        fw(chr(c63))
        fw(chr(c64))
        fw(chr(c7))
        fw(chr(PESOS))
        fw(chr(c8))
        fw(chr(PESOS))
        fw(str(c9)) # cast as string
        fw(chr(c10))
        fw(chr(10)) # new line
        
        
        
        c8 = c8 + 1 # go to next row
        
    c9 = c9 + 1





