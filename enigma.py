import string
from stator import stator
from firstRotor import firstRotor
from secondRotor import secondRotor
from thirdRotor import thirdRotor

abc = list(string.ascii_uppercase)

rotor_3 = thirdRotor()
rotor_2 = secondRotor()
rotor_1 = firstRotor()
stator = stator()

def crypt_word(word):
	result = list()
	for letter in word:
		result.append(codeByRotors(letter))
	return result	

def decrypt_word(word):
	result = list()
	for letter in word:
		result.append(decodeByRotors(letter))
	return result

def codeByRotors(letter):
	number = abc.index(letter) + 1
	thirdRtl = rotor_3.code(number, 0)
	secondRtl = rotor_2.code(thirdRtl, 0)
	firstRtl = rotor_1.code(secondRtl, 0)
	statorRtl = stator.find(firstRtl)
	firstLtr = rotor_1.code(statorRtl, 1)
	secondLtr = rotor_2.code(firstLtr, 1)
	thirdLtr = rotor_3.code(secondLtr, 1)
	result = thirdLtr

	return abc[result - 1]

def decodeByRotors(letter):
	number = abc.index(letter) + 1
	thirdRtl = rotor_3.decode(number, 0)
	secondRtl = rotor_2.decode(thirdRtl, 0)
	firstRtl = rotor_1.decode(secondRtl, 0)
	statorRtl = stator.find(firstRtl)
	firstLtr = rotor_1.decode(statorRtl, 1)
	secondLtr = rotor_2.decode(firstLtr, 1)
	thirdLtr = rotor_3.decode(secondLtr, 1)
	result = thirdLtr

	return abc[result - 1]

def configureMachine(action, frtRrStart, sndRrStart, trdRrStart):
	if action == '1':
		rotor_1.code_position = frtRrStart
		rotor_2.code_position = sndRrStart
		rotor_3.code_position = trdRrStart
	elif action == '2':
		rotor_1.decode_position = frtRrStart
		rotor_2.decode_position = sndRrStart
		rotor_3.decode_position = trdRrStart
	

def runMachine(action, stringByWords):
	result = ''
	strg = ''
	if action == '1':
		for word in stringByWords:
			crypted = crypt_word(word)
			result += strg.join(crypted)
			result += ' '
	elif action == '2':
		for word in stringByWords:
			uncr = decrypt_word(word)
			result += strg.join(uncr)
			result += ' '
	return result

def process(frtRrStart, sndRrStart, trdRrStart, inputString, action):
	inputString = inputString.upper()
	stringByWords = inputString.split()
	if action and frtRrStart and sndRrStart and trdRrStart:
		configureMachine(action, int(frtRrStart), int(sndRrStart), int(trdRrStart))
		result = runMachine(action, stringByWords)
		return result
	else:
		return 'Error: Some settings ara failed'
