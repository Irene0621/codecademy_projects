#!/usr/bin/env python
# coding: utf-8

# In[12]:


"""Caesar Cipher codecademy project: the program consist on two functions in the first one the input is an encoded message and the output 
is a decoded message. The second one the input is a decoded message and the output is a coded message"""

#encoded_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"


offset = 10 #number of letters to shift 

decoded_message = []
abecedary = "abcdefghijklmnopqrstuvwxyz" #26 letters 0-25

def decoding_message(encoded_message, offset):
  for character in encoded_message:
    if character in abecedary:
      find_index = abecedary.find(character)
      index_decoded= (find_index + offset)%26

      decoded_message.append(abecedary[index_decoded])

    else:
      decoded_message.append(character)
  x= ''.join(decoded_message)
  print("The decoded message is: " + str(x))

decoding_message(encoded_message, offset)

#funcion para codificar mensaje 

decoded_message = "Alice is the spy"

offset = 10 

encoded_message = []
abecedary = "abcdefghijklmnopqrstuvwxyz" #26 caracteres 0-25
def coding_message(decoded_message, offset):
  for character in decoded_message:
    if character in abecedary:
      find_index = abecedary.find(character)
      index_decoded= (find_index - offset)%26

      encoded_message.append(abecedary[index_decoded])

    else:
      encoded_message.append(character)
  x= ''.join(encoded_message)
  print("The encoded message is: " + str(x))

coding_message(decoded_message, offset)





# In[ ]:




