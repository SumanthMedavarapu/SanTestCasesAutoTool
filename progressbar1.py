







def percentageCalculator(x, y, case=1):
    """Calculate percentages
       Case1: What is x% of y?
       Case2: x is what percent of y?
       Case3: What is the percentage increase/decrease from x to y?
    """
    if case == 1:
        #Case1: What is x% of y?
        r = x/100*y
        return r
    elif case == 2:
        #Case2: x is what percent of y?
        r = x/y*100
        return r
    elif case == 3:
        #Case3: What is the percentage increase/decrease from x to y?
        r = (y-x)/x*100
        return r
    else:
        raise Exception("Only case 1,2 and 3 are available!")







"""root = Tk()
root.title("App v0.1")
root.geometry("600x320")

#root.iconbitmap(os.path.join(os.getcwd(), 'favicon.ico'))

#fields = 'input1', 'input2', 'input4', 'input5', 'input6'
fields = 'input1'

ents = makeform(root, fields)

runButton = Button(root, text='Start downloading', command=(lambda : runActions(progress, status)))#e=ents:
percent = Label(root, text="", anchor=S) 
progress = Progressbar(root, length=500, mode='determinate')    
status = Label(root, text="Click button to start process..", relief=SUNKEN, anchor=W, bd=2) 


runButton.pack(pady=15)
percent.pack()
progress.pack()
status.pack(side=BOTTOM, fill=X)

root.mainloop()




functions = [Dupport, PowerPlan]
And loop over them:

n = int(input('Number: '))
for i in range(n):
    functions[i]()"""
