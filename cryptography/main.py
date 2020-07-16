# acceptable characters string
alph = 'abcdefghijklmnopqrstuvwxyz`~1!2@3#4$5%6^7&8*9(0)-_=+[{]}\|;:\'",<.>/? '

# encryption/decryption divergence line 48-53
path = (str(input('Encryption or Decryption?(e/d) '))).lower()

# safety to prevent invalid input
if path != 'e' and path != 'd':
  print('Invalid Input.')
  exit()

# encryption/decryption key
key = str(input('Enter key: '))

# message to be encrypted or encrypted message
msg = str(input('Message to be encrypted/decrypted: '))

# to preserve whitespaces
key = list(key.lower())

# assigns appropriate value to each character based on position in
# alph string on line 2
key_l = []
for char in key:
    if char in alph:
      key_l.append(alph.index(char))

# to preserve whitespaces
msg = list(msg.lower())

# assigns appropriate value to each character based on position in
# alph string on line 2
msg_l = []
for char in msg:
    if char in alph:
        msg_l.append(alph.index(char))

# for iterating through key_l
counter = 0

# encryption/decryption loop
for i in range(len(msg_l)):
    
    # to return to first element in key_l in case message is longer
    # than key
    var = counter % len(key_l)
    
    # encryption/decryption specific code begins
    if path == 'e':
        msg_l[i] += (key_l[var])
    else:
        msg_l[i] -= (key_l[var])
    # encryption/decryption specific code ends
      
    # to start from beginning of alph in case index is out of range
    # can happen only in case of encryption (positive indices)
    if msg_l[i] >= 0:
        msg_l[i] = alph[msg_l[i] % (len(alph))]
    
    # may give negative indices. no changes necessary
    # negative numbers => index from other end
    else:
        msg_l[i] = alph[msg_l[i]]

    # so cursor switches to next element in key_l    
    counter += 1

# prints out encrypted/decrypted message
print('Output:', ''.join(msg_l))

# Footnotes: 
# 1. Changes required in lines 2, 19 and 29 while making the whole
# process case sensitive.
# 2. alph string needs to have elements in same order when decrypting
# on another system.