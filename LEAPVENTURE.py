
# coding: utf-8

# In[19]:


def HextoDec (string):
    decimal = 0
    
    #i = index, d = letter/num of hex
    #in enumerate(string) just means to go through each char of the string 
    for i,d in enumerate(string) : 
        #hex string
        hex = "0123456789ABCDEF"
        
        value= hex.index(d) # 0 to 15
        
        
        #index = string.index(i)
        power = (len(string) -(i+1)) #power of 16
        decimal += (value*16**power)
    return decimal




def BintoDec (string):
    deciaml = 0
    for index, value in enumerate(string[::-1]):
        deciaml += int(value) * 2**index    
    return deciaml 

HextoDec("FFF")
BintoDec("111")

