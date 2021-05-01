import os, sys, time
import base64
from math import exp, expm1
import random
import string
import numpy as np

logo = '''\033[1;38m\033[1m
  ____  _   _ ____  _____ _   _  ___   ____ ____      _    ____  _   _ 
 | ___|| | | |  _ \|___ /| \ | |/ _ \ / ___|  _ \    / \  |  _ \| | | |
 |___ \| |_| | |_) | |_ \|  \| | | | | |  _| |_) |  / _ \ | |_) | |_| |
  ___) |  _  |  _ < ___) | |\  | |_| | |_| |  _ <  / ___ \|  __/|  _  |
 |____/|_| |_|_| \_\____/|_| \_|\___/ \____|_| \_\/_/   \_\_|   |_| |_|\033[1;m\033[0m 
                                                 \033[1m\033[37m Made with \033[91m<3\033[37m By 5HR3D\033[1;m\033[0m                      
'''

#5HR3code
def shrecode_e():
	main = '''jO!l@JT<Eu+Am>z%*C-0sy,Wc"wt$Sa.Fh~D|x\X9?PG/nK`dU=q#LQ;8V:pr7'eBg 6[Y&b5oH^]i4N(f3}_{kZI2v1R)M'''
	newMessage = '\n  '
	ekey = -19
	message = input(' \n\033[1m\n Enter Text: \033[0m')
	for character in message:
		if character in main:
			position = main.find(character)
			newPosition = (position + ekey) % 95
			newCharacter = main[newPosition]
			newMessage += newCharacter
		else:
			newMessage += character
	print("\n Encrypted Text: " + newMessage)
	print("")
		
def shrecode_d():
	main = '''jO!l@JT<Eu+Am>z%*C-0sy,Wc"wt$Sa.Fh~D|x\X9?PG/nK`dU=q#LQ;8V:pr7'eBg 6[Y&b5oH^]i4N(f3}_{kZI2v1R)M'''
	newMessage = '\n  '
	dkey = +19
	message = input(' \n\033[1m\n Enter Text: \033[0m')
	for character in message:
		if character in main:
			position = main.find(character)
			newPosition = (position + dkey) % 95
			newCharacter = main[newPosition]
			newMessage += newCharacter
		else:
			newMessage += character
	print("\n Decrypted Text:")
	print(newMessage + "\n")
	
#----------------------base64----------------------------------------
def base64_e():
	try:
		decoded_string = input(' String To Encode: ')
		encoded_string = base64.b64encode(decoded_string.encode('utf-8'))
		print(" Encoded String: " + str(encoded_string))
	except:
		print(' Invalid Input')

def base64_d():
	try:
		encoded_string = input(' String To Decode: ')
		decoded_string = base64.b64decode(encoded_string.encode('utf-8'))
		print (" Decoded String: " + str(decoded_string))
	except:
		print(' Invalid Input')


#--------------------------------------------------------------------
def hill_e():
	main=string.ascii_lowercase

	def generate_key(n,s):
		s=s.replace(" ","")
		s=s.lower()

		key_matrix=['' for i in range(n)]
		i=0;j=0
		for c in s:
			if c in main:
				key_matrix[i]+=c
				j+=1
				if(j>n-1):
					i+=1
					j=0
		print("The key matrix "+"("+str(n)+'x'+str(n)+") is:")
		print(key_matrix)
		
		key_num_matrix=[]	
		for i in key_matrix:
			sub_array=[]
			for j in range(n):
				sub_array.append(ord(i[j])-ord('a'))
			key_num_matrix.append(sub_array)
			
		for i in key_num_matrix:
			print(i)
		return(key_num_matrix)
		
	def message_matrix(s,n):
		s=s.replace(" ","")
		s=s.lower()
		final_matrix=[]
		if(len(s)%n!=0):
			# z is the bogus word
			while(len(s)%n!=0):
				s=s+'z'
		
		print("Converted plain_text for encryption: ",s)
		for k in range(len(s)//n):
			message_matrix=[]
			for i in range(n):
				sub=[]
				for j in range(1):
					sub.append(ord(s[i+(n*k)])-ord('a'))
				message_matrix.append(sub)
			final_matrix.append(message_matrix)
		print("The column matrices of plain text in numbers are:  ")
		for i in final_matrix:
			print(i)
		return(final_matrix)
	
	# Function to get cofactor of  
	# mat[p][q] in temp[][]
	# passing the key matrix as 'mat' to check for invertibility
	def getCofactor(mat, temp, p, q, n):
		i = 0
		j = 0
		
		# Looping for each element 
		# of the matrix 
		for row in range(n): 
			for col in range(n):
				# Copying into temporary matrix only those element   
				# which are not in given row and column 
				if (row != p and col != q) : 
					temp[i][j] = mat[row][col] 
					j += 1
					
					# Row is filled, so increase
					# row index and reset col index 
					if (j == n - 1):
						j = 0
						i += 1
					
	# Recursive function for finding determinant of matrix. 
	# n is current dimension of mat[][].  
	def determinantOfMatrix(mat, n): 
		D = 0 # Initialize result 
		# Base case : if matrix 
		# contains single element 
		if (n == 1):
			return mat[0][0] 
			
		# To store cofactors 
		temp = [[0 for x in range(n)] 
			for y in range(n)]  
			
		sign = 1 # To store sign multiplier 
		
		# Iterate for each
		# element of first row 
		for f in range(n): 
		
			# Getting Cofactor of mat[0][f] 
			getCofactor(mat, temp, 0, f, n) 
			D += (sign * mat[0][f] *
				determinantOfMatrix(temp, n - 1))
				
			# terms are to be added with alternate sign
			sign = -sign
		return D
		
	def isInvertible(mat, n): 
		if (determinantOfMatrix(mat, n) != 0): 
			return True
		else: 
			return False
			
	def multiply_and_convert(key,message):
    
		# multiplying matrices
		# resultant must have:
		# rows = numbers of rows in message matrix
		# columns = number of columns in key matrix 
		res_num = [[0 for x in range(len(message[0]))] for y in range(len(key))]
    
		for i in range(len(key)): 
			for j in range(len(message[0])):
				for k in range(len(message)): 
					# resulted number matrix
					res_num[i][j]+=key[i][k] * message[k][j]

		res_alpha = [['' for x in range(len(message[0]))] for y in range(len(key))]
		# getting the alphabets from the numbers
		#according to the logic of hill ciipher
		for i in range(len(key)):
			for j in range(len(message[0])):
				# resultant alphabet matrix
				res_alpha[i][j]+=chr((res_num[i][j]%26)+97)
		return(res_alpha)

	# implementing all logic and calling function
	n=int(input("What will be the order of square matrix: "))
	s=input("Enter the key: ")
	key=generate_key(n,s)
	
	# check for invertability here
	if (isInvertible(key, len(key))): 
		print("Yes it is invertable and can be decrypted") 
	else: 
		print("No it is not invertable and cannot be decrypted")
    

	plain_text=input("Enter the message: ")
	message=message_matrix(plain_text,n)
	final_message=''
	for i in message:
		sub=multiply_and_convert(key,i)
		for j in sub:
			for k in j:
				final_message+=k
	print("plain message: ",plain_text)
	print("final encrypted message: ",final_message)


#--------------------------------------------------------------------

def hill_d():

	main=string.ascii_lowercase

	def generate_key(n,s):
		s=s.replace(" ","")
		s=s.lower()
    
		key_matrix=['' for i in range(n)]
		i=0;j=0
		for c in s:
			if c in main:
					key_matrix[i]+=c
					j+=1
					if(j>n-1):
						i+=1
						j=0
		print("The key matrix "+"("+str(n)+'x'+str(n)+") is:")
		print(key_matrix)
    
		key_num_matrix=[]
		for i in key_matrix:
			sub_array=[]
			for j in range(n):
				sub_array.append(ord(i[j])-ord('a'))
			key_num_matrix.append(sub_array)

		for i in key_num_matrix:
			print(i)
		return(key_num_matrix)


	def modInverse(a, m) : 
		a = a % m; 
		for x in range(1, m) : 
			if ((a * x) % m == 1) : 
				return x 
		return 1

	def method(a, m) :
		if(a>0):
			return (a%m)
		else:
			k=(abs(a)//m)+1
		return method(a+k*m,m)


	def message_matrix(s,n):
		s=s.replace(" ","")
		s=s.lower()
		final_matrix=[]
		if(len(s)%n!=0):
			# may be negative also
			for i in range(abs(len(s)%n)):
				# z is the bogus word
				s=s+'z'
		print("Converted cipher_text for decryption: ",s)
		for k in range(len(s)//n):
			message_matrix=[]
			for i in range(n):
				sub=[]
				for j in range(1):
					sub.append(ord(s[i+(n*k)])-ord('a'))
				message_matrix.append(sub)
			final_matrix.append(message_matrix)
		print("The column matrices of plain text in numbers are:  ")
		for i in final_matrix:
			print(i)
		return(final_matrix)


	def multiply_and_convert(key,message):
    
		# multiplying matrices
		# resultant must have:
		# rows = numbers of rows in message matrix
		# columns = number of columns in key matrix 
		res_num = [[0 for x in range(len(message[0]))] for y in range(len(key))]
    
		for i in range(len(key)): 
			for j in range(len(message[0])):
				for k in range(len(message)): 
					# resulted number matrix
					res_num[i][j]+=key[i][k] * message[k][j]

		res_alpha = [['' for x in range(len(message[0]))] for y in range(len(key))]
		# getting the alphabets from the numbers
		# according to the logic of hill ciipher
		for i in range(len(key)):
			for j in range(len(message[0])):
				# resultant alphabet matrix
				res_alpha[i][j]+=chr((res_num[i][j]%26)+97)
            
		return(res_alpha)
		
		
	n=int(input("What will be the order of square matrix: "))
	s=input("Enter the key: ")
	key_matrix=generate_key(n,s)
	A = np.array(key_matrix)
	det=np.linalg.det(A)
	adjoint=det*np.linalg.inv(A)

	if(det!=0):
		convert_det=modInverse(int(det),26)
		adjoint=adjoint.tolist()
		print("Adjoint Matrix before modulo26 operation: ")
		for i in adjoint:
			print(i)
		print(convert_det)

		# applying modulo 26 to all elements in adjoint matrix
		for i in range(len(adjoint)):
			for j in range(len(adjoint[i])):
				adjoint[i][j]=round(adjoint[i][j])
				adjoint[i][j]=method(adjoint[i][j],26)
		print("Adjoint Matrix after modulo26 operation: ")
		for i in adjoint:
			print(i)

		# modulo is applied to inverse of determinant and
		# multiplied to all elements in the adjoint matrix
		# to form inverse matrix
		adjoint=np.array(adjoint)
		inverse=convert_det*adjoint

		inverse=inverse.tolist()
		for i in range(len(inverse)):
			for j in range(len(inverse[i])):
				inverse[i][j]=inverse[i][j]%26
	
		print("Inverse matrix after applying modulo26 operation: ")
		for i in inverse:
			print(i)

		cipher_text=input("Enter the cipher text: ")
		message=message_matrix(cipher_text,n)
		plain_text=''
		for i in message:
			sub=multiply_and_convert(inverse,i)
			for j in sub:
				for k in j:
					plain_text+=k
                
		print("plain message: ",plain_text)
	else:
		print("Matrix cannot be inverted")
#--------------------------playfair----------------------------------
def playfair_e():
	def key_generation(key):
		main=string.ascii_lowercase.replace('j','.')
		key=key.lower()
    
		key_matrix=['' for i in range(5)]
		i=0;j=0
		for c in key:
			if c in main:
				key_matrix[i]+=c
				main=main.replace(c,'.')
				j+=1
				if(j>4):
					i+=1
					j=0

		for c in main:
			if c!='.':
				key_matrix[i]+=c

				j+=1
				if j>4:
					i+=1
					j=0
	                
		return(key_matrix)


	def conversion(plain_text):
		plain_text_pairs=[]
		cipher_text_pairs=[]

		plain_text=plain_text.replace(" ","")
		plain_text=plain_text.lower()

		i=0
		
		while i<len(plain_text):
			a=plain_text[i]
			b=''

			if((i+1)==len(plain_text)):
				b='x'
			else:
				b=plain_text[i+1]

			if(a!=b):
				plain_text_pairs.append(a+b)
				i+=2
			else:
				plain_text_pairs.append(a+'x')
				i+=1
            
		print("plain text pairs: ",plain_text_pairs)


		for pair in plain_text_pairs:
			flag=False
			for row in key_matrix:
				if(pair[0] in row and pair[1] in row):
					j0=row.find(pair[0])
					j1=row.find(pair[1])
					cipher_text_pair=row[(j0+1)%5]+row[(j1+1)%5]
					cipher_text_pairs.append(cipher_text_pair)
					flag=True
			if flag:
				continue
                
			for j in range(5):
				col="".join([key_matrix[i][j] for i in range(5)])
				if(pair[0] in col and pair[1] in col):
					i0=col.find(pair[0])
					i1=col.find(pair[1])
					cipher_text_pair=col[(i0+1)%5]+col[(i1+1)%5]
					cipher_text_pairs.append(cipher_text_pair)
					flag=True
			if flag:
				continue
			i0=0
			i1=0
			j0=0
			j1=0

			for i in range(5):
				row=key_matrix[i]
				if(pair[0] in row):
					i0=i
					j0=row.find(pair[0])
					if(pair[1] in row):
						i1=i
						j1=row.find(pair[1])
			cipher_text_pair=key_matrix[i0][j1]+key_matrix[i1][j0]
			cipher_text_pairs.append(cipher_text_pair)
        
		print("cipher text pairs: ",cipher_text_pairs)
		print('plain text: ',plain_text)
		print('cipher text: ',"".join(cipher_text_pairs))


	key=input("Enter the key: ")

	key_matrix=key_generation(key)
	print("Key Matrix for encryption:")
	print(key_matrix)
	plain_text=input("Enter the message: ")

	conversion(plain_text)

#---------------------------------playfair_d--------------------------------

def playfair_d():

	def key_generation(key):
		main=string.ascii_lowercase.replace('j','.')
		key=key.lower()
    
		key_matrix=['' for i in range(5)]
		i=0;j=0
		for c in key:
			if c in main:
				key_matrix[i]+=c

				main=main.replace(c,'.')
				j+=1
				if(j>4):
					i+=1
					j=0

		for c in main:
			if c!='.':
				key_matrix[i]+=c

				j+=1
				if j>4:
					i+=1
					j=0
                
		return(key_matrix)


	def conversion(cipher_text):
		plain_text_pairs=[]
		cipher_text_pairs=[]
		cipiher_text=cipher_text.lower()

		i=0
		while i<len(cipher_text):
			a=cipher_text[i]
			b=cipher_text[i+1]

			cipher_text_pairs.append(a+b)
			i+=2
            
		print("cipher text pairs: ",cipher_text_pairs)


		for pair in cipher_text_pairs:
			flag=False
			for row in key_matrix:
				if(pair[0] in row and pair[1] in row):
					j0=row.find(pair[0])
					j1=row.find(pair[1])
					plain_text_pair=row[(j0+4)%5]+row[(j1+4)%5]
					plain_text_pairs.append(plain_text_pair)
					flag=True
			if flag:
				continue

			for j in range(5):
				col="".join([key_matrix[i][j] for i in range(5)])
				if(pair[0] in col and pair[1] in col):
					i0=col.find(pair[0])
					i1=col.find(pair[1])
					plain_text_pair=col[(i0+4)%5]+col[(i1+4)%5]
					plain_text_pairs.append(plain_text_pair)
					flag=True
			if flag:
				continue
			i0=0
			i1=0
			j0=0
			j1=0

			for i in range(5):
				row=key_matrix[i]
				if(pair[0] in row):
					i0=i
					j0=row.find(pair[0])
				if(pair[1] in row):
					i1=i
					j1=row.find(pair[1])
			plain_text_pair=key_matrix[i0][j1]+key_matrix[i1][j0]
			plain_text_pairs.append(plain_text_pair)
        
		print("plain text pairs: ",plain_text_pairs)
    
		print('cipher text: ',"".join(cipher_text_pairs))
		print('plain text (message): ',"".join(plain_text_pairs))


	key=input("Enter the key: ")

	key_matrix=key_generation(key)
	print("Key Matrix for encryption:")
	print(key_matrix)
	cipher_text=input("Enter the encrypted message: ")

	conversion(cipher_text)




#---------------------------railfence_e-------------------------------------

def railfence_e():


	def sequence(n):
		arr=[]
		i=0

		while(i<n-1):
			arr.append(i)
			i+=1
		while(i>0):
			arr.append(i)
			i-=1
		return(arr)

	def railfence(s,n):
		s=s.lower()

		L=sequence(n)
		print("The raw sequence of indices: ",L)

		temp=L
    
		# adjustments
		while(len(s)>len(L)):
			L=L+temp

		for i in range(len(L)-len(s)):
			L.pop()
		print("The row indices of the characters in the given string: ",L)
    
    
		print("Transformed message for encryption: ",s)

		# converting into cipher text
		num=0
		cipher_text=""
		while(num<n):
			for i in range(L.count(num)):
				# adding characters according to
				# indices to get cipher text
				cipher_text=cipher_text+s[L.index(num)]
				L[L.index(num)]=n
			num+=1
		print("The cipher text is: ",cipher_text)
   
	plain_text=input("Enter the string to be encrypted: ")
	n=int(input("Enter the number of rails: "))
	railfence(plain_text,n)

#---------------------------railfence_d-----------------------------

def railfence_d():
	# this function is to get the desired sequence
	def sequence(n):
		arr=[]
		i=0

		while(i<n-1):
			arr.append(i)
			i+=1
		while(i>0):
			arr.append(i)
			i-=1
		return(arr)

	# this is to implement the logic
	def railfence(cipher_text,n):
		# converting into lower cases
		cipher_text=cipher_text.lower()

		L=sequence(n)
		print("The raw sequence of indices: ",L)

		temp=L
    
		# adjustments
		while(len(cipher_text)>len(L)):
			L=L+temp

		# removing the extra last indices
		for i in range(len(L)-len(cipher_text)):
			L.pop()
        
		# storing L.sort() in temp1
		temp1=sorted(L)
    
		print("The row indices of the characters in the cipher string: ",L)

		print("The row indices of the characters in the plain string: ",temp1)
    
		print("Transformed message for decryption: ",cipher_text)

		# converting into plain text
		plain_text=""
		for i in L:

			k=temp1.index(i)
			temp1[k]=n
			plain_text+=cipher_text[k]
        
		print("The cipher text is: ",plain_text)


	cipher_text=input("Enter the string to be decrypted: ")
	n=int(input("Enter the number of rails: "))
	railfence(cipher_text,n)
#-------------------vernam_e------------------------------------------

def vernam_e():

	# function to apply algo of vernam cipher
	def vernam(plain_text,key):

		# convert into lower cases and remove spaces
    
		plain_text=plain_text.replace(" ","")
		key=key.replace(" ","")
		plain_text=plain_text.lower()
		key=key.lower()
    
		# conditional statements
		if(len(plain_text)!=len(key)):
			print("Lengths are different")
        
		else:
			cipher_text=""
        
			# iterating through the length
			for i in range(len(plain_text)):
				k1=ord(plain_text[i])-97
				k2=ord(key[i])-97
				s=chr((k1+k2)%26+97)
				cipher_text+=s
			print("Enrypted message is: ",cipher_text)


	plain_text=input("Enter the message: ")
	key=input("Enter the one time pad: ")
	vernam(plain_text,key)
#---------------------------vernam_d---------------------------------

def vernam_d():

	# function to apply algo of vernam cipher
	def vernam(cipher_text,key):

		# convert into lower cases and remove spaces
		cipher_text=cipher_text.lower()
		key=key.lower()
		cipher_text=cipher_text.replace(" ","")
		key=key.replace(" ","")
    
		plain_text=""
    
		# iterating through the length
		for i in range(len(cipher_text)):
			k1=ord(cipher_text[i])-97
			k2=ord(key[i])-97
			s=chr((((k1-k2)+26)%26)+97)
			plain_text+=s
		print("Decrypted message is: ",plain_text)

	plain_text=input("Enter the message to be decrypted: ")
	key=input("Enter the one time pad: ")
	vernam(plain_text,key)


#----------------------------vigenere_e--------------------------------
def vigenere_e():

	main=string.ascii_lowercase

	def conversion(plain_text,key):
		index=0
		cipher_text=""

		# convert into lower case
		plain_text=plain_text.lower()
		key=key.lower()
    
		# For generating key, the given keyword is repeated
		# in a circular manner until it matches the length of 
		# the plain text.
		for c in plain_text:
			if c in main:
				# to get the number corresponding to the alphabet
				off=ord(key[index])-ord('a')
            
				# implementing algo logic here
				encrypt_num=(ord(c)-ord('a')+off)%26
				encrypt=chr(encrypt_num+ord('a'))
            
				# adding into cipher text to get the encrypted message
				cipher_text+=encrypt
            
				# for cyclic rotation in generating key from keyword
				index=(index+1)%len(key)
			# to not to change spaces or any other special
			# characters in their positions
			else:
				cipher_text+=c

		print("plain text: ",plain_text)
		print("cipher text: ",cipher_text)

	plain_text=input("Enter the message: ")
	key=input("Enter the key: ")

	# calling function
	conversion(plain_text,key)


#----------------------------vigenere_d--------------------------------
def vigenere_d():
	main=string.ascii_lowercase
	def conversion(cipher_text,key):
		index=0
		plain_text=""

		# convert into lower case
		cipher_text=cipher_text.lower()
		key=key.lower()
    
		for c in cipher_text:
			if c in main:
				# to get the number corresponding to the alphabet
				off=ord(key[index])-ord('a')

				positive_off=26-off
				decrypt=chr((ord(c)-ord('a')+positive_off)%26+ord('a'))
            
				# adding into plain text to get the decrypted messag
				plain_text+=decrypt
            
				# for cyclic rotation in generating key from keyword
				index=(index+1)%len(key)
			else:
				plain_text+=c

		print("cipher text: ",cipher_text)
		print("plain text (message): ",plain_text)

	cipher_text=input("Enter the message to be decrypted: ")
	key=input("Enter the key for decryption: ")

	# calling function
	conversion(cipher_text,key)
#---------------------------caesar-----------------------------------
def caesar_e():
	def encrypt(text,s):
   
		# Cipher(n) = De-cipher(26-n)
		s=s   
		text =text.replace(" ","")
		result=""  #empty string
		for i in range(len(text)):
			char=text[i]
			if(char.isupper()):  #if the text[i] is in upper case
				result=result+chr((ord(char)+s-65)%26+65)
			else:
				result=result+chr((ord(char)+s-97)%26+97)
		return result


	word=str(input("enter the word:"))
	k=int(input("Enter the key: "))
	
	print("Encoded word in Caeser cipher is: ",encrypt(word,k))

def caesar_d():

	def decrypt(text,s):

		# Cipher(n) = De-cipher(26-n)
		s=26-s 
        
		result=""  #empty string
		for i in range(len(text)):
			char=text[i]
			if(char.isupper()):  #if the text[i] is in upper case
				result=result+chr((ord(char)+s-65)%26+65)
			else:
				result=result+chr((ord(char)+s-97)%26+97)
		return result


	word=str(input("enter the word:"))
	d=int(input("Enter the key: "))

	print("Encoded word in Caeser cipher is: ",decrypt(word,d))



#----------------------------Main--------------------------------


print(logo)

def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)
slowprint("\033[1m\033[1;33m [!] Loading...\n\n\033[1;m\033[0m ")
time.sleep(0.8)
os.system('clear')

print(logo)


print("\n Choose:\n")

print(" [01] 5HR3code")
print(" [02] Base64")
print(" [03] Ciphers")
print(" [04] Info for nerds.")
print(" [55] Exit")

choice = input("\n  [#]:> ")


if choice == "1" or choice == "01":
	os.system('clear')
	print(logo)
	print("\n  5HR3CODE\n")
	print(" [01] Encrypt")
	print(" [02] Decrypt")
	shreinput = input("\n  [#]:> ")
	
	if shreinput == "1" or shreinput == "01":
		os.system('clear')
		print(logo)
		print("\n  5HR3CODE ENCRYPTION:")
		print(" ")
		shrecode_e()
		
	elif shreinput == "2" or shreinput == "02":
		os.system('clear')
		print(logo)
		print("\n  5HR3CODE DECRYPTION:")
		print(" ")
		shrecode_d()
	
	else:
		print("\n Error Occured, Please Re-try.\n")	
	

elif choice == "2" or choice == "02":
	os.system('clear')
	print(logo)
	print("\n  BASE64\n")
	print(" [01] Encrypt")
	print(" [02] Decrypt")
	b64input = input("\n  [#]:> ")

	if b64input == "1" or b64input == "01":
		base64_e()
		
	elif b64input == "2" or b64input == "02":
		base64_d()
		
	else:
		print("\n Error Occured, Please Re-try.\n")	
	
elif choice == "3" or choice == "03":
	os.system('clear')
	print(logo)
	print("\n CIPHERS:")
	print("\n [01] Hill cipher")
	print(" [02] Playfair cipher")
	print(" [03] Rail-fence cipher")
	print(" [04] Vernam cipher")
	print(" [05] Vigenere cipher")
	print(" [06] Caesar cipher")
	cypherinput = input("\n  [#]:> ")
		
	if cypherinput == "1" or cypherinput == "01":
		print("\n [01] Encrypt")
		print(" [02] Decrypt")
		hillcyi = input("\n  [#]:> ")
		if hillcyi == "1" or hillcyi == "01":
			hill_e()
		elif hillcyi == "2" or hillcyi == "02":
			hill_d()
		else:
			print(" Error Occured, Please Try again.")
	
	elif cypherinput == "2" or cypherinput == "02":
		print("\n [01] Encrypt")
		print(" [02] Decrypt")
		pfcyi = input("\n  [#]:> ")
		if pfcyi == "1" or pfcyi == "01":
			playfair_e()
		elif pfcyi == "2" or pfcyi == "02":
			playfair_d()
		else:
			print(" Error Occured, Please Try again.")
			
	elif cypherinput == "3" or cypherinput == "03":
		print("\n [01] Encrypt")
		print(" [02] Decrypt")
		rfcyi = input("\n  [#]:> ")
		if rfcyi == "1" or rfcyi == "01":
			railfence_e()
		elif rfcyi == "2" or rfcyi == "02":
			railfence_d()
		else:
			print(" Error Occured, Please Try again.")
			
	elif cypherinput == "4" or cypherinput == "04":
		print("\n [01] Encrypt")
		print(" [02] Decrypt")
		vcyi = input("\n  [#]:> ")
		if vcyi == "1" or vcyi == "01":
			vernam_e()
		elif vcyi == "2" or vcyi == "02":
			vernam_d()
		else:
			print(" Error Occured, Please Try again.")
			
	elif cypherinput == "5" or cypherinput == "05":
		print("\n [01] Encrypt")
		print(" [02] Decrypt")
		vicyi = input("\n  [#]:> ")
		if vicyi == "1" or vicyi == "01":
			vigenere_e()
		elif vicyi == "2" or vicyi == "02":
			vigenere_d()
		else:
			print(" Error Occured, Please Try again.")
			
	elif cypherinput == "6" or cypherinput == "06":
		print("\n [01] Encrypt")
		print(" [02] Decrypt")
		ccyi = input("\n  [#]:> ")
		if ccyi == "1" or ccyi == "01":
			caesar_e()
		elif ccyi == "2" or ccyi == "02":
			caesar_d()
		else:
			print(" Error Occured, Please Try again.")
		
	else:
		print(" Error Occured, Please Try again.")
		
		
elif choice == "4" or choice == "04":
	os.system("clear")
	print(logo)
	print(" INFO FOR NERDS:")
	print("""
>BASE64
   Base64 is a group of binary-to-text encoding schemes 
   that represent binary data (more specifically a 
   sequence of 8-bit bytes) in an ASCII string 
   format by translating it into a radix-64 representation.

   For more info on the Algorithm:
   https://www.lucidchart.com/techblog/2017/10/23/base64-encoding-a-visual-explanation/

>CIPHERS
   ~HILL CIPHER
    Hill cipher is a polygraphic substitution
    cipher based on linear algebra.

    For more info on the Algorithm:
    https://massey.limfinity.com/207/hillcipher.pdf

   ~PLAYFAIR
    Playfair cipher or Playfair square or Wheatstone–Playfair 
    cipher is a manual symmetric encryption technique and was 
    the first literal digram substitution cipher.

    For more info on the Algorithm:
    https://en.wikipedia.org/wiki/Playfair_cipher

   ~RAIL FENCE
    The rail fence cipher (also called a zigzag cipher) is a 
    form of transposition cipher. It 
    derives its name from the way in which it is encoded. 

    For more info on the Algorithm:
    http://rumkin.com/tools/cipher/railfence.php

    ~VERNAM
    Vernam cipher is a symmetrical stream cipher in which 
    the plaintext is combined with a random or pseudorandom 
    stream of data (the "keystream") of the same length, to 
    generate the ciphertext, using the Boolean "exclusive or" 
    XOR) function.

    For more info on the Algorithm:
    https://en.wikipedia.org/wiki/Gilbert_Vernam

   ~VIGENERE
    The Vigenère cipher is a method of encrypting alphabetic
    text by using a series of interwoven Caesar ciphers, 
    based on the letters of a 
    keyword. It employs a form of polyalphabetic substitution

    For more info on the Algorithm:
    https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher#Cryptanalysis
 
   ~CAESAR
    Caesar's cipher is one of the simplest and most 
    widely known encryption techniques. It is a type 
    of substitution cipher in which each letter in the 
    plaintext is replaced by a letter some fixed number 
    of positions down the alphabet. For example, with a 
    left shift of 3, D would be replaced by A, E would 
    become B, and so on. The method is named after Julius 
    Caesar, who used it in his private correspondence.

    For more info on the Algorithm:
    https://en.wikipedia.org/wiki/Caesar_cipher#Breaking_the_cipher

>5HR3CODE
   SHRECODE is a modified type of the Shift Cipher. Shrecode can 
   encrypt alphanumeric (+symbols) unlike other ciphers ¯\_(ツ)_/¯
   
""")
	
elif choice == "55":
	exit()
		
else:
	print(" Error Occured, Please Try again.")
