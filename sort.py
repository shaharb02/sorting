#!/usr/bin/env python3
import turtle
import time
import os
import binascii
import random

window = turtle.Screen()
window.title("Sorter")
window.bgcolor("#FFFFAA")
window.setup(width=1600, height=900)
window.tracer(0)

turtles = []
color_list = ['#'+str(binascii.b2a_hex(os.urandom(3)))[2:8] for _ in range(200)]
method = 0
sorting = 0
startt = 0
button_list = []
swaps = 0
complexity = "O(N)"
def start():
	global startt
	txt = "Welcome To 0x5h31eg's Sorting Simulation"
	t = turtle.Turtle()
	t.speed(0)
	t.penup()
	t.write(txt, align='center', font=("Courier", 50, "normal"))
	t.sety(-100)
	for i in range(5,0,-1):
		t.setx(i*250 - 750)
		t.write(i, align='center', font=("Courier", 40, "normal"))
		time.sleep(1)
	window.clear()
	window.bgcolor("#FFFFAA")
	window.tracer(0)
	startt = 5
def exitt():
	window.bye()
def text():
    methods = ["Selection", "Bubble", "Insertion", "Cocktail Shaker", "Pigeonhole", "Merge"]
    draw = turtle.Turtle()
    draw.speed(0)
    draw.penup()
    draw.ht()
    for x in range(6):
        draw.goto(-500 + x*200,-250)
        draw.write(methods[x],align='center', font=("Courier", 16, "normal"))
def buttons():   
    for i in range(6):
        t1 = turtle.Turtle()
        t1.speed(0)
        t1.shape("circle")
        t1.shapesize(5, 5)
        t1.color(('#00FFFF'))
        t1.penup()
        t1.goto(-500 + i*200 , -300)
        button_list.append(t1)
    button_list[0].color("red")
    window.update() 
def timething():
	draw = turtle.Turtle()
	draw.speed(0)
	draw.penup()
	draw.color("#FFFFAA")
	draw.goto(-500 ,-50)
	draw.shape("square")
	draw.shapesize(15,30,5)
def init():
    turtless = []
    text()
    buttons()
    timething()
    for k in range(100):
        x = random.randint(5, 50)
        t1 = turtle.Turtle()
        t1.speed(0)
        t1.shape("square")
        t1.shapesize(x, 0.2)
        t1.color(color_list[k])
        t1.penup()
        t1.goto(k * 10 - 500, 450)
        turtless.append(t1)
        window.update()
    return turtless

def randomize():
    if not sorting:
        for index, myturtle in enumerate(turtles):
            x = random.randint(5, 50)
            myturtle.shapesize(x, 0.2)
            color_list = ['#'+str(binascii.b2a_hex(os.urandom(3)))[2:8] for _ in range(200)]
            myturtle.color(color_list[index])
        window.update()
    else:
        pass
def method_choose(x, y):

	global method
	#print(x,y)
	if not sorting:
		if y < -250 and y > -350:
			for t in button_list:
				t.color('#00FFFF')

			if x > -550 and x < -450:
				method = 0

			if x > -350 and x < -250:
				method = 1

			if x > -150 and x < -50:
				method = 2

			if x > 50 and x < 150:
				method = 3

			if x > 250 and x < 350:
				method = 4

			if x > 450 and x < 550:
				method = 5
			button_list[method].color("red")

	else:
		pass
def left():
    global method
    if not sorting:
        method -= 1
        if method == -1:
            method = 5

        for t in button_list:
        	t.color('#00FFFF')
        button_list[method].color("red")
def right():
    global method
    if not sorting:
        method += 1
        if method == 6:
            method = 0
        for t in button_list:
        	t.color('#00FFFF')
        button_list[method].color("red")
def sort():  #Sorting Manager
    global sorting, swaps
    runtime = time.time()
    sorting += 1
    if sorting <= 1:
        
        if method == 0:
            selection(turtles)
            complexity = "O(n^2) comps, O(n) swaps"
        elif method == 1:
            bubble(turtles)
            complexity = "O(n^2) comps, O(n^2) swaps"
        elif method == 2:
            insertion(turtles)
            complexity = "O(n^2) comps, O(n^2) swaps"
        elif method == 3:
            cocktail(turtles)
            complexity = "O(n^2) comps, O(n^2) swaps"
        elif method == 4:
            pigeon(turtles)
            complexity = "O(n)"
        else:
            merge(turtles)
            complexity = "O(nlogn)"
    runtime -= time.time()
    runtime = str(round(-runtime,2)) + " seconds"


    draw = turtle.Turtle()
    draw.speed(0)
    draw.penup()
    draw.ht()
    draw.goto(-500 ,-200)
    draw.write(runtime,align='center', font=("Courier", 16, "normal"))
    draw.goto(-500 ,-150)
    draw.write(str(swaps) + " swaps",align='center', font=("Courier", 16, "normal"))
    draw.goto(-500 ,-100)
    draw.write(complexity + " time complexity",align='center', font=("Courier", 16, "normal"))
    time.sleep(2.5)
    window.update()


    sorting -= 1
    swaps = 0
def selection(nums):
    global swaps
    for i in range(len(nums)):
        maxpos = i
        for j in range(i, len(nums)):
            if nums[j].turtlesize() < nums[maxpos].turtlesize():
                maxpos = j
                swaps += 1

        tmp = nums[maxpos]
        nums[maxpos] = nums[i]
        nums[i] = tmp
        window.update()
        tmp = nums[maxpos].xcor()
        nums[maxpos].setx(nums[i].xcor())
        nums[i].setx(tmp)
        nums[i].color("blue") #sort 0
    #for i in nums:
    #    i.color("green")
    #    window.update()
def bubble(nums):
    global swaps
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j].turtlesize() > nums[j+1].turtlesize():
                x1 = nums[j].xcor()
                x2 = nums[j+1].xcor()
                nums[j].setx(x2)
                nums[j + 1].setx(x1)
                tmp = nums[j]
                nums[j] = nums[j+1]
                nums[j + 1] = tmp
                window.update()
                swaps += 1
        nums[i].color("blue")
        window.update()

    #for i in nums:
    #    i.color("green")
    #    window.update()
def insertion(arr):
    global swaps
    for i in range(0, len(arr)):
        to_move = arr[i]
        cnt = 0
        j = i-1

        while(j >= 0 and arr[j].turtlesize()[0] > to_move.turtlesize()[0]):
            arr[j].setx(arr[j].xcor() + 10)
            arr[j+1] = arr[j]
            j -= 1
            cnt+=1
            window.update()
            swaps += 1
        to_move.setx(to_move.xcor()+cnt*-10)
        arr[j+1] = to_move
        to_move.color('blue')
        window.update()

    #for i in arr:
    #    i.color('green')
    #    window.update()
def cocktail(arr):
    global swaps
    start = 0
    end = len(arr)-1

    while (start < end):
        for i in range(start, end, 1):
            if(arr[i].turtlesize()[0] > arr[i+1].turtlesize()[0]):
                x1 = arr[i].xcor()
                x2 = arr[i+1].xcor()
                arr[i].setx(x2)
                arr[i+1].setx(x1)
                tmp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = tmp
                window.update()
                swaps += 1
        arr[end].color('blue')
        end -= 1
        
        for i in range(end, start, -1):
            if(arr[i].turtlesize()[0] < arr[i-1].turtlesize()[0]):
                x1 = arr[i].xcor()
                x2 = arr[i-1].xcor()
                arr[i].setx(x2)
                arr[i-1].setx(x1)
                tmp = arr[i]
                arr[i] = arr[i-1]
                arr[i-1] = tmp
                window.update()
                swaps += 1
        arr[start].color('red')
        window.update()

        start+=1
    for i in arr:
        window.update()
        i.color('green')
def pigeon(arr):
    vals = [x.turtlesize()[0] for x in arr]
    mx = max(vals)
    mn = min(vals)
    rng = mx-mn+1

    narr = [None]*rng
    for t in arr:
        t.color('red')
        window.update()
        size = t.shapesize()[0]
        if narr[size - mn] is None:
            narr[size - mn] = [t]
        else:
            narr[size - mn].append(t)
    arr.reverse()
    for t in arr:      
        t.setx(-6000)
        window.update()
    '''
    for ls in narr:
        if ls != None:
            for t in ls:
                print(t.turtlesize()[0], end=" ")
    '''      
    cor = -500
    i = 1
    for ls in narr:
        if ls != None:
            for val in ls:
                val.setx(cor)
                cor+=10
                arr[-i] = val
                i += 1
                val.color('blue')
                window.update()
    arr.reverse()

    #time.sleep(0.1)
    #for t in arr:
    #    t.color('green')
    #    window.update()
def merge(arr, cnt=0, side=''):

    global swaps
    if len(arr) > 1:

        mid = len(arr)//2
 
        L = arr[:mid]
        R = arr[mid:]

        merge(L,cnt+1, 'l')
        merge(R,cnt+1, 'r')

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i].turtlesize()[0] < R[j].turtlesize()[0]:
                arr[k] = L[i]
                i += 1
                swaps += 1
            else:
                arr[k] = R[j]
                j += 1
                swaps += 1
            k += 1
 
        while i < len(L):
            arr[k] = L[i]
            swaps += 1
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            swaps += 1

            j += 1
            k += 1

        if cnt == 10:
        	if side == 'l':
	        	for i, t in enumerate(arr):
	        		t.setx(i*10 -700)
	        		t.sety(0)
	        		t.color(color_list[k])
	        		window.update()
	        if side == 'r':
	        	for i, t in enumerate(arr):
	        		t.setx(i*10 +500)
	        		t.sety(0)
	        		t.color(color_list[k])
	        		window.update()
        if cnt != 10:
	        for i, t in enumerate(arr):
	            t.setx(i*10 -500)
	            t.color(color_list[k])
	            window.update()


    if len(arr) == 100:
        for t in arr:
            t.color("blue")
            window.update()
        #for t in arr:
        #    t.color("green")
        #    window.update()

#while startt == 0:
#	start()

turtles = init()

while True:
    window.listen()
    window.onkeypress(randomize, "r")
    window.onkeypress(right, "Right")
    window.onkeypress(left, "Left")
    window.onkeypress(sort, "Return")
    window.onkeypress(exitt,"Up")
    turtle.onscreenclick(method_choose)
    window.update()
