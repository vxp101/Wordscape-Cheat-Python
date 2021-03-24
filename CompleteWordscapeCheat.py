from tkinter import *
import re

dictionary = open('/storage/emulated/0/Documents/Python_Scripts/words_alpha.txt', 'r');
def txt():
	output.delete(0.0, END)
	text = txtbox.get()
	regEx = '^[' + text +']+$'
	unfiltArray = ""
	for i in dictionary:	
		if re.search(re.compile(regEx), i) and len(i) <= len(text) + 1:
			unfiltArray += i
	array = unfiltArray.split('\n')
	endGame = []
	for i in array:
		testCase = []
		testCaseU = []
		testCheck = False
		counter = 0
		for j in i:
			testCase.append(i.count(j))
			testCaseU.append(text.count(j))
		for j in testCase:
			if j <= testCaseU[counter]:
				testCheck = True
				counter += 1
			else:
				testCheck = False
				break
		if testCheck and len(i) > 2:
			output.insert(END, i + "\n")
window = Tk()
window.configure(bg="black")
Label (window, text='Wordscape Cheat', width=20, height=10, fg="white", bg="black").grid(row=0, column=0)
txtbox = Entry(window, width=20)
txtbox.grid(row=1, column=0)
Button(window, text='Submit', width=10, bg="white", command=txt).grid(row=2, column=0)
output = Text(window, bg="white", width=40, wrap=WORD)
output.grid(row=3, column=0)

window.mainloop()

