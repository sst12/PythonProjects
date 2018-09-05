#!/bin/python3
import random

def newPass(n):
	chars = '''abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(),./<>?;':"[]{}-_+="'''
	password = ''
	for c in range(n):
		password += random.choice(chars)
	return(password)
LengthOfPass = int(input("How many Charchters DO you want: "))
NoOfPass = int(input("How Many Password DO you Want: "))
for i in range(NoOfPass):
	New_Password =  newPass(LengthOfPass)
	print(New_Password)
