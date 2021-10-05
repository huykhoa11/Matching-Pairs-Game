import tkinter 
import random

img = [None]*14
card = [0]*26
face = [0]*26
turn = 0
check1 = 50
check2 = 100
tmp1 = 100
tmp2 = 100
phase = 1
a = 100
score_you = 0
score_com = 0
result = 13

def draw_result():
	global score_you, score_com
	cvs.delete("all")
	if score_you > score_com:
		cvs.create_text(980, 250, text="YOU WIN", fill="blue", font=("Times New Roman", 45))
	elif score_you < score_com:
		cvs.create_text(450, 250, text="COMPUTER WIN", fill="blue", font=("Times New Roman", 45))
	else:
		cvs.create_text(450, 250, text="DRAW", fill="blue", font=("Times New Roman", 45))

def draw_card():
	cvs.delete("all")
	for i in range(26):
		x = (i%7)*120+60
		y = int(i/7)*150+75
		if face[i]==0:
			cvs.create_image(x, y, image=img[0])
		if face[i]==1:
			cvs.create_image(x, y, image=img[card[i]])
	cvs.create_text(980, 250, text="YOU:"+str(score_you),fill="crimson", font=("Times New Roman", 36))
	cvs.create_text(980, 300, text="COM:"+str(score_com),fill="crimson", font=("Times New Roman", 36))


def shuffle_card():
	for i in range(26):
		card[i] = 1+i%13
	for i in range(100):
		r1 = random.randint(0, 12)
		r2 = random.randint(13, 25)
		card[r1], card[r2] = card[r2], card[r1]


def computer():
	global turn, phase, check1, check2, tmp1, tmp2, a, result
	arr = []
	if phase == -1:
		for i in range(26):
			if face[i] != 2:
				arr.append(i)

		if len(arr)>1:
			tmp1 = random.choice(arr)
			a = arr.index(tmp1)
			arr.remove(tmp1)
			face[tmp1] = 1

			tmp2 = random.choice(arr)
			arr.insert(a, tmp1)
			face[tmp2] = 1

			draw_card()
			check1 = card[tmp1]
			check2 = card[tmp2]
			root.after(900,check)


def check():
	global turn, phase, check1, check2, tmp1, tmp2, score_you, score_com, result
	if check1 == check2:
		face[tmp1] = 2
		face[tmp2] = 2
		result -= 1
		if phase == 1:
			score_you += 1
		elif phase == -1:
			score_com += 1
		if result == 0:
			draw_result()
	else:
		face[tmp1] = 0
		face[tmp2] = 0
		phase *= -1
	draw_card()
	if phase == -1:
		computer()
	turn = 0
	

def click(e):
	global turn, phase, check1, check2, tmp1, tmp2
	if phase == 1 and turn < 2:
		x = int(e.x/120)
		y = int(e.y/150)
		if 0<=x and x<=6 and 0<=y and y<=3:
			n = x+y*7
			if n>= 26:
				return
			if face[n]==0:
				face[n] = 1
				turn += 1
				if turn == 1:
					check1 = card[n]
					tmp1 = n
				if turn == 2:
					check2 = card[n]
					tmp2 = n
			if turn == 1 or turn == 2:
				draw_card()
			if turn == 2:
				root.after(900,check)


root = tkinter.Tk()
root.title("Game")
root.resizable(False, False)

root.bind("<Button>", click)
cvs = tkinter.Canvas(width=1100, height=650, bg="white")


for i in range(14):
	img[i] = tkinter.PhotoImage(file="img/"+str(i)+".png")

shuffle_card()
draw_card()
cvs.pack()
root.mainloop()