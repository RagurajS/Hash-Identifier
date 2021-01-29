print("***This is the alpha version of Hash Identifier by Ragu, Maynot differentiate Hash types efficiently...***")
hash = input("\nEnter the Hash to identify: ")

nums = []
chars = []
bit = 0

for i in hash:
  if (i.isdigit() == True):
    bit = bit+4
    nums.append(i)
  else:
    bit = bit+1
    chars.append(i)

if (len(hash)==4):
  print("\nThis is CRC-16 Hashing Algorithm.")
if (len(hash)==8):
  print("\nThis is CRC-32 Hashing Algorithm.")
if (len(hash)==32):
  print("\nThis is MD5 Hashing Algorithm.")
elif (len(hash) == 40):
  print("\nThis is SHA1 Hashing Algorithm.")
elif (len(hash)==64):
  print("\nThis is SHA2-256 Hashing Algorithm.")
elif (len(hash)==96):
  print("\nThis is SHA2-384 Hashing Algorithm.")
elif (len(hash)==128):
  print("\nThis is SHA2-512 Hashing Algorithm.")
elif (len(hash) == 60 and hash[:2] == "$1" or hash[:2] == "$2"):
  print("\nThis is BCrypt Hashing Algorithm.")
elif (len(hash) == 34 and hash[:2] == "$1"):
  print("\nThis is MD5-Crypt Hashing Algorithm.")
elif (len(hash) == 56):
  print("\nThis is Keccak-224 Hashing Algorithm.")
else:
  print("\nCannot map to acquired data/ Unknown Hashing Algorithm.")
  
print("Length of given Hash is: ", len(hash))
print("Bit size is: ", (len(hash)*4),  "(Remember Bit size may vary if hash is salted or 'B'-type algorithms)")
print("Total size of Hash: "+str(bit), "(calculated by char = 1 byte, int = 4 byte)")
print("Length of numbers: ", len(''.join(nums)))
print("Length of characters: "+str(len(''.join(chars))))
print("Nums = "+str(nums))
print("Chars = "+str(chars), "\n")
