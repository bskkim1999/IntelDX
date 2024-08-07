def introKor():
	print("hello (kor)")

def introEng():
	print("hello (eng)")

def introJap():
	print("hello (jap)")


while True:
	selectNum = int(input("choose 1 or 2 or 3 or 4: ") )


	if selectNum==1:
		introKor()

	elif selectNum==2:
		introEng()

	elif selectNum==3:
		introJap()

	elif selectNum==4:
		break
