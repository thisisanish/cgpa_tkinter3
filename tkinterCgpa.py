from tkinter import *
from tkinter import messagebox

def grade(grd):
	dictio = {'O':10,'A+':9,'A':8,'B':7,'B-':6,'C':5,'D':4,'E':2}
	return dictio[grd]

def magicFunc(event):
	print ("Calculating !")
	gradess_second_sem = 0
	creditss_second_sem = 0
	gradess_first_sem = 0
	creditss_first_sem = 0
	for j in range (6):
		gradess_first_sem = gradess_first_sem + int(creditss_list[j].get())*(grade(grades_list[j].get()))
		creditss_first_sem = creditss_first_sem + int(creditss_list[j].get())
	gradess_first_sem = round(gradess_first_sem/creditss_first_sem,2)
	for j in range (6, 12):
		gradess_second_sem = gradess_second_sem + int(creditss_list[j].get())*(grade(grades_list[j].get()))
		creditss_second_sem = creditss_second_sem + int(creditss_list[j].get())
	gradess_second_sem = round(gradess_second_sem/creditss_second_sem,2)

	gradess_this_year = round((gradess_first_sem+gradess_second_sem)/2,2)

	if (gradess_this_year<8.5): # very very important piece of code!!!!!!
		emoji = "(︶︹︶)"
	else:
		emoji = "(̿▀̿‿ ̿▀̿ ̿)"
	messagebox.showinfo(emoji,"Final CGPA   : "+ str(gradess_this_year)+" CGPA" + "\n" + "I Sem TGPA  : "+ str(gradess_first_sem)+" CGPA" + "\n" + "II Sem TGPA : "+ str(gradess_second_sem)+" CGPA")	

top = Tk()
top.title("THE GREAT CGPA CALCUATOR")
top.configure(background="black")

CGPATEXT = Label(top, text = "The Great CGPA Calcuator", font=("Helvetica",20))
CGPATEXT.pack()

creditss_list = []
grades_list = []
sem_list=[]

L1 = Label(top, text = "¯\_(ツ)_/¯", bg="black", fg="white", font=("Helvetica",20))
L1.pack()

frame_2 = Frame()
frame_2.pack()

lbl_sem = Label(frame_2,text="Semister :")
lbl_sem.grid(row=0,column=0)
lbl_creditss = Label(frame_2,text="Credits :")
lbl_creditss.grid(row=0,column=1)
lbl_grades = Label(frame_2,text="Grades :")
lbl_grades.grid(row = 0,column=2)

for i in range (12):			
			if i<6:
				sem_list.append(Label(frame_2, text = "SEMISTER 1"))
				sem_list[i].grid(row = i+1,column = 0,padx=10,pady=10)
			else:
				sem_list.append(Label(frame_2, text = "SEMISTER 2"))
				sem_list[i].grid(row = i+1,column = 0,padx=10,pady=10)

			creditss_list.append(Spinbox(frame_2,values=(1,2,3,4,5,20)))
			creditss_list[i].grid(row = i+1,column = 1,padx=10,pady=10)
				
			grades_list.append(Spinbox(frame_2,values = ("E","D","C","B-","B","A","A+","O")))
			grades_list[i].grid(row = i+1,column=2,padx=10,pady=10)
			
btn_calcCG = Button(text="! Press with Caution !", bg="red", fg="white")
btn_calcCG.bind("<Button-1>",magicFunc)
btn_calcCG.pack(pady=8)

top.mainloop()
