################# import modules #############################     
from tkinter import *
import requests
import bs4
from tkinter import messagebox
###############################################################





Ans_list=[0,0,0,0,0]
global Ans_var





#################### Functions of questions #####################
def q1():
    label4=Label(lf2, text="1. Are you experiencing any of the following symptomps\n \t\tCough,Fever,Difficulty in Breathing,loss of senses of smell and test?", bg="teal", font=('Arial',12)).grid(row=0,column=0)
    button1=Button(lf2,text="Yes", command=q1_yes).grid(row=1,column=1)
    button2=Button(lf2,text="No", command=q1_no).grid(row=1,column=2)
    
def q2():
    label5=Label(lf2, text="2. Have you ever had any of the following: \n\t\tDiabetes,Hypertension,Lung disease,Heart disease,Kidney disorder   \t\t", font=('Arial',12), bg="teal").grid(row=2,column=0)
    button11=Button(lf2,text="Yes", command=q2_yes).grid(row=3,column=1)
    button12=Button(lf2,text="No", command=q2_no).grid(row=3,column=2)
def q3():
    label6=Label(lf2, text="3. Have you travelled anywhere internationally in the last \n28-45 days?", bg="teal", font=('Arial',12)).grid(row=4,column=0)
    button21=Button(lf2,text="Yes", command=q3_yes).grid(row=5,column=1)
    button22=Button(lf2,text="No", command=q3_no).grid(row=5,column=2)
def q4():
    label7=Label(lf2, text="4. Have you recently interacted or lived with someone   \nwho has tested positive for covid-19", font=('Arial',12), bg="teal").grid(row=6,column=0)
    button31=Button(lf2,text="Yes", command=q4_yes).grid(row=7,column=1)
    button32=Button(lf2,text="No", command=q4_no).grid(row=7,column=2)
def q5():
    label8=Label(lf2, text="5. Are you a healthcare worker and you examined a     \nCovid-19 confirmed case without proctetive gear", font=('Arial',12), bg="teal").grid(row=8,column=0)
    button41=Button(lf2,text="Yes",command=message).grid(row=9,column=1)
    button42=Button(lf2,text="No", command=message).grid(row=9,column=2)
def q1_yes():
    Ans_list[0]=1
    q2()
def q1_no():
    Ans_list[0]=0
    q2()

def q2_yes():
    Ans_list[1]=1
    q3()
def q2_no():
    Ans_list[1]=0
    q3()

def q3_yes():
    Ans_list[2]=1
    q4()
def q3_no():
    Ans_list[2]=0
    q4()

def q4_yes():
    Ans_list[3]=1
    q5()
def q4_no():
    Ans_list[3]=0
    q5()
    
def q5_yes():
    Ans_list[4]=1
    message()

def q5_no():
    Ans_list[4]=0
    message()

def message():
    Ans_var=0
    print(Ans_list)
    for i in range(5):
        if Ans_list[i]==1:
            Ans_var=1
            break
    print(Ans_var)
    if Ans_var==1:
        messagebox.showwarning("Test Result", "You are at Risk\nIf the information provided by you is accurate, \nit indicates that you are either unwell or at risk. \n Talk to a Doctor immediately")
    else:
        messagebox.showinfo("Test Result", "You are safe")
    
###############################################################








################ Function For Get live Updates##############################
def live_updates():
    def get_corona_datails():
        url = "https://www.mohfw.gov.in/"
        data = requests.get(url)
        bsdata = bs4.BeautifulSoup(data.text, 'html.parser')
        bsdata1 = bsdata.find_all("strong", class_="mob-hide")
        temp = []
        for i in bsdata1:
            value = i.text.strip().split()
            temp.append(value)
        return temp[1], temp[3], temp[5]
    
    activeCases, dischargedCases, deathCases = get_corona_datails()
    window1 = Tk()
    window1.geometry("800x400")
    window1.configure(bg="light pink")
    # root.iconbitmap("abc.jpg")
    window1.title("CORONA LIVE UPDATES")
    f1 = ("poppins", 25, "bold")
    lb00 = Label(window1, text="Covid-19 cases in India \n\n\n", font=f1,
             bg="light pink").grid(row=0, column=1)
    # photo = PhotoImage(file = r"C:\Users\dell\Downloads\pic.jpg",size="40x40").grid(row=0,column=2)
    lb001 = Label(window1, text="Cases:", font=f1, bg="light pink").grid(row=1, column=1)
    lb002= Label(window1, text="TOTAL (TODAY)", font=f1, bg="light pink").grid(row=1, column=2)
    lb01 = Label(window1, text="Active Cases:", font=f1, bg="light pink").grid(row=2, column=1)
    lb02 = Label(window1, text="Discharged Cases:", font=f1, bg="light pink").grid(row=3, column=1)
    lb03 = Label(window1, text="Death Cases: ", font=f1, bg="light pink").grid(row=4, column=1)
    lb1 = Label(window1, text=activeCases, font=f1, bg="light pink").grid(row=2, column=2)
    lb2 = Label(window1, text=dischargedCases, font=f1, bg="light pink").grid(row=3, column=2)
    lb3 = Label(window1, text=deathCases, font=f1, bg="light pink").grid(row=4, column=2)
    window1.mainloop()
######################################################################################








#################################### Starting window ################################
root=Tk()
root.geometry("1300x650")
root.title("CORONA TRACKER INDIA")
root.configure(background="light blue")
label1=Label(root, text="COVID-19 TRACKER WITH LIVE UPDATES", font="Helvetica 16 bold italic", fg="Black" , bg="light blue")
label1.pack()
lf=LabelFrame(root, text="Note:", bg="light green" )
lf.pack(fill="both", expand="no", padx=70, pady=30)
label2=Label(lf, text="Please note that information from this chat will be used for \nmonitoring & management of the current health crisis in the fight against COVID-19", font="Helvetica 12 bold", bg="light green")
label2.pack()
label3=Label(lf, text="If you are experiencing any of the following symptomps or \nfinding it is apply on you then please give the right answer", font="Helvetica 12 bold", fg="black", pady=20, bg="light green")
label3.pack()
lf2=LabelFrame(root, bg="teal")
lf2.pack()
q1()
frmm=Frame(root, bg="yellow").pack()
label9=Label(frmm, text="Click here for corona updates in india",  font="Helvetica 16 bold italic", bg="light blue").pack()
button0=Button(frmm, text="Updates", bg="teal" , command=live_updates).pack(pady=10)
root.mainloop()
#########################################################################################################





