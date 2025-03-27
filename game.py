import os 
import random
import pynput

try:
    import pynput

except ImportError:
    os.system("python -m pip install pynput")
    import pynput

from pynput.keyboard import Key, Listener


l = [

        0,0,0,0,
        0,0,0,0,
        2,0,0,0,
        0,0,0,0,         
    
    ]


row1 = [l[0], l[1], l[2], l[3]]
row2 = [l[4], l[5], l[6], l[7]]
row3 = [l[8], l[9], l[10], l[11]]
row4 = [l[12], l[13], l[14], l[15]]

l2 = [row1, row2, row3, row4]


LINE_CLEAR = '\x1b[2K'
global scr 
scr = 0



def spawn():

    ran1 = random.choice([row1, row2, row3, row4])
    indx = random.randint(0,3)
    
    if ran1[indx] == 0:           
        ran1[indx] = 2

    
    else:
        spawn()

def row():
    spawn() 
    for i in l2:
        print(i)



def add(a, b):
    global scr
    scr += a + b
    return a + b


row()
print("\nScore:", scr)

# Do)wn function is called upon pressing 's'

def down():
    
    if row1[0] == row2[0] and row1[0] != 0:
        
        if row3[0] == 0 and row4[0] == 0:
            row4[0] = add(row1[0], row2[0])
            row1[0], row2[0], row3[0] = 0, 0, 0
        

        elif row3[0] == 0 and row4[0] != 0:
            
            if row2[0] != row4[0]:
                row3[0] = add(row1[0], row2[0]) 
                row1[0], row2[0] = 0, 0

            elif row2[0] == row4[0]:
                row4[0] = add(row2[0], row4[0])
                row3[0] = row1[0]
                row1[0] = 0
                row2[0] = 0
         

        elif row3[0] == row4[0]:
            
            row4[0] = add(row4[0], row3[0])
            row3[0] = add(row1[0], row2[0])
            row1[0], row2[0] = 0, 0

        
        elif row3[0] != 0 and row4[0] != 0 and row2[0] != row3[0]:
            
            row2[0] = add(row1[0], row2[0]) 
            row1[0] = 0
            # call(col1)
        
        elif row2[0] == row3[0]:
            print("y")

            if row4[0] != 0:
                row3[0] = add(row2[0], row2[0])
                row2[0] = row1[0]
                row1[0] = 0 
            elif row4[0] == 0:
                row4[0] = add(row3[0], row2[0]) 
                row3[0] = row1[0]
                row1[0] = 0
                row2[0] = 0
        
        elif row2[0] != row3[0] and row4[0] == 0:
            row4[0] = row3[0]
            row3[0] = add(row2[0], row1[0])
            row2[0] = 0
            row1[0] = 0

        
    
    elif row2[0] == row3[0] and row3[0] != 0:
        
        if row4[0] == 0:

            row4[0] = add(row2[0], row3[0])
            row3[0] = row1[0]
            row1[0] = 0
            row2[0] = 0
            # call(col1)

        elif row4[0] != 0 and row3[0] != row4[0]:
            row3[0] = add(row2[0], row3[0])
            row2[0] = row1[0]
            row1[0] = 0
            # call(col1)
        
        elif row3[0] == row4[0]:
            row4[0] = add(row3[0], row4[0])
            row3[0] = row2[0]
            if row1[0] != 0:
                row2[0] = row1[0]
                row1[0] = 0
            else:
                row2[0] = 0
            
    
    elif row3[0] == row4[0] and row3[0] != 0:
            
            row4[0] = add(row3[0], row4[0])
            if row2[0] != 0:
                row3[0] = row2[0]
                row2[0] = row1[0]
                row1[0] = 0
            elif row2[0] == 0:
                row3[0] = row1[0]
                row1[0] = 0
            # call(col1)
    
    elif row2[0]==row3[0]==row4[0] and row2[0] == 0 and row1[0] != 0:
        
        row4[0] = row1[0]
        row1[0] = 0

    elif row1[0]==row3[0]==row4[0] and row1[0] == 0 and row2[0] != 0:
        
        row4[0] = row2[0]
        row2[0] = 0
    
    elif row1[0]==row2[0]==row4[0] and row1[0] == 0 and row3[0] != 0:
        
        row4[0] = row3[0]
        row3[0] = 0
    



    elif row1[0] == row3[0] and row3[0] != 0:
        
        if row2[0] == row4[0] and row4[0] == 0:
            row4[0] = add(row1[0], row3[0])
            row1[0] = 0
            row3[0] = 0

        elif row2[0] == 0 and row4[0] != 0:
            row3[0] =  add(row1[0], row3[0])
            row1[0] = 0
            row2[0] = 0
        
        elif row4[0] == 0 and row2[0] != 0 and row2[0] != row1[0]:
            row4[0] = row3[0]
            row3[0] = row2[0]
            row2[0] = row1[0]
            row1[0] = 0 
    
    elif row2[0] == row4[0]:
        
        if row1[0] == row3[0] and row3[0] == 0:
            row4[0] = add(row2[0], row4[0])
            row2[0] = 0
        elif row4[0] == 0:
            row4[0] = row3[0]
            row3[0] = row1[0]
            row1[0] = 0
        elif row3[0] == 0 and row4[0] != 0:
            row4[0] = add(row2[0], row4[0])
            row2[0] = 0
            row3[0] = row1[0]
            row1[0] = 0

    elif row1[0] == row4[0] and row2[0] == row3[0] and row3[0] == 0:
        
        row4[0] = add(row1[0], row4[0])
        row1[0] = 0

    elif row1[0] != row2[0]:
        
        if row3[0] == row4[0] and row4[0] == 0:
            row4[0] = row2[0]
            row3[0] = row1[0]
            row1[0] = 0
            row2[0] = 0
        
        elif row4[0] != 0 and row3[0] == 0 and row2[0] != 0:
            
            row3[0] = row2[0]
            row2[0] = row1[0]
            row1[0] = 0

        elif row4[0] == 0 and row3[0] != 0:
            
            row4[0] = row3[0]
            row3[0] = row2[0]
            row2[0] = row1[0]
            row1[0] = 0

        elif row2[0] == row3[0] and row3[0] == 0 and row4[0] != 0:
            
            row3[0] = row1[0]
            row1[0] = 0        
        


        elif row2[0] == row4[0] and row3[0] == 0:
            
            row4[0] = add(row2[0], row4[0])
            row3[0] = row1[0]
            row2[0] = row1[0]
            row1[0] = 0
        



    
    
    

        

        
    
    # Column 2
      
    if row1[1] == row2[1] and row1[1] != 0:
        
        if row3[1] == 0 and row4[1] == 0:
            
            row4[1] = add(row1[1], row2[1]) 
            row1[1], row2[1], row3[1] = 0, 0, 0
        
        elif row3[1] == 0 and row4[1] != 0:

            if row2[1] != row4[1]:
                row3[1] = add(row1[1], row2[1]) 
                row1[1], row2[1] = 0, 0
            elif row2[1] == row4[1]:
                row4[1] = add(row2[1], row4[1])
                row3[1] = row1[1]
                row1[1] = 0
                row2[1] = 0
         
        elif row3[1] == row4[1]:
            
            row4[1] = add(row4[1], row3[1])
            row3[1] = add(row1[1], row2[1])
            row1[1], row2[1] = 0, 0

        
        elif row3[1] != 0 and row4[1] != 0 and row2[1] != row3[1]:
            
            row2[1] = add(row1[1], row2[1]) 
            row1[1] = 0
            # call(col1)
        
        elif row2[1] == row3[1]:
            if row4[1] != 0:
                row3[1] = add(row2[1], row2[1])
                row2[1] = row1[1]
                row1[1] = 0 
            elif row4[1] == 0:
                row4[1] = add(row3[1], row2[1]) 
                row3[1] = row1[1]
                row1[1] = 0
                row2[1] = 0
        
        elif row2[1] != row3[1] and row4[1] == 0:
            row4[1] = row3[1]
            row3[1] = add(row2[1], row1[1])
            row2[1] = 0
            row1[1] = 0
    
    elif row2[1] == row3[1] and row3[1] != 0:
        
        if row4[1] == 0:

            row4[1] = add(row2[1], row3[1])
            row3[1] = row1[1]
            row1[1] = 0
            row2[1] = 0
            # call(col1)

        elif row4[1] != 0 and row3[1] != row4[1]:
            row3[1] = add(row2[1], row3[1])
            row2[1] = row1[1]
            row1[1] = 0
            # call(col1)
        
        elif row3[1] == row4[1]:
            row4[1] = add(row3[1], row4[1])
            row3[1] = row2[1]
            if row1[1] != 0:
                row2[1] = row1[1]
                row1[1] = 0
            else:
                row2[1] = 0
            
    
    elif row3[1] == row4[1] and row3[1] != 0:
            
            row4[1] = add(row3[1], row4[1])
            if row2[1] != 0:
                row3[1] = row2[1]
                row2[1] = row1[1]
                row1[1] = 0
            elif row2[1] == 0:
                row3[1] = row1[1]
                row1[1] = 0
            # call(col1)
    
    elif row2[1]==row3[1]==row4[1] and row2[1] == 0 and row1[1] != 0:
        
        row4[1] = row1[1]
        row1[1] = 0

    elif row1[1]==row3[1]==row4[1] and row1[1] == 0 and row2[1] != 0:
        
        row4[1] = row2[1]
        row2[1] = 0
    
    elif row1[1]==row2[1]==row4[1] and row1[1] == 0 and row3[1] != 0:
        
        row4[1] = row3[1]
        row3[1] = 0
    



    elif row1[1] == row3[1] and row3[1] != 0:
        
        if row2[1] == row4[1] and row4[1] == 0:
            row4[1] = add(row1[1], row3[1])
            row1[1] = 0
            row3[1] = 0

        elif row2[1] == 0 and row4[1] != 0:
            row3[1] =  add(row1[1], row3[1])
            row1[1] = 0
            row2[1] = 0
        
        elif row4[1] == 0 and row2[1] != 0 and row2[1] != row1[1]:
            row4[1] = row3[1]
            row3[1] = row2[1]
            row2[1] = row1[1]
            row1[1] = 0 
    
    elif row2[1] == row4[1]:
        
        if row1[1] == row3[1] and row3[1] == 0:
            row4[1] = add(row2[1], row4[1])
            row2[1] = 0
        elif row4[1] == 0:
            row4[1] = row3[1]
            row3[1] = row1[1]
            row1[1] = 0
        elif row3[1] == 0 and row4[1] != 0:
            row4[1] = add(row2[1], row4[1])
            row2[1] = 0
            row3[1] = row1[1]
            row1[1] = 0

    elif row1[1] == row4[1] and row2[1] == row3[1] and row3[1] == 0:
        
        row4[1] = add(row1[1], row4[1])
        row1[1] = 0

    elif row1[1] != row2[1]:
        
        if row3[1] == row4[1] and row4[1] == 0:
            row4[1] = row2[1]
            row3[1] = row1[1]
            row1[1] = 0
            row2[1] = 0
        
        elif row4[1] != 0 and row3[1] == 0 and row2[1] != 0:
            
            row3[1] = row2[1]
            row2[1] = row1[1]
            row1[1] = 0

        elif row4[1] == 0 and row3[1] != 0:
            
            row4[1] = row3[1]
            row3[1] = row2[1]
            row2[1] = row1[1]
            row1[1] = 0

        elif row2[1] == row3[1] and row3[1] == 0 and row4[1] != 0:
            
            row3[1] = row1[1]
            row1[1] = 0        
        


        elif row2[1] == row4[1] and row3[1] == 0:
            
            row4[1] = add(row2[1], row4[1])
            row3[1] = row1[1]
            row2[1] = row1[1]
            row1[1] = 0


# Column 3

    
    if row1[2] == row2[2] and row1[2] != 0:
        
        if row3[2] == 0 and row4[2] == 0:
            
            row4[2] = add(row1[2], row2[2]) 
            row1[2], row2[2], row3[2] = 0, 0, 0
        
        elif row3[2] == 0 and row4[2] != 0:

            if row2[2] != row4[2]:
                row3[2] = add(row1[2], row2[2]) 
                row1[2], row2[2] = 0, 0
            elif row2[2] == row4[2]:
                row4[2] = add(row2[2], row4[2])
                row3[2] = row1[2]
                row1[2] = 0
                row2[2] = 0
         
        elif row3[2] == row4[2]:
            
            row4[2] = add(row4[2], row3[2])
            row3[2] = add(row1[2], row2[2])
            row1[2], row2[2] = 0, 0
        
        elif row3[2] != 0 and row4[2] != 0 and row2[2] != row3[2]:
            
            row2[2] = add(row1[2], row2[2]) 
            row1[2] = 0
            # call(col1)
        
        elif row2[2] == row3[2]:
            if row4[2] != 0:
                row3[2] = add(row2[2], row2[2])
                row2[2] = row1[2]
                row1[2] = 0 
            elif row4[2] == 0:
                row4[2] = add(row3[2], row2[2]) 
                row3[2] = row1[2]
                row1[2] = 0
                row2[2] = 0
        
        elif row2[2] != row3[2] and row4[2] == 0:
            row4[2] = row3[2]
            row3[2] = add(row2[2], row1[2])
            row2[2] = 0
            row1[2] = 0
    
    elif row2[2] == row3[2] and row3[2] != 0:
        
        if row4[2] == 0:

            row4[2] = add(row2[2], row3[2])
            row3[2] = row1[2]
            row1[2] = 0
            row2[2] = 0
            # call(col1)

        elif row4[2] != 0 and row3[2] != row4[2]:
            row3[2] = add(row2[2], row3[2])
            row2[2] = row1[2]
            row1[2] = 0
            # call(col1)
        
        elif row3[2] == row4[2]:
            row4[2] = add(row3[2], row4[2])
            row3[2] = row2[2]
            if row1[2] != 0:
                row2[2] = row1[2]
                row1[2] = 0
            else:
                row2[2] = 0
            
    
    elif row3[2] == row4[2] and row3[2] != 0:
            
            row4[2] = add(row3[2], row4[2])
            if row2[2] != 0:
                row3[2] = row2[2]
                row2[2] = row1[2]
                row1[2] = 0
            elif row2[2] == 0:
                row3[2] = row1[2]
                row1[2] = 0
            # call(col1)
    
    elif row2[2]==row3[2]==row4[2] and row2[2] == 0 and row1[2] != 0:
        
        row4[2] = row1[2]
        row1[2] = 0

    elif row1[2]==row3[2]==row4[2] and row1[2] == 0 and row2[2] != 0:
        
        row4[2] = row2[2]
        row2[2] = 0
    
    elif row1[2]==row2[2]==row4[2] and row1[2] == 0 and row3[2] != 0:
        
        row4[2] = row3[2]
        row3[2] = 0
    



    elif row1[2] == row3[2] and row3[2] != 0:
        
        if row2[2] == row4[2] and row4[2] == 0:
            row4[2] = add(row1[2], row3[2])
            row1[2] = 0
            row3[2] = 0

        elif row2[2] == 0 and row4[2] != 0:
            row3[2] =  add(row1[2], row3[2])
            row1[2] = 0
            row2[2] = 0
        
        elif row4[2] == 0 and row2[2] != 0 and row2[2] != row1[2]:
            row4[2] = row3[2]
            row3[2] = row2[2]
            row2[2] = row1[2]
            row1[2] = 0 
    
    elif row2[2] == row4[2]:
        
        if row1[2] == row3[2] and row3[2] == 0:
            row4[2] = add(row2[2], row4[2])
            row2[2] = 0
        elif row4[2] == 0:
            row4[2] = row3[2]
            row3[2] = row1[2]
            row1[2] = 0
        elif row3[2] == 0 and row4[2] != 0:
            row4[2] = add(row2[2], row4[2])
            row2[2] = 0
            row3[2] = row1[2]
            row1[2] = 0

    elif row1[2] == row4[2] and row2[2] == row3[2] and row3[2] == 0:
        
        row4[2] = add(row1[2], row4[2])
        row1[2] = 0

    elif row1[2] != row2[2]:
        
        if row3[2] == row4[2] and row4[2] == 0:
            row4[2] = row2[2]
            row3[2] = row1[2]
            row1[2] = 0
            row2[2] = 0
        
        elif row4[2] != 0 and row3[2] == 0 and row2[2] != 0:
            
            row3[2] = row2[2]
            row2[2] = row1[2]
            row1[2] = 0

        elif row4[2] == 0 and row3[2] != 0:
            
            row4[2] = row3[2]
            row3[2] = row2[2]
            row2[2] = row1[2]
            row1[2] = 0

        elif row2[2] == row3[2] and row3[2] == 0 and row4[2] != 0:
            
            row3[2] = row1[2]
            row1[2] = 0        
        


        elif row2[2] == row4[2] and row3[2] == 0:
            
            row4[2] = add(row2[2], row4[2])
            row3[2] = row1[2]
            row2[2] = row1[2]
            row1[2] = 0
        
# Column 4

    
    if row1[3] == row2[3] and row1[3] != 0:
        
        if row3[3] == 0 and row4[3] == 0:
            
            row4[3] = add(row1[3], row2[3]) 
            row1[3], row2[3], row3[3] = 0, 0, 0
        
        elif row3[3] == 0 and row4[3] != 0:

            if row2[3] != row4[3]:
                row3[3] = add(row1[3], row2[3]) 
                row1[3], row2[3] = 0, 0
            elif row2[3] == row4[3]:
                row4[3] = add(row2[3], row4[3])
                row3[3] = row1[3]
                row1[3] = 0
                row2[3] = 0
         
        elif row3[3] == row4[3]:
            
            row4[3] = add(row4[3], row3[3])
            row3[3] = add(row1[3], row2[3])
            row1[3], row2[3] = 0, 0

        
        elif row3[3] != 0 and row4[3] != 0 and row2[3] != row3[3]:
            
            row2[3] = add(row1[3], row2[3]) 
            row1[3] = 0
            # call(col1)
        
        elif row2[3] == row3[3]:
            if row4[3] != 0:
                row3[3] = add(row2[3], row2[3])
                row2[3] = row1[3]
                row1[3] = 0 
            elif row4[3] == 0:
                row4[3] = add(row3[3], row2[3]) 
                row3[3] = row1[3]
                row1[3] = 0
                row2[3] = 0

        elif row2[3] != row3[3] and row4[3] == 0:
            row4[3] = row3[3]
            row3[3] = add(row2[3], row1[3])
            row2[3] = 0
            row1[3] = 0

    elif row2[3] == row3[3] and row3[3] != 0:
        
        if row4[3] == 0:

            row4[3] = add(row2[3], row3[3])
            row3[3] = row1[3]
            row1[3] = 0
            row2[3] = 0
            # call(col1)

        elif row4[3] != 0 and row3[3] != row4[3]:
            row3[3] = add(row2[3], row3[3])
            row2[3] = row1[3]
            row1[3] = 0
            # call(col1)
        
        elif row3[3] == row4[3]:
            row4[3] = add(row3[3], row4[3])
            row3[3] = row2[3]
            if row1[3] != 0:
                row2[3] = row1[3]
                row1[3] = 0
            else:
                row2[3] = 0
            
    
    elif row3[3] == row4[3] and row3[3] != 0:
            
            row4[3] = add(row3[3], row4[3])
            if row2[3] != 0:
                row3[3] = row2[3]
                row2[3] = row1[3]
                row1[3] = 0
            elif row2[3] == 0:
                row3[3] = row1[3]
                row1[3] = 0
            # call(col1)
    
    elif row2[3]==row3[3]==row4[3] and row2[3] == 0 and row1[3] != 0:
        
        row4[3] = row1[3]
        row1[3] = 0

    elif row1[3]==row3[3]==row4[3] and row1[3] == 0 and row2[3] != 0:
        
        row4[3] = row2[3]
        row2[3] = 0
    
    elif row1[3]==row2[3]==row4[3] and row1[3] == 0 and row3[3] != 0:
        
        row4[3] = row3[3]
        row3[3] = 0
    



    elif row1[3] == row3[3] and row3[3] != 0:
        
        if row2[3] == row4[3] and row4[3] == 0:
            row4[3] = add(row1[3], row3[3])
            row1[3] = 0
            row3[3] = 0

        elif row2[3] == 0 and row4[3] != 0:
            row3[3] =  add(row1[3], row3[3])
            row1[3] = 0
            row2[3] = 0

        elif row4[3] == 0 and row2[3] != 0 and row2[3] != row1[2]:
            row4[3] = row3[2]
            row3[3] = row2[2]
            row2[3] = row1[2]
            row1[3] = 0 
    
    elif row2[3] == row4[3]:
        
        if row1[3] == row3[3] and row3[3] == 0:
            row4[3] = add(row2[3], row4[3])
            row2[3] = 0
        elif row4[3] == 0:
            row4[3] = row3[3]
            row3[3] = row1[3]
            row1[3] = 0
        elif row3[3] == 0 and row4[3] != 0:
            row4[3] = add(row2[3], row4[3])
            row2[3] = 0
            row3[3] = row1[3]
            row1[3] = 0

    elif row1[3] == row4[3] and row2[3] == row3[3] and row3[3] == 0:
        
        row4[3] = add(row1[3], row4[3])
        row1[3] = 0

    elif row1[3] != row2[3]:
        
        if row3[3] == row4[3] and row4[3] == 0:
            row4[3] = row2[3]
            row3[3] = row1[3]
            row1[3] = 0
            row2[3] = 0
        
        elif row4[3] != 0 and row3[3] == 0 and row2[3] != 0:
            
            row3[3] = row2[3]
            row2[3] = row1[3]
            row1[3] = 0

        elif row4[3] == 0 and row3[3] != 0:
            
            row4[3] = row3[3]
            row3[3] = row2[3]
            row2[3] = row1[3]
            row1[3] = 0

        elif row2[3] == row3[3] and row3[3] == 0 and row4[3] != 0:
            
            row3[3] = row1[3]
            row1[3] = 0        
        


        elif row2[3] == row4[3] and row3[3] == 0:
            
            row4[3] = add(row2[3], row4[3])
            row3[3] = row1[3]
            row2[3] = row1[3]
            row1[3] = 0



def up():
    if row4[0] == row3[0] and row4[0] != 0:
        
        if row2[0] == 0 and row1[0] == 0:
            
            row1[0] = add(row4[0], row3[0]) 
            row4[0], row3[0], row2[0] = 0, 0, 0
        
        elif row2[0] == 0 and row1[0] != 0:
            
            if row3[0] != row1[0]:
                row2[0] = add(row4[0], row3[0]) 
                row4[0], row3[0] = 0, 0
            elif row3[0] == row1[0]:
                row1[0] = add(row3[0], row1[0])
                row2[0] = row4[0]
                row4[0] = 0
                row3[0] = 0
         
        elif row2[0] == row1[0]:
            
            row1[0] = add(row1[0], row2[0])
            row2[0] = add(row4[0], row3[0])
            row4[0], row3[0] = 0, 0

        
        elif row2[0] != 0 and row1[0] != 0 and row3[0] != row2[0]:
            
            row3[0] = add(row4[0], row3[0]) 
            row4[0] = 0
            # call(col1)
        
        elif row3[0] == row2[0]:
            print("y")

            if row1[0] != 0:
                row2[0] = add(row3[0], row3[0])
                row3[0] = row4[0]
                row4[0] = 0 
            elif row1[0] == 0:
                row1[0] = add(row2[0], row3[0]) 
                row2[0] = row4[0]
                row4[0] = 0
                row3[0] = 0
        
        elif row3[0] != row2[0] and row1[0] == 0:
            row1[0] = row2[0]
            row2[0] = add(row3[0], row4[0])
            row3[0] = 0
            row4[0] = 0

        
    
    elif row3[0] == row2[0] and row2[0] != 0:
        
        if row1[0] == 0:

            row1[0] = add(row3[0], row2[0])
            row2[0] = row4[0]
            row4[0] = 0
            row3[0] = 0
            # call(col1)

        elif row1[0] != 0 and row2[0] != row1[0]:
            row2[0] = add(row3[0], row2[0])
            row3[0] = row4[0]
            row4[0] = 0
            # call(col1)
        
        elif row2[0] == row1[0]:
            row1[0] = add(row2[0], row1[0])
            row2[0] = row3[0]
            if row4[0] != 0:
                row3[0] = row4[0]
                row4[0] = 0
            else:
                row3[0] = 0
            
    
    elif row2[0] == row1[0] and row2[0] != 0:
            
            row1[0] = add(row2[0], row1[0])
            if row3[0] != 0:
                row2[0] = row3[0]
                row3[0] = row4[0]
                row4[0] = 0
            elif row3[0] == 0:
                row2[0] = row4[0]
                row4[0] = 0
            # call(col1)
    
    elif row3[0]==row2[0]==row1[0] and row3[0] == 0 and row4[0] != 0:
        
        row1[0] = row4[0]
        row4[0] = 0

    elif row4[0]==row2[0]==row1[0] and row4[0] == 0 and row3[0] != 0:
        
        row1[0] = row3[0]
        row3[0] = 0
    
    elif row4[0]==row3[0]==row1[0] and row4[0] == 0 and row2[0] != 0:
        
        row1[0] = row2[0]
        row2[0] = 0
    



    elif row4[0] == row2[0] and row2[0] != 0:
        
        if row3[0] == row1[0] and row1[0] == 0:
            row1[0] = add(row4[0], row2[0])
            row4[0] = 0
            row2[0] = 0

        elif row3[0] == 0 and row1[0] != 0:
            row2[0] =  add(row4[0], row2[0])
            row4[0] = 0
            row3[0] = 0
        
        elif row1[0] == 0 and row3[0] != 0 and row3[0] != row4[0]:
            row1[0] = row2[0]
            row2[0] = row3[0]
            row3[0] = row4[0]
            row4[0] = 0 
    
    elif row3[0] == row1[0]:
        
        if row4[0] == row2[0] and row2[0] == 0:
            row1[0] = add(row3[0], row1[0])
            row3[0] = 0
        elif row1[0] == 0:
            row1[0] = row2[0]
            row2[0] = row4[0]
            row4[0] = 0
        elif row2[0] == 0 and row1[0] != 0:
            row1[0] = add(row3[0], row1[0])
            row3[0] = 0
            row2[0] = row4[0]
            row4[0] = 0

    elif row4[0] == row1[0] and row3[0] == row2[0] and row2[0] == 0:
        
        row1[0] = add(row4[0], row1[0])
        row4[0] = 0

    elif row4[0] != row3[0]:
        
        if row2[0] == row1[0] and row1[0] == 0:
            row1[0] = row3[0]
            row2[0] = row4[0]
            row4[0] = 0
            row3[0] = 0
        
        elif row1[0] != 0 and row2[0] == 0 and row3[0] != 0:
            
            row2[0] = row3[0]
            row3[0] = row4[0]
            row4[0] = 0

        elif row1[0] == 0 and row2[0] != 0:
            
            row1[0] = row2[0]
            row2[0] = row3[0]
            row3[0] = row4[0]
            row4[0] = 0

        elif row3[0] == row2[0] and row2[0] == 0 and row1[0] != 0:
            
            row2[0] = row4[0]
            row4[0] = 0        
        


        elif row3[0] == row1[0] and row2[0] == 0:
            
            row1[0] = add(row3[0], row1[0])
            row2[0] = row4[0]
            row3[0] = row4[0]
            row4[0] = 0
        



    
    
    

        

        
    
    # Column 2
      
    if row4[1] == row3[1] and row4[1] != 0:
        
        if row2[1] == 0 and row1[1] == 0:
            
            row1[1] = add(row4[1], row3[1]) 
            row4[1], row3[1], row2[1] = 0, 0, 0
        
        elif row2[1] == 0 and row1[1] != 0:

            if row3[1] != row1[1]:
                row2[1] = add(row4[1], row3[1]) 
                row4[1], row3[1] = 0, 0
            elif row3[1] == row1[1]:
                row1[1] = add(row3[1], row1[1])
                row2[1] = row4[1]
                row4[1] = 0
                row3[1] = 0
         
        elif row2[1] == row1[1]:
            
            row1[1] = add(row1[1], row2[1])
            row2[1] = add(row4[1], row3[1])
            row4[1], row3[1] = 0, 0

        
        elif row2[1] != 0 and row1[1] != 0 and row3[1] != row2[1]:
            
            row3[1] = add(row4[1], row3[1]) 
            row4[1] = 0
            # call(col1)
        
        elif row3[1] == row2[1]:
            if row1[1] != 0:
                row2[1] = add(row3[1], row3[1])
                row3[1] = row4[1]
                row4[1] = 0 
            elif row1[1] == 0:
                row1[1] = add(row2[1], row3[1]) 
                row2[1] = row4[1]
                row4[1] = 0
                row3[1] = 0
        
        elif row3[1] != row2[1] and row1[1] == 0:
            row1[1] = row2[1]
            row2[1] = add(row3[1], row4[1])
            row3[1] = 0
            row4[1] = 0
    
    elif row3[1] == row2[1] and row2[1] != 0:
        
        if row1[1] == 0:

            row1[1] = add(row3[1], row2[1])
            row2[1] = row4[1]
            row4[1] = 0
            row3[1] = 0
            # call(col1)

        elif row1[1] != 0 and row2[1] != row1[1]:
            row2[1] = add(row3[1], row2[1])
            row3[1] = row4[1]
            row4[1] = 0
            # call(col1)
        
        elif row2[1] == row1[1]:
            row1[1] = add(row2[1], row1[1])
            row2[1] = row3[1]
            if row4[1] != 0:
                row3[1] = row4[1]
                row4[1] = 0
            else:
                row3[1] = 0
            
    
    elif row2[1] == row1[1] and row2[1] != 0:
            
            row1[1] = add(row2[1], row1[1])
            if row3[1] != 0:
                row2[1] = row3[1]
                row3[1] = row4[1]
                row4[1] = 0
            elif row3[1] == 0:
                row2[1] = row4[1]
                row4[1] = 0
            # call(col1)
    
    elif row3[1]==row2[1]==row1[1] and row3[1] == 0 and row4[1] != 0:
        
        row1[1] = row4[1]
        row4[1] = 0

    elif row4[1]==row2[1]==row1[1] and row4[1] == 0 and row3[1] != 0:
        
        row1[1] = row3[1]
        row3[1] = 0
    
    elif row4[1]==row3[1]==row1[1] and row4[1] == 0 and row2[1] != 0:
        
        row1[1] = row2[1]
        row2[1] = 0
    



    elif row4[1] == row2[1] and row2[1] != 0:
        
        if row3[1] == row1[1] and row1[1] == 0:
            row1[1] = add(row4[1], row2[1])
            row4[1] = 0
            row2[1] = 0

        elif row3[1] == 0 and row1[1] != 0:
            row2[1] =  add(row4[1], row2[1])
            row4[1] = 0
            row3[1] = 0
        
        elif row1[1] == 0 and row3[1] != 0 and row3[1] != row4[1]:
            row1[1] = row2[1]
            row2[1] = row3[1]
            row3[1] = row4[1]
            row4[1] = 0 
    
    elif row3[1] == row1[1]:
        
        if row4[1] == row2[1] and row2[1] == 0:
            row1[1] = add(row3[1], row1[1])
            row3[1] = 0
        elif row1[1] == 0:
            row1[1] = row2[1]
            row2[1] = row4[1]
            row4[1] = 0
        elif row2[1] == 0 and row1[1] != 0:
            row1[1] = add(row3[1], row1[1])
            row3[1] = 0
            row2[1] = row4[1]
            row4[1] = 0

    elif row4[1] == row1[1] and row3[1] == row2[1] and row2[1] == 0:
        
        row1[1] = add(row4[1], row1[1])
        row4[1] = 0

    elif row4[1] != row3[1]:
        
        if row2[1] == row1[1] and row1[1] == 0:
            row1[1] = row3[1]
            row2[1] = row4[1]
            row4[1] = 0
            row3[1] = 0
        
        elif row1[1] != 0 and row2[1] == 0 and row3[1] != 0:
            
            row2[1] = row3[1]
            row3[1] = row4[1]
            row4[1] = 0

        elif row1[1] == 0 and row2[1] != 0:
            
            row1[1] = row2[1]
            row2[1] = row3[1]
            row3[1] = row4[1]
            row4[1] = 0

        elif row3[1] == row2[1] and row2[1] == 0 and row1[1] != 0:
            
            row2[1] = row4[1]
            row4[1] = 0        
        


        elif row3[1] == row1[1] and row2[1] == 0:
            
            row1[1] = add(row3[1], row1[1])
            row2[1] = row4[1]
            row3[1] = row4[1]
            row4[1] = 0


# Column 3

    
    if row4[2] == row3[2] and row4[2] != 0:
        
        if row2[2] == 0 and row1[2] == 0:
            
            row1[2] = add(row4[2], row3[2]) 
            row4[2], row3[2], row2[2] = 0, 0, 0
        
        elif row2[2] == 0 and row1[2] != 0:

            if row3[2] != row1[2]:
                row2[2] = add(row4[2], row3[2]) 
                row4[2], row3[2] = 0, 0
            elif row3[2] == row1[2]:
                row1[2] = add(row3[2], row1[2])
                row2[2] = row4[2]
                row4[2] = 0
                row3[2] = 0
         
        elif row2[2] == row1[2]:
            
            row1[2] = add(row1[2], row2[2])
            row2[2] = add(row4[2], row3[2])
            row4[2], row3[2] = 0, 0
        
        elif row2[2] != 0 and row1[2] != 0 and row3[2] != row2[2]:
            
            row3[2] = add(row4[2], row3[2]) 
            row4[2] = 0
            # call(col1)
        
        elif row3[2] == row2[2]:
            if row1[2] != 0:
                row2[2] = add(row3[2], row3[2])
                row3[2] = row4[2]
                row4[2] = 0 
            elif row1[2] == 0:
                row1[2] = add(row2[2], row3[2]) 
                row2[2] = row4[2]
                row4[2] = 0
                row3[2] = 0
        
        elif row3[2] != row2[2] and row1[2] == 0:
            row1[2] = row2[2]
            row2[2] = add(row3[2], row4[2])
            row3[2] = 0
            row4[2] = 0
    
    elif row3[2] == row2[2] and row2[2] != 0:
        
        if row1[2] == 0:

            row1[2] = add(row3[2], row2[2])
            row2[2] = row4[2]
            row4[2] = 0
            row3[2] = 0
            # call(col1)

        elif row1[2] != 0 and row2[2] != row1[2]:
            row2[2] = add(row3[2], row2[2])
            row3[2] = row4[2]
            row4[2] = 0
            # call(col1)
        
        elif row2[2] == row1[2]:
            row1[2] = add(row2[2], row1[2])
            row2[2] = row3[2]
            if row4[2] != 0:
                row3[2] = row4[2]
                row4[2] = 0
            else:
                row3[2] = 0
            
    
    elif row2[2] == row1[2] and row2[2] != 0:
            
            row1[2] = add(row2[2], row1[2])
            if row3[2] != 0:
                row2[2] = row3[2]
                row3[2] = row4[2]
                row4[2] = 0
            elif row3[2] == 0:
                row2[2] = row4[2]
                row4[2] = 0
            # call(col1)
    
    elif row3[2]==row2[2]==row1[2] and row3[2] == 0 and row4[2] != 0:
        
        row1[2] = row4[2]
        row4[2] = 0

    elif row4[2]==row2[2]==row1[2] and row4[2] == 0 and row3[2] != 0:
        
        row1[2] = row3[2]
        row3[2] = 0
    
    elif row4[2]==row3[2]==row1[2] and row4[2] == 0 and row2[2] != 0:
        
        row1[2] = row2[2]
        row2[2] = 0
    



    elif row4[2] == row2[2] and row2[2] != 0:
        
        if row3[2] == row1[2] and row1[2] == 0:
            row1[2] = add(row4[2], row2[2])
            row4[2] = 0
            row2[2] = 0

        elif row3[2] == 0 and row1[2] != 0:
            row2[2] =  add(row4[2], row2[2])
            row4[2] = 0
            row3[2] = 0
        
        elif row1[2] == 0 and row3[2] != 0 and row3[2] != row4[2]:
            row1[2] = row2[2]
            row2[2] = row3[2]
            row3[2] = row4[2]
            row4[2] = 0 
    
    elif row3[2] == row1[2]:
        
        if row4[2] == row2[2] and row2[2] == 0:
            row1[2] = add(row3[2], row1[2])
            row3[2] = 0
        elif row1[2] == 0:
            row1[2] = row2[2]
            row2[2] = row4[2]
            row4[2] = 0
        elif row2[2] == 0 and row1[2] != 0:
            row1[2] = add(row3[2], row1[2])
            row3[2] = 0
            row2[2] = row4[2]
            row4[2] = 0

    elif row4[2] == row1[2] and row3[2] == row2[2] and row2[2] == 0:
        
        row1[2] = add(row4[2], row1[2])
        row4[2] = 0

    elif row4[2] != row3[2]:
        
        if row2[2] == row1[2] and row1[2] == 0:
            row1[2] = row3[2]
            row2[2] = row4[2]
            row4[2] = 0
            row3[2] = 0
        
        elif row1[2] != 0 and row2[2] == 0 and row3[2] != 0:
            
            row2[2] = row3[2]
            row3[2] = row4[2]
            row4[2] = 0

        elif row1[2] == 0 and row2[2] != 0:
            
            row1[2] = row2[2]
            row2[2] = row3[2]
            row3[2] = row4[2]
            row4[2] = 0

        elif row3[2] == row2[2] and row2[2] == 0 and row1[2] != 0:
            
            row2[2] = row4[2]
            row4[2] = 0        
        


        elif row3[2] == row1[2] and row2[2] == 0:
            
            row1[2] = add(row3[2], row1[2])
            row2[2] = row4[2]
            row3[2] = row4[2]
            row4[2] = 0
        
# Column 4

    
    if row4[3] == row3[3] and row4[3] != 0:
        
        if row2[3] == 0 and row1[3] == 0:
            
            row1[3] = add(row4[3], row3[3]) 
            row4[3], row3[3], row2[3] = 0, 0, 0
        
        elif row2[3] == 0 and row1[3] != 0:

            if row3[3] != row1[3]:
                row2[3] = add(row4[3], row3[3]) 
                row4[3], row3[3] = 0, 0
            elif row3[3] == row1[3]:
                row1[3] = add(row3[3], row1[3])
                row2[3] = row4[3]
                row4[3] = 0
                row3[3] = 0
         
        elif row2[3] == row1[3]:
            
            row1[3] = add(row1[3], row2[3])
            row2[3] = add(row4[3], row3[3])
            row4[3], row3[3] = 0, 0

        
        elif row2[3] != 0 and row1[3] != 0 and row3[3] != row2[3]:
            
            row3[3] = add(row4[3], row3[3]) 
            row4[3] = 0
            # call(col1)
        
        elif row3[3] == row2[3]:
            if row1[3] != 0:
                row2[3] = add(row3[3], row3[3])
                row3[3] = row4[3]
                row4[3] = 0 
            elif row1[3] == 0:
                row1[3] = add(row2[3], row3[3]) 
                row2[3] = row4[3]
                row4[3] = 0
                row3[3] = 0

        elif row3[3] != row2[3] and row1[3] == 0:
            row1[3] = row2[3]
            row2[3] = add(row3[3], row4[3])
            row3[3] = 0
            row4[3] = 0

    elif row3[3] == row2[3] and row2[3] != 0:
        
        if row1[3] == 0:

            row1[3] = add(row3[3], row2[3])
            row2[3] = row4[3]
            row4[3] = 0
            row3[3] = 0
            # call(col1)

        elif row1[3] != 0 and row2[3] != row1[3]:
            row2[3] = add(row3[3], row2[3])
            row3[3] = row4[3]
            row4[3] = 0
            # call(col1)
        
        elif row2[3] == row1[3]:
            row1[3] = add(row2[3], row1[3])
            row2[3] = row3[3]
            if row4[3] != 0:
                row3[3] = row4[3]
                row4[3] = 0
            else:
                row3[3] = 0
            
    
    elif row2[3] == row1[3] and row2[3] != 0:
            
            row1[3] = add(row2[3], row1[3])
            if row3[3] != 0:
                row2[3] = row3[3]
                row3[3] = row4[3]
                row4[3] = 0
            elif row3[3] == 0:
                row2[3] = row4[3]
                row4[3] = 0
            # call(col1)
    
    elif row3[3]==row2[3]==row1[3] and row3[3] == 0 and row4[3] != 0:
        
        row1[3] = row4[3]
        row4[3] = 0

    elif row4[3]==row2[3]==row1[3] and row4[3] == 0 and row3[3] != 0:
        
        row1[3] = row3[3]
        row3[3] = 0
    
    elif row4[3]==row3[3]==row1[3] and row4[3] == 0 and row2[3] != 0:
        
        row1[3] = row2[3]
        row2[3] = 0
    



    elif row4[3] == row2[3] and row2[3] != 0:
        
        if row3[3] == row1[3] and row1[3] == 0:
            row1[3] = add(row4[3], row2[3])
            row4[3] = 0
            row2[3] = 0

        elif row3[3] == 0 and row1[3] != 0:
            row2[3] =  add(row4[3], row2[3])
            row4[3] = 0
            row3[3] = 0

        elif row1[3] == 0 and row3[3] != 0 and row3[3] != row4[2]:
            row1[3] = row2[2]
            row2[3] = row3[2]
            row3[3] = row4[2]
            row4[3] = 0 
    
    elif row3[3] == row1[3]:
        
        if row4[3] == row2[3] and row2[3] == 0:
            row1[3] = add(row3[3], row1[3])
            row3[3] = 0
        elif row1[3] == 0:
            row1[3] = row2[3]
            row2[3] = row4[3]
            row4[3] = 0
        elif row2[3] == 0 and row1[3] != 0:
            row1[3] = add(row3[3], row1[3])
            row3[3] = 0
            row2[3] = row4[3]
            row4[3] = 0

    elif row4[3] == row1[3] and row3[3] == row2[3] and row2[3] == 0:
        
        row1[3] = add(row4[3], row1[3])
        row4[3] = 0

    elif row4[3] != row3[3]:
        
        if row2[3] == row1[3] and row1[3] == 0:
            row1[3] = row3[3]
            row2[3] = row4[3]
            row4[3] = 0
            row3[3] = 0
        
        elif row1[3] != 0 and row2[3] == 0 and row3[3] != 0:
            
            row2[3] = row3[3]
            row3[3] = row4[3]
            row4[3] = 0

        elif row1[3] == 0 and row2[3] != 0:
            
            row1[3] = row2[3]
            row2[3] = row3[3]
            row3[3] = row4[3]
            row4[3] = 0

        elif row3[3] == row2[3] and row2[3] == 0 and row1[3] != 0:
            
            row2[3] = row4[3]
            row4[3] = 0        
        


        elif row3[3] == row1[3] and row2[3] == 0:
            
            row1[3] = add(row3[3], row1[3])
            row2[3] = row4[3]
            row3[3] = row4[3]
            row4[3] = 0

       

def right():
    
    # For Row 1

    if row1[0] == row1[1] and row1[0] != 0:
        
        if row1[2] == 0 and row1[3] == 0:
            
            row1[3] = add(row1[0], row1[1]) 
            row1[0], row1[1], row1[2] = 0, 0, 0
        
        elif row1[2] == 0 and row1[3] != 0:
            
            if row1[1] != row1[3]:
                row1[2] = add(row1[0], row1[1]) 
                row1[0], row1[1] = 0, 0
            elif row1[1] == row1[3]:
                row1[3] = add(row1[1], row1[3])
                row1[2] = row1[0]
                row1[0] = 0
                row1[1] = 0
         
        elif row1[2] == row1[3]:
            
            row1[3] = add(row1[3], row1[2])
            row1[2] = add(row1[0], row1[1])
            row1[0], row1[1] = 0, 0

        
        elif row1[2] != 0 and row1[3] != 0 and row1[1] != row1[2]:
            
            row1[1] = add(row1[0], row1[1]) 
            row1[0] = 0
            # call(col1)
        
        elif row1[1] == row1[2]:
            print("y")

            if row1[3] != 0:
                row1[2] = add(row1[1], row1[1])
                row1[1] = row1[0]
                row1[0] = 0 
            elif row1[3] == 0:
                row1[3] = add(row1[2], row1[1]) 
                row1[2] = row1[0]
                row1[0] = 0
                row1[1] = 0
        
        elif row1[1] != row1[2] and row1[3] == 0:
            row1[3] = row1[2]
            row1[2] = add(row1[1], row1[0])
            row1[1] = 0
            row1[0] = 0

        
    
    elif row1[1] == row1[2] and row1[2] != 0:
        
        if row1[3] == 0:

            row1[3] = add(row1[1], row1[2])
            row1[2] = row1[0]
            row1[0] = 0
            row1[1] = 0
            # call(col1)

        elif row1[3] != 0 and row1[2] != row1[3]:
            row1[2] = add(row1[1], row1[2])
            row1[1] = row1[0]
            row1[0] = 0
            # call(col1)
        
        elif row1[2] == row1[3]:
            row1[3] = add(row1[2], row1[3])
            row1[2] = row1[1]
            if row1[0] != 0:
                row1[1] = row1[0]
                row1[0] = 0
            else:
                row1[1] = 0
            
    
    elif row1[2] == row1[3] and row1[2] != 0:
            
            row1[3] = add(row1[2], row1[3])
            if row1[1] != 0:
                row1[2] = row1[1]
                row1[1] = row1[0]
                row1[0] = 0
            elif row1[1] == 0:
                row1[2] = row1[0]
                row1[0] = 0
            # call(col1)
    
    elif row1[1]==row1[2]==row1[3] and row1[1] == 0 and row1[0] != 0:
        
        row1[3] = row1[0]
        row1[0] = 0

    elif row1[0]==row1[2]==row1[3] and row1[0] == 0 and row1[1] != 0:
        
        row1[3] = row1[1]
        row1[1] = 0
    
    elif row1[0]==row1[1]==row1[3] and row1[0] == 0 and row1[2] != 0:
        
        row1[3] = row1[2]
        row1[2] = 0
    



    elif row1[0] == row1[2] and row1[2] != 0:
        
        if row1[1] == row1[3] and row1[3] == 0:
            row1[3] = add(row1[0], row1[2])
            row1[0] = 0
            row1[2] = 0

        elif row1[1] == 0 and row1[3] != 0:
            row1[2] =  add(row1[0], row1[2])
            row1[0] = 0
            row1[1] = 0
        
        elif row1[3] == 0 and row1[1] != 0 and row1[1] != row1[0]:
            row1[3] = row1[2]
            row1[2] = row1[1]
            row1[1] = row1[0]
            row1[0] = 0 
    
    elif row1[1] == row1[3]:
        
        if row1[0] == row1[2] and row1[2] == 0:
            row1[3] = add(row1[1], row1[3])
            row1[1] = 0
        elif row1[3] == 0:
            row1[3] = row1[2]
            row1[2] = row1[0]
            row1[0] = 0
        elif row1[2] == 0 and row1[3] != 0:
            row1[3] = add(row1[1], row1[3])
            row1[1] = 0
            row1[2] = row1[0]
            row1[0] = 0

    elif row1[0] == row1[3] and row1[1] == row1[2] and row1[2] == 0:
        
        row1[3] = add(row1[0], row1[3])
        row1[0] = 0

    elif row1[0] != row1[1]:
        
        if row1[2] == row1[3] and row1[3] == 0:
            row1[3] = row1[1]
            row1[2] = row1[0]
            row1[0] = 0
            row1[1] = 0
        
        elif row1[3] != 0 and row1[2] == 0 and row1[1] != 0:
            
            row1[2] = row1[1]
            row1[1] = row1[0]
            row1[0] = 0

        elif row1[3] == 0 and row1[2] != 0:
            
            row1[3] = row1[2]
            row1[2] = row1[1]
            row1[1] = row1[0]
            row1[0] = 0

        elif row1[1] == row1[2] and row1[2] == 0 and row1[3] != 0:
            
            row1[2] = row1[0]
            row1[0] = 0        
        


        elif row1[1] == row1[3] and row1[2] == 0:
            
            row1[3] = add(row1[1], row1[3])
            row1[2] = row1[0]
            row1[1] = row1[0]
            row1[0] = 0
        
    
    if row2[0] == row2[1] and row2[0] != 0:
        
        if row2[2] == 0 and row2[3] == 0:
            
            row2[3] = add(row2[0], row2[1]) 
            row2[0], row2[1], row2[2] = 0, 0, 0
        
        elif row2[2] == 0 and row2[3] != 0:
            
            if row2[1] != row2[3]:
                row2[2] = add(row2[0], row2[1]) 
                row2[0], row2[1] = 0, 0
            elif row2[1] == row2[3]:
                row2[3] = add(row2[1], row2[3])
                row2[2] = row2[0]
                row2[0] = 0
                row2[1] = 0
         
        elif row2[2] == row2[3]:
            
            row2[3] = add(row2[3], row2[2])
            row2[2] = add(row2[0], row2[1])
            row2[0], row2[1] = 0, 0

        
        elif row2[2] != 0 and row2[3] != 0 and row2[1] != row2[2]:
            
            row2[1] = add(row2[0], row2[1]) 
            row2[0] = 0
            # call(col1)
        
        elif row2[1] == row2[2]:
            print("y")

            if row2[3] != 0:
                row2[2] = add(row2[1], row2[1])
                row2[1] = row2[0]
                row2[0] = 0 
            elif row2[3] == 0:
                row2[3] = add(row2[2], row2[1]) 
                row2[2] = row2[0]
                row2[0] = 0
                row2[1] = 0
        
        elif row2[1] != row2[2] and row2[3] == 0:
            row2[3] = row2[2]
            row2[2] = add(row2[1], row2[0])
            row2[1] = 0
            row2[0] = 0

        
    
    elif row2[1] == row2[2] and row2[2] != 0:
        
        if row2[3] == 0:

            row2[3] = add(row2[1], row2[2])
            row2[2] = row2[0]
            row2[0] = 0
            row2[1] = 0
            # call(col1)

        elif row2[3] != 0 and row2[2] != row2[3]:
            row2[2] = add(row2[1], row2[2])
            row2[1] = row2[0]
            row2[0] = 0
            # call(col1)
        
        elif row2[2] == row2[3]:
            row2[3] = add(row2[2], row2[3])
            row2[2] = row2[1]
            if row2[0] != 0:
                row2[1] = row2[0]
                row2[0] = 0
            else:
                row2[1] = 0
            
    
    elif row2[2] == row2[3] and row2[2] != 0:
            
            row2[3] = add(row2[2], row2[3])
            if row2[1] != 0:
                row2[2] = row2[1]
                row2[1] = row2[0]
                row2[0] = 0
            elif row2[1] == 0:
                row2[2] = row2[0]
                row2[0] = 0
            # call(col1)
    
    elif row2[1]==row2[2]==row2[3] and row2[1] == 0 and row2[0] != 0:
        
        row2[3] = row2[0]
        row2[0] = 0

    elif row2[0]==row2[2]==row2[3] and row2[0] == 0 and row2[1] != 0:
        
        row2[3] = row2[1]
        row2[1] = 0
    
    elif row2[0]==row2[1]==row2[3] and row2[0] == 0 and row2[2] != 0:
        
        row2[3] = row2[2]
        row2[2] = 0
    



    elif row2[0] == row2[2] and row2[2] != 0:
        
        if row2[1] == row2[3] and row2[3] == 0:
            row2[3] = add(row2[0], row2[2])
            row2[0] = 0
            row2[2] = 0

        elif row2[1] == 0 and row2[3] != 0:
            row2[2] =  add(row2[0], row2[2])
            row2[0] = 0
            row2[1] = 0
        
        elif row2[3] == 0 and row2[1] != 0 and row2[1] != row2[0]:
            row2[3] = row2[2]
            row2[2] = row2[1]
            row2[1] = row2[0]
            row2[0] = 0 
    
    elif row2[1] == row2[3]:
        
        if row2[0] == row2[2] and row2[2] == 0:
            row2[3] = add(row2[1], row2[3])
            row2[1] = 0
        elif row2[3] == 0:
            row2[3] = row2[2]
            row2[2] = row2[0]
            row2[0] = 0
        elif row2[2] == 0 and row2[3] != 0:
            row2[3] = add(row2[1], row2[3])
            row2[1] = 0
            row2[2] = row2[0]
            row2[0] = 0

    elif row2[0] == row2[3] and row2[1] == row2[2] and row2[2] == 0:
        
        row2[3] = add(row2[0], row2[3])
        row2[0] = 0

    elif row2[0] != row2[1]:
        
        if row2[2] == row2[3] and row2[3] == 0:
            row2[3] = row2[1]
            row2[2] = row2[0]
            row2[0] = 0
            row2[1] = 0
        
        elif row2[3] != 0 and row2[2] == 0 and row2[1] != 0:
            
            row2[2] = row2[1]
            row2[1] = row2[0]
            row2[0] = 0

        elif row2[3] == 0 and row2[2] != 0:
            
            row2[3] = row2[2]
            row2[2] = row2[1]
            row2[1] = row2[0]
            row2[0] = 0

        elif row2[1] == row2[2] and row2[2] == 0 and row2[3] != 0:
            
            row2[2] = row2[0]
            row2[0] = 0        
        


        elif row2[1] == row2[3] and row2[2] == 0:
            
            row2[3] = add(row2[1], row2[3])
            row2[2] = row2[0]
            row2[1] = row2[0]
            row2[0] = 0
        

    # For Row3 

    
    if row3[0] == row3[1] and row3[0] != 0:
        
        if row3[2] == 0 and row3[3] == 0:
            
            row3[3] = add(row3[0], row3[1]) 
            row3[0], row3[1], row3[2] = 0, 0, 0
        
        elif row3[2] == 0 and row3[3] != 0:
            
            if row3[1] != row3[3]:
                row3[2] = add(row3[0], row3[1]) 
                row3[0], row3[1] = 0, 0
            elif row3[1] == row3[3]:
                row3[3] = add(row3[1], row3[3])
                row3[2] = row3[0]
                row3[0] = 0
                row3[1] = 0
         
        elif row3[2] == row3[3]:
            
            row3[3] = add(row3[3], row3[2])
            row3[2] = add(row3[0], row3[1])
            row3[0], row3[1] = 0, 0

        
        elif row3[2] != 0 and row3[3] != 0 and row3[1] != row3[2]:
            
            row3[1] = add(row3[0], row3[1]) 
            row3[0] = 0
            # call(col1)
        
        elif row3[1] == row3[2]:
            print("y")

            if row3[3] != 0:
                row3[2] = add(row3[1], row3[1])
                row3[1] = row3[0]
                row3[0] = 0 
            elif row3[3] == 0:
                row3[3] = add(row3[2], row3[1]) 
                row3[2] = row3[0]
                row3[0] = 0
                row3[1] = 0
        
        elif row3[1] != row3[2] and row3[3] == 0:
            row3[3] = row3[2]
            row3[2] = add(row3[1], row3[0])
            row3[1] = 0
            row3[0] = 0

        
    
    elif row3[1] == row3[2] and row3[2] != 0:
        
        if row3[3] == 0:

            row3[3] = add(row3[1], row3[2])
            row3[2] = row3[0]
            row3[0] = 0
            row3[1] = 0
            # call(col1)

        elif row3[3] != 0 and row3[2] != row3[3]:
            row3[2] = add(row3[1], row3[2])
            row3[1] = row3[0]
            row3[0] = 0
            # call(col1)
        
        elif row3[2] == row3[3]:
            row3[3] = add(row3[2], row3[3])
            row3[2] = row3[1]
            if row3[0] != 0:
                row3[1] = row3[0]
                row3[0] = 0
            else:
                row3[1] = 0
            
    
    elif row3[2] == row3[3] and row3[2] != 0:
            
            row3[3] = add(row3[2], row3[3])
            if row3[1] != 0:
                row3[2] = row3[1]
                row3[1] = row3[0]
                row3[0] = 0
            elif row3[1] == 0:
                row3[2] = row3[0]
                row3[0] = 0
            # call(col1)
    
    elif row3[1]==row3[2]==row3[3] and row3[1] == 0 and row3[0] != 0:
        
        row3[3] = row3[0]
        row3[0] = 0

    elif row3[0]==row3[2]==row3[3] and row3[0] == 0 and row3[1] != 0:
        
        row3[3] = row3[1]
        row3[1] = 0
    
    elif row3[0]==row3[1]==row3[3] and row3[0] == 0 and row3[2] != 0:
        
        row3[3] = row3[2]
        row3[2] = 0
    



    elif row3[0] == row3[2] and row3[2] != 0:
        
        if row3[1] == row3[3] and row3[3] == 0:
            row3[3] = add(row3[0], row3[2])
            row3[0] = 0
            row3[2] = 0

        elif row3[1] == 0 and row3[3] != 0:
            row3[2] =  add(row3[0], row3[2])
            row3[0] = 0
            row3[1] = 0
        
        elif row3[3] == 0 and row3[1] != 0 and row3[1] != row3[0]:
            row3[3] = row3[2]
            row3[2] = row3[1]
            row3[1] = row3[0]
            row3[0] = 0 
    
    elif row3[1] == row3[3]:
        
        if row3[0] == row3[2] and row3[2] == 0:
            row3[3] = add(row3[1], row3[3])
            row3[1] = 0
        elif row3[3] == 0:
            row3[3] = row3[2]
            row3[2] = row3[0]
            row3[0] = 0
        elif row3[2] == 0 and row3[3] != 0:
            row3[3] = add(row3[1], row3[3])
            row3[1] = 0
            row3[2] = row3[0]
            row3[0] = 0

    elif row3[0] == row3[3] and row3[1] == row3[2] and row3[2] == 0:
        
        row3[3] = add(row3[0], row3[3])
        row3[0] = 0

    elif row3[0] != row3[1]:
        
        if row3[2] == row3[3] and row3[3] == 0:
            row3[3] = row3[1]
            row3[2] = row3[0]
            row3[0] = 0
            row3[1] = 0
        
        elif row3[3] != 0 and row3[2] == 0 and row3[1] != 0:
            
            row3[2] = row3[1]
            row3[1] = row3[0]
            row3[0] = 0

        elif row3[3] == 0 and row3[2] != 0:
            
            row3[3] = row3[2]
            row3[2] = row3[1]
            row3[1] = row3[0]
            row3[0] = 0

        elif row3[1] == row3[2] and row3[2] == 0 and row3[3] != 0:
            
            row3[2] = row3[0]
            row3[0] = 0        
        


        elif row3[1] == row3[3] and row3[2] == 0:
            
            row3[3] = add(row3[1], row3[3])
            row3[2] = row3[0]
            row3[1] = row3[0]
            row3[0] = 0
        

    # For row4

    
    if row4[0] == row4[1] and row4[0] != 0:
        
        if row4[2] == 0 and row4[3] == 0:
            
            row4[3] = add(row4[0], row4[1]) 
            row4[0], row4[1], row4[2] = 0, 0, 0
        
        elif row4[2] == 0 and row4[3] != 0:
            
            if row4[1] != row4[3]:
                row4[2] = add(row4[0], row4[1]) 
                row4[0], row4[1] = 0, 0
            elif row4[1] == row4[3]:
                row4[3] = add(row4[1], row4[3])
                row4[2] = row4[0]
                row4[0] = 0
                row4[1] = 0
         
        elif row4[2] == row4[3]:
            
            row4[3] = add(row4[3], row4[2])
            row4[2] = add(row4[0], row4[1])
            row4[0], row4[1] = 0, 0

        
        elif row4[2] != 0 and row4[3] != 0 and row4[1] != row4[2]:
            
            row4[1] = add(row4[0], row4[1]) 
            row4[0] = 0
            # call(col1)
        
        elif row4[1] == row4[2]:
            print("y")

            if row4[3] != 0:
                row4[2] = add(row4[1], row4[1])
                row4[1] = row4[0]
                row4[0] = 0 
            elif row4[3] == 0:
                row4[3] = add(row4[2], row4[1]) 
                row4[2] = row4[0]
                row4[0] = 0
                row4[1] = 0
        
        elif row4[1] != row4[2] and row4[3] == 0:
            row4[3] = row4[2]
            row4[2] = add(row4[1], row4[0])
            row4[1] = 0
            row4[0] = 0

        
    
    elif row4[1] == row4[2] and row4[2] != 0:
        
        if row4[3] == 0:

            row4[3] = add(row4[1], row4[2])
            row4[2] = row4[0]
            row4[0] = 0
            row4[1] = 0
            # call(col1)

        elif row4[3] != 0 and row4[2] != row4[3]:
            row4[2] = add(row4[1], row4[2])
            row4[1] = row4[0]
            row4[0] = 0
            # call(col1)
        
        elif row4[2] == row4[3]:
            row4[3] = add(row4[2], row4[3])
            row4[2] = row4[1]
            if row4[0] != 0:
                row4[1] = row4[0]
                row4[0] = 0
            else:
                row4[1] = 0
            
    
    elif row4[2] == row4[3] and row4[2] != 0:
            
            row4[3] = add(row4[2], row4[3])
            if row4[1] != 0:
                row4[2] = row4[1]
                row4[1] = row4[0]
                row4[0] = 0
            elif row4[1] == 0:
                row4[2] = row4[0]
                row4[0] = 0
            # call(col1)
    
    elif row4[1]==row4[2]==row4[3] and row4[1] == 0 and row4[0] != 0:
        
        row4[3] = row4[0]
        row4[0] = 0

    elif row4[0]==row4[2]==row4[3] and row4[0] == 0 and row4[1] != 0:
        
        row4[3] = row4[1]
        row4[1] = 0
    
    elif row4[0]==row4[1]==row4[3] and row4[0] == 0 and row4[2] != 0:
        
        row4[3] = row4[2]
        row4[2] = 0
    



    elif row4[0] == row4[2] and row4[2] != 0:
        
        if row4[1] == row4[3] and row4[3] == 0:
            row4[3] = add(row4[0], row4[2])
            row4[0] = 0
            row4[2] = 0

        elif row4[1] == 0 and row4[3] != 0:
            row4[2] =  add(row4[0], row4[2])
            row4[0] = 0
            row4[1] = 0
        
        elif row4[3] == 0 and row4[1] != 0 and row4[1] != row4[0]:
            row4[3] = row4[2]
            row4[2] = row4[1]
            row4[1] = row4[0]
            row4[0] = 0 
    
    elif row4[1] == row4[3]:
        
        if row4[0] == row4[2] and row4[2] == 0:
            row4[3] = add(row4[1], row4[3])
            row4[1] = 0
        elif row4[3] == 0:
            row4[3] = row4[2]
            row4[2] = row4[0]
            row4[0] = 0
        elif row4[2] == 0 and row4[3] != 0:
            row4[3] = add(row4[1], row4[3])
            row4[1] = 0
            row4[2] = row4[0]
            row4[0] = 0

    elif row4[0] == row4[3] and row4[1] == row4[2] and row4[2] == 0:
        
        row4[3] = add(row4[0], row4[3])
        row4[0] = 0

    elif row4[0] != row4[1]:
        
        if row4[2] == row4[3] and row4[3] == 0:
            row4[3] = row4[1]
            row4[2] = row4[0]
            row4[0] = 0
            row4[1] = 0
        
        elif row4[3] != 0 and row4[2] == 0 and row4[1] != 0:
            
            row4[2] = row4[1]
            row4[1] = row4[0]
            row4[0] = 0

        elif row4[3] == 0 and row4[2] != 0:
            
            row4[3] = row4[2]
            row4[2] = row4[1]
            row4[1] = row4[0]
            row4[0] = 0

        elif row4[1] == row4[2] and row4[2] == 0 and row4[3] != 0:
            
            row4[2] = row4[0]
            row4[0] = 0        
        


        elif row4[1] == row4[3] and row4[2] == 0:
            
            row4[3] = add(row4[1], row4[3])
            row4[2] = row4[0]
            row4[1] = row4[0]
            row4[0] = 0
        


def left():
     
    # For Row 1

    if row1[3] == row1[2] and row1[3] != 0:
        
        if row1[1] == 0 and row1[0] == 0:
            
            row1[0] = add(row1[3], row1[2]) 
            row1[3], row1[2], row1[1] = 0, 0, 0
        
        elif row1[1] == 0 and row1[0] != 0:
            
            if row1[2] != row1[0]:
                row1[1] = add(row1[3], row1[2]) 
                row1[3], row1[2] = 0, 0
            elif row1[2] == row1[0]:
                row1[0] = add(row1[2], row1[0])
                row1[1] = row1[3]
                row1[3] = 0
                row1[2] = 0
         
        elif row1[1] == row1[0]:
            
            row1[0] = add(row1[0], row1[1])
            row1[1] = add(row1[3], row1[2])
            row1[3], row1[2] = 0, 0

        
        elif row1[1] != 0 and row1[0] != 0 and row1[2] != row1[1]:
            
            row1[2] = add(row1[3], row1[2]) 
            row1[3] = 0
            # call(col1)
        
        elif row1[2] == row1[1]:
            print("y")

            if row1[0] != 0:
                row1[1] = add(row1[2], row1[2])
                row1[2] = row1[3]
                row1[3] = 0 
            elif row1[0] == 0:
                row1[0] = add(row1[1], row1[2]) 
                row1[1] = row1[3]
                row1[3] = 0
                row1[2] = 0
        
        elif row1[2] != row1[1] and row1[0] == 0:
            row1[0] = row1[1]
            row1[1] = add(row1[2], row1[3])
            row1[2] = 0
            row1[3] = 0

        
    
    elif row1[2] == row1[1] and row1[1] != 0:
        
        if row1[0] == 0:

            row1[0] = add(row1[2], row1[1])
            row1[1] = row1[3]
            row1[3] = 0
            row1[2] = 0
            # call(col1)

        elif row1[0] != 0 and row1[1] != row1[0]:
            row1[1] = add(row1[2], row1[1])
            row1[2] = row1[3]
            row1[3] = 0
            # call(col1)
        
        elif row1[1] == row1[0]:
            row1[0] = add(row1[1], row1[0])
            row1[1] = row1[2]
            if row1[3] != 0:
                row1[2] = row1[3]
                row1[3] = 0
            else:
                row1[2] = 0
            
    
    elif row1[1] == row1[0] and row1[1] != 0:
            
            row1[0] = add(row1[1], row1[0])
            if row1[2] != 0:
                row1[1] = row1[2]
                row1[2] = row1[3]
                row1[3] = 0
            elif row1[2] == 0:
                row1[1] = row1[3]
                row1[3] = 0
            # call(col1)
    
    elif row1[2]==row1[1]==row1[0] and row1[2] == 0 and row1[3] != 0:
        
        row1[0] = row1[3]
        row1[3] = 0

    elif row1[3]==row1[1]==row1[0] and row1[3] == 0 and row1[2] != 0:
        
        row1[0] = row1[2]
        row1[2] = 0
    
    elif row1[3]==row1[2]==row1[0] and row1[3] == 0 and row1[1] != 0:
        
        row1[0] = row1[1]
        row1[1] = 0
    



    elif row1[3] == row1[1] and row1[1] != 0:
        
        if row1[2] == row1[0] and row1[0] == 0:
            row1[0] = add(row1[3], row1[1])
            row1[3] = 0
            row1[1] = 0

        elif row1[2] == 0 and row1[0] != 0:
            row1[1] =  add(row1[3], row1[1])
            row1[3] = 0
            row1[2] = 0
        
        elif row1[0] == 0 and row1[2] != 0 and row1[2] != row1[3]:
            row1[0] = row1[1]
            row1[1] = row1[2]
            row1[2] = row1[3]
            row1[3] = 0 
    
    elif row1[2] == row1[0]:
        
        if row1[3] == row1[1] and row1[1] == 0:
            row1[0] = add(row1[2], row1[0])
            row1[2] = 0
        elif row1[0] == 0:
            row1[0] = row1[1]
            row1[1] = row1[3]
            row1[3] = 0
        elif row1[1] == 0 and row1[0] != 0:
            row1[0] = add(row1[2], row1[0])
            row1[2] = 0
            row1[1] = row1[3]
            row1[3] = 0

    elif row1[3] == row1[0] and row1[2] == row1[1] and row1[1] == 0:
        
        row1[0] = add(row1[3], row1[0])
        row1[3] = 0

    elif row1[3] != row1[2]:
        
        if row1[1] == row1[0] and row1[0] == 0:
            row1[0] = row1[2]
            row1[1] = row1[3]
            row1[3] = 0
            row1[2] = 0
        
        elif row1[0] != 0 and row1[1] == 0 and row1[2] != 0:
            
            row1[1] = row1[2]
            row1[2] = row1[3]
            row1[3] = 0

        elif row1[0] == 0 and row1[1] != 0:
            
            row1[0] = row1[1]
            row1[1] = row1[2]
            row1[2] = row1[3]
            row1[3] = 0

        elif row1[2] == row1[1] and row1[1] == 0 and row1[0] != 0:
            
            row1[1] = row1[3]
            row1[3] = 0        
        


        elif row1[2] == row1[0] and row1[1] == 0:
            
            row1[0] = add(row1[2], row1[0])
            row1[1] = row1[3]
            row1[2] = row1[3]
            row1[3] = 0
        
    
    if row2[3] == row2[2] and row2[3] != 0:
        
        if row2[1] == 0 and row2[0] == 0:
            
            row2[0] = add(row2[3], row2[2]) 
            row2[3], row2[2], row2[1] = 0, 0, 0
        
        elif row2[1] == 0 and row2[0] != 0:
            
            if row2[2] != row2[0]:
                row2[1] = add(row2[3], row2[2]) 
                row2[3], row2[2] = 0, 0
            elif row2[2] == row2[0]:
                row2[0] = add(row2[2], row2[0])
                row2[1] = row2[3]
                row2[3] = 0
                row2[2] = 0
         
        elif row2[1] == row2[0]:
            
            row2[0] = add(row2[0], row2[1])
            row2[1] = add(row2[3], row2[2])
            row2[3], row2[2] = 0, 0

        
        elif row2[1] != 0 and row2[0] != 0 and row2[2] != row2[1]:
            
            row2[2] = add(row2[3], row2[2]) 
            row2[3] = 0
            # call(col1)
        
        elif row2[2] == row2[1]:
            print("y")

            if row2[0] != 0:
                row2[1] = add(row2[2], row2[2])
                row2[2] = row2[3]
                row2[3] = 0 
            elif row2[0] == 0:
                row2[0] = add(row2[1], row2[2]) 
                row2[1] = row2[3]
                row2[3] = 0
                row2[2] = 0
        
        elif row2[2] != row2[1] and row2[0] == 0:
            row2[0] = row2[1]
            row2[1] = add(row2[2], row2[3])
            row2[2] = 0
            row2[3] = 0

        
    
    elif row2[2] == row2[1] and row2[1] != 0:
        
        if row2[0] == 0:

            row2[0] = add(row2[2], row2[1])
            row2[1] = row2[3]
            row2[3] = 0
            row2[2] = 0
            # call(col1)

        elif row2[0] != 0 and row2[1] != row2[0]:
            row2[1] = add(row2[2], row2[1])
            row2[2] = row2[3]
            row2[3] = 0
            # call(col1)
        
        elif row2[1] == row2[0]:
            row2[0] = add(row2[1], row2[0])
            row2[1] = row2[2]
            if row2[3] != 0:
                row2[2] = row2[3]
                row2[3] = 0
            else:
                row2[2] = 0
            
    
    elif row2[1] == row2[0] and row2[1] != 0:
            
            row2[0] = add(row2[1], row2[0])
            if row2[2] != 0:
                row2[1] = row2[2]
                row2[2] = row2[3]
                row2[3] = 0
            elif row2[2] == 0:
                row2[1] = row2[3]
                row2[3] = 0
            # call(col1)
    
    elif row2[2]==row2[1]==row2[0] and row2[2] == 0 and row2[3] != 0:
        
        row2[0] = row2[3]
        row2[3] = 0

    elif row2[3]==row2[1]==row2[0] and row2[3] == 0 and row2[2] != 0:
        
        row2[0] = row2[2]
        row2[2] = 0
    
    elif row2[3]==row2[2]==row2[0] and row2[3] == 0 and row2[1] != 0:
        
        row2[0] = row2[1]
        row2[1] = 0
    



    elif row2[3] == row2[1] and row2[1] != 0:
        
        if row2[2] == row2[0] and row2[0] == 0:
            row2[0] = add(row2[3], row2[1])
            row2[3] = 0
            row2[1] = 0

        elif row2[2] == 0 and row2[0] != 0:
            row2[1] =  add(row2[3], row2[1])
            row2[3] = 0
            row2[2] = 0
        
        elif row2[0] == 0 and row2[2] != 0 and row2[2] != row2[3]:
            row2[0] = row2[1]
            row2[1] = row2[2]
            row2[2] = row2[3]
            row2[3] = 0 
    
    elif row2[2] == row2[0]:
        
        if row2[3] == row2[1] and row2[1] == 0:
            row2[0] = add(row2[2], row2[0])
            row2[2] = 0
        elif row2[0] == 0:
            row2[0] = row2[1]
            row2[1] = row2[3]
            row2[3] = 0
        elif row2[1] == 0 and row2[0] != 0:
            row2[0] = add(row2[2], row2[0])
            row2[2] = 0
            row2[1] = row2[3]
            row2[3] = 0

    elif row2[3] == row2[0] and row2[2] == row2[1] and row2[1] == 0:
        
        row2[0] = add(row2[3], row2[0])
        row2[3] = 0

    elif row2[3] != row2[2]:
        
        if row2[1] == row2[0] and row2[0] == 0:
            row2[0] = row2[2]
            row2[1] = row2[3]
            row2[3] = 0
            row2[2] = 0
        
        elif row2[0] != 0 and row2[1] == 0 and row2[2] != 0:
            
            row2[1] = row2[2]
            row2[2] = row2[3]
            row2[3] = 0

        elif row2[0] == 0 and row2[1] != 0:
            
            row2[0] = row2[1]
            row2[1] = row2[2]
            row2[2] = row2[3]
            row2[3] = 0

        elif row2[2] == row2[1] and row2[1] == 0 and row2[0] != 0:
            
            row2[1] = row2[3]
            row2[3] = 0        
        


        elif row2[2] == row2[0] and row2[1] == 0:
            
            row2[0] = add(row2[2], row2[0])
            row2[1] = row2[3]
            row2[2] = row2[3]
            row2[3] = 0
        

    # For Row3 

    
    if row3[3] == row3[2] and row3[3] != 0:
        
        if row3[1] == 0 and row3[0] == 0:
            
            row3[0] = add(row3[3], row3[2]) 
            row3[3], row3[2], row3[1] = 0, 0, 0
        
        elif row3[1] == 0 and row3[0] != 0:
            
            if row3[2] != row3[0]:
                row3[1] = add(row3[3], row3[2]) 
                row3[3], row3[2] = 0, 0
            elif row3[2] == row3[0]:
                row3[0] = add(row3[2], row3[0])
                row3[1] = row3[3]
                row3[3] = 0
                row3[2] = 0
         
        elif row3[1] == row3[0]:
            
            row3[0] = add(row3[0], row3[1])
            row3[1] = add(row3[3], row3[2])
            row3[3], row3[2] = 0, 0

        
        elif row3[1] != 0 and row3[0] != 0 and row3[2] != row3[1]:
            
            row3[2] = add(row3[3], row3[2]) 
            row3[3] = 0
            # call(col1)
        
        elif row3[2] == row3[1]:
            print("y")

            if row3[0] != 0:
                row3[1] = add(row3[2], row3[2])
                row3[2] = row3[3]
                row3[3] = 0 
            elif row3[0] == 0:
                row3[0] = add(row3[1], row3[2]) 
                row3[1] = row3[3]
                row3[3] = 0
                row3[2] = 0
        
        elif row3[2] != row3[1] and row3[0] == 0:
            row3[0] = row3[1]
            row3[1] = add(row3[2], row3[3])
            row3[2] = 0
            row3[3] = 0

        
    
    elif row3[2] == row3[1] and row3[1] != 0:
        
        if row3[0] == 0:

            row3[0] = add(row3[2], row3[1])
            row3[1] = row3[3]
            row3[3] = 0
            row3[2] = 0
            # call(col1)

        elif row3[0] != 0 and row3[1] != row3[0]:
            row3[1] = add(row3[2], row3[1])
            row3[2] = row3[3]
            row3[3] = 0
            # call(col1)
        
        elif row3[1] == row3[0]:
            row3[0] = add(row3[1], row3[0])
            row3[1] = row3[2]
            if row3[3] != 0:
                row3[2] = row3[3]
                row3[3] = 0
            else:
                row3[2] = 0
            
    
    elif row3[1] == row3[0] and row3[1] != 0:
            
            row3[0] = add(row3[1], row3[0])
            if row3[2] != 0:
                row3[1] = row3[2]
                row3[2] = row3[3]
                row3[3] = 0
            elif row3[2] == 0:
                row3[1] = row3[3]
                row3[3] = 0
            # call(col1)
    
    elif row3[2]==row3[1]==row3[0] and row3[2] == 0 and row3[3] != 0:
        
        row3[0] = row3[3]
        row3[3] = 0

    elif row3[3]==row3[1]==row3[0] and row3[3] == 0 and row3[2] != 0:
        
        row3[0] = row3[2]
        row3[2] = 0
    
    elif row3[3]==row3[2]==row3[0] and row3[3] == 0 and row3[1] != 0:
        
        row3[0] = row3[1]
        row3[1] = 0
    



    elif row3[3] == row3[1] and row3[1] != 0:
        
        if row3[2] == row3[0] and row3[0] == 0:
            row3[0] = add(row3[3], row3[1])
            row3[3] = 0
            row3[1] = 0

        elif row3[2] == 0 and row3[0] != 0:
            row3[1] =  add(row3[3], row3[1])
            row3[3] = 0
            row3[2] = 0
        
        elif row3[0] == 0 and row3[2] != 0 and row3[2] != row3[3]:
            row3[0] = row3[1]
            row3[1] = row3[2]
            row3[2] = row3[3]
            row3[3] = 0 
    
    elif row3[2] == row3[0]:
        
        if row3[3] == row3[1] and row3[1] == 0:
            row3[0] = add(row3[2], row3[0])
            row3[2] = 0
        elif row3[0] == 0:
            row3[0] = row3[1]
            row3[1] = row3[3]
            row3[3] = 0
        elif row3[1] == 0 and row3[0] != 0:
            row3[0] = add(row3[2], row3[0])
            row3[2] = 0
            row3[1] = row3[3]
            row3[3] = 0

    elif row3[3] == row3[0] and row3[2] == row3[1] and row3[1] == 0:
        
        row3[0] = add(row3[3], row3[0])
        row3[3] = 0

    elif row3[3] != row3[2]:
        
        if row3[1] == row3[0] and row3[0] == 0:
            row3[0] = row3[2]
            row3[1] = row3[3]
            row3[3] = 0
            row3[2] = 0
        
        elif row3[0] != 0 and row3[1] == 0 and row3[2] != 0:
            
            row3[1] = row3[2]
            row3[2] = row3[3]
            row3[3] = 0

        elif row3[0] == 0 and row3[1] != 0:
            
            row3[0] = row3[1]
            row3[1] = row3[2]
            row3[2] = row3[3]
            row3[3] = 0

        elif row3[2] == row3[1] and row3[1] == 0 and row3[0] != 0:
            
            row3[1] = row3[3]
            row3[3] = 0        
        


        elif row3[2] == row3[0] and row3[1] == 0:
            
            row3[0] = add(row3[2], row3[0])
            row3[1] = row3[3]
            row3[2] = row3[3]
            row3[3] = 0
        

    # For row4

    
    if row4[3] == row4[2] and row4[3] != 0:
        
        if row4[1] == 0 and row4[0] == 0:
            
            row4[0] = add(row4[3], row4[2]) 
            row4[3], row4[2], row4[1] = 0, 0, 0
        
        elif row4[1] == 0 and row4[0] != 0:
            
            if row4[2] != row4[0]:
                row4[1] = add(row4[3], row4[2]) 
                row4[3], row4[2] = 0, 0
            elif row4[2] == row4[0]:
                row4[0] = add(row4[2], row4[0])
                row4[1] = row4[3]
                row4[3] = 0
                row4[2] = 0
         
        elif row4[1] == row4[0]:
            
            row4[0] = add(row4[0], row4[1])
            row4[1] = add(row4[3], row4[2])
            row4[3], row4[2] = 0, 0

        
        elif row4[1] != 0 and row4[0] != 0 and row4[2] != row4[1]:
            
            row4[2] = add(row4[3], row4[2]) 
            row4[3] = 0
            # call(col1)
        
        elif row4[2] == row4[1]:
            print("y")

            if row4[0] != 0:
                row4[1] = add(row4[2], row4[2])
                row4[2] = row4[3]
                row4[3] = 0 
            elif row4[0] == 0:
                row4[0] = add(row4[1], row4[2]) 
                row4[1] = row4[3]
                row4[3] = 0
                row4[2] = 0
        
        elif row4[2] != row4[1] and row4[0] == 0:
            row4[0] = row4[1]
            row4[1] = add(row4[2], row4[3])
            row4[2] = 0
            row4[3] = 0

        
    
    elif row4[2] == row4[1] and row4[1] != 0:
        
        if row4[0] == 0:

            row4[0] = add(row4[2], row4[1])
            row4[1] = row4[3]
            row4[3] = 0
            row4[2] = 0
            # call(col1)

        elif row4[0] != 0 and row4[1] != row4[0]:
            row4[1] = add(row4[2], row4[1])
            row4[2] = row4[3]
            row4[3] = 0
            # call(col1)
        
        elif row4[1] == row4[0]:
            row4[0] = add(row4[1], row4[0])
            row4[1] = row4[2]
            if row4[3] != 0:
                row4[2] = row4[3]
                row4[3] = 0
            else:
                row4[2] = 0
            
    
    elif row4[1] == row4[0] and row4[1] != 0:
            
            row4[0] = add(row4[1], row4[0])
            if row4[2] != 0:
                row4[1] = row4[2]
                row4[2] = row4[3]
                row4[3] = 0
            elif row4[2] == 0:
                row4[1] = row4[3]
                row4[3] = 0
            # call(col1)
    
    elif row4[2]==row4[1]==row4[0] and row4[2] == 0 and row4[3] != 0:
        
        row4[0] = row4[3]
        row4[3] = 0

    elif row4[3]==row4[1]==row4[0] and row4[3] == 0 and row4[2] != 0:
        
        row4[0] = row4[2]
        row4[2] = 0
    
    elif row4[3]==row4[2]==row4[0] and row4[3] == 0 and row4[1] != 0:
        
        row4[0] = row4[1]
        row4[1] = 0
    



    elif row4[3] == row4[1] and row4[1] != 0:
        
        if row4[2] == row4[0] and row4[0] == 0:
            row4[0] = add(row4[3], row4[1])
            row4[3] = 0
            row4[1] = 0

        elif row4[2] == 0 and row4[0] != 0:
            row4[1] =  add(row4[3], row4[1])
            row4[3] = 0
            row4[2] = 0
        
        elif row4[0] == 0 and row4[2] != 0 and row4[2] != row4[3]:
            row4[0] = row4[1]
            row4[1] = row4[2]
            row4[2] = row4[3]
            row4[3] = 0 
    
    elif row4[2] == row4[0]:
        
        if row4[3] == row4[1] and row4[1] == 0:
            row4[0] = add(row4[2], row4[0])
            row4[2] = 0
        elif row4[0] == 0:
            row4[0] = row4[1]
            row4[1] = row4[3]
            row4[3] = 0
        elif row4[1] == 0 and row4[0] != 0:
            row4[0] = add(row4[2], row4[0])
            row4[2] = 0
            row4[1] = row4[3]
            row4[3] = 0

    elif row4[3] == row4[0] and row4[2] == row4[1] and row4[1] == 0:
        
        row4[0] = add(row4[3], row4[0])
        row4[3] = 0

    elif row4[3] != row4[2]:
        
        if row4[1] == row4[0] and row4[0] == 0:
            row4[0] = row4[2]
            row4[1] = row4[3]
            row4[3] = 0
            row4[2] = 0
        
        elif row4[0] != 0 and row4[1] == 0 and row4[2] != 0:
            
            row4[1] = row4[2]
            row4[2] = row4[3]
            row4[3] = 0

        elif row4[0] == 0 and row4[1] != 0:
            
            row4[0] = row4[1]
            row4[1] = row4[2]
            row4[2] = row4[3]
            row4[3] = 0

        elif row4[2] == row4[1] and row4[1] == 0 and row4[0] != 0:
            
            row4[1] = row4[3]
            row4[3] = 0        
        


        elif row4[2] == row4[0] and row4[1] == 0:
            
            row4[0] = add(row4[2], row4[0])
            row4[1] = row4[3]
            row4[2] = row4[3]
            row4[3] = 0
    

def on_press(key):
     
    if key == Key.up: # or key == Key.up :
        print('\033[2J') 
        up()
        row()
        print("\nScore:", scr)
    


    elif key == Key.down: # or key == Key.down:
        print('\033[2J')
        down()
        row()
        print("\nScore:", scr)
        

    
    elif key == Key.left: # or key == Key.left:
        print('\033[2J')
        left()
        row()
        print("\nScore:", scr)
    

    elif key == Key.right: # or key == Key.right:
        print('\033[2J')
        right()
        row()
        print("\nScore:", scr)
    
    elif key == Key.esc:
        return False

        
with Listener(on_press = on_press) as listener:
    listener.join()

