# !/bin/Python3

def Encript(key,message):
	alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
	newMessage = ''
	for character in message:
		if character in alphabet:
			position = alphabet.find(character)
			newPosition = (position + key) % 61
			newCharacter = alphabet[newPosition]
			newMessage += newCharacter
	return(newMessage)

def Decript(key,message):
	alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
	newMessage = ''
	for character in message:
		if character in alphabet:
			position = alphabet.find(character)
			newPosition = (position - key)
			if newPosition < 0:
				newPosition = 61 + newPosition
			newCharacter = alphabet[newPosition]
			newMessage += newCharacter
	return(newMessage)

flag1 = True
flag2 = True
message = input('Please enter the Text: ')
while flag1:
	key = int(input('Please enter the key(Only between 0-61): '))
	if key > 61 or key < 0:
		print("Choose the key Between 0-61")
	else:
		while flag2: 
			choice = int(input("Enter 1 for Encription and 2 for Decription"))
			if choice==1:
				Encripted_message = Encript(key,message)
				print('Encripted message is : ', Encripted_message)
				flag2 = False
			elif choice==2:
				Decripted_message = Decript(key,message)
				print('Decripted message is : ', Decripted_message)
				flag2 = False
			else:
				print("Only choose between 1 and 2")
		flag1 = False
