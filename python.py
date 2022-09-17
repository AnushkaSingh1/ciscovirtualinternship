# Programming Python Problem Statement 
import socket
#To Check if ip address is valid
ipa = input()
try:
    socket.inet_aton(ipa)
    print("Valid IP")
except socket.error:
    print("Invalid IP")
 
 #To print ip address  in decimal, hexadecimal, binary, octal
 try:
    socket.inet_aton(ipa)
   print(ipa)
parts = ipa.split('.')
print()

for part in parts:
  #  print(part)
    
    print()
   
    for part in parts:
        hexNumber= format(int(parts[0]), '02x'), \
                + (format(int(parts[1]), '02x'), \
                + (format(int(parts[2]), '02x'), \
                + (format(int(parts[3]), '02x')
     
     with open("conversion.txt", "h") as external_file:
              print("IP Address in HEX base 16")
              print("0x" +hexNumber, file=external_file)
          print()
          external_file.close()

for part in parts:
hex2 += format(int(part),'02x')
with open("conversion.txt", "d") as external_file:
print('IP Address in Decimal')
print(int (hex2, base=16), file=external_file)
external_file.close()

 binaryNumber= \
         format(int(parts[0]),   '08b'), \
        + (format(int(parts[1]), '08b'), \
        + (format(int(parts[2]), '08b'), \
        + (format(int(parts[3]), '08b')
        
        with open("conversion.txt", "b") as external_file:
        print('IP Address in Binary')
        print('0b'+bianryNumber, file=external_file)
        external_file.close()
        
        print()
        with open("conversion.txt", "o") as external_file:
print('IP Address in Octal base 8')
print( '0o'+format(int('0x'+hexNumber, base=16), '03o'), file=external_file)
external_file.close()