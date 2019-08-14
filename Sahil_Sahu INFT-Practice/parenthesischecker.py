
def balanced(expr):
	stk = []
	for i in range(len(expr)):
		if (expr[i]== "(" or expr[i]== "[" or expr[i]== "{"):
			stk.append(expr[i])
			continue

		if(len(stk)==0):
			return False

		if(expr[i]==")"):
			x = stk.pop()
			if(x == "{" or x == "["):
				return False

		elif(expr[i]=="]"):
			x = stk.pop()
			if(x == "{" or x == "("):
				return False

		elif(expr[i]=="}"):
			x = stk.pop()
			if(x == "(" or x == "["):
				return False

	if(len(stk)==0):
		return True
	else:
		return False


# print ("Enter")
expression = input("Enter Expression you want to test\nMinimum length should be 2 characters ->")
while(len(expression)<2):
	expression = input("\n\nEnter Expression you want to test\nMinimum length should be 2 characters ->")

if(balanced(expression)):
	print (expression+" is BALANCED !!!")
else:
	print (expression+" is NOT BALANCED...")