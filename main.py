import mysql.connector
import mysql.connector as sqltor
from tkinter import *
import random
import tkinter as tk
from tkinter import ttk
import winsound
from PIL import *
from PIL import Image, ImageTk
from tkinter import ttk
import webbrowser
import requests
from transformers import pipeline
import time


#start of GUI
window=tk.Tk()
window.title("VARP Mangement program")
window.attributes("-fullscreen",True)

#notebook deployed
notebook = ttk.Notebook(window)
notebook.place(x=0,y=0)

#frames
frame1 = ttk.Frame(notebook,width=10000,height=900)

frame2 = ttk.Frame(notebook,width=10000,height=900)

frame3 = ttk.Frame(notebook,width=10000,height=900)

frame4 =  ttk.Frame(notebook,width=10000,height=900)

frame5 =  ttk.Frame(notebook,width=10000,height=900)

frame6 =  ttk.Frame(notebook,width=10000,height=900)

frame7 =  ttk.Frame(notebook,width=10000,height=900)

frame8 =  ttk.Frame(notebook,width=10000,height=900)

frame9 =  ttk.Frame(notebook,width=10000,height=900)

frame10 =  ttk.Frame(notebook,width=10000,height=900)

frame11 =  ttk.Frame(notebook,width=10000,height=900)

frame12 = ttk.Frame(notebook,width=10000,height=900)

frame13 = ttk.Frame(notebook,width=10000,height=900)

frame14 = ttk.Frame(notebook,width=10000,height=900)

frame15 =  ttk.Frame(notebook,width=10000,height=900)

frame16 =  ttk.Frame(notebook,width=10000,height=900)

frame17 =  ttk.Frame(notebook,width=10000,height=900)

frame18 =  ttk.Frame(notebook,width=10000,height=900)

frame19 =  ttk.Frame(notebook,width=10000,height=900)

frame20 =  ttk.Frame(notebook,width=10000,height=900)

frame21 =  ttk.Frame(notebook,width=10000,height=900)

frame22 =  ttk.Frame(notebook,width=10000,height=900)


#frames placed
frame1.place(x=0,y=0)

frame2.place(x=0,y=0)

frame3.place(x=0,y=0)

frame4.place(x=0,y=0)

frame5.place(x=0,y=0)

frame6.place(x=0,y=0)

frame7.place(x=0,y=0)

frame8.place(x=0,y=0)

frame9.place(x=0,y=0)

frame10.place(x=0,y=0)

frame11.place(x=0,y=0)

frame12.place(x=0,y=0)

frame13.place(x=0,y=0)

frame14.place(x=0,y=0)

frame15.place(x=0,y=0)

frame16.place(x=0,y=0)

frame17.place(x=0,y=0)

frame18.place(x=0,y=0)

frame19.place(x=0,y=0)

frame20.place(x=0,y=0)

frame21.place(x=0,y=0)

frame22.place(x=0,y=0)

#frames deployed
notebook.add(frame1, text='0')

notebook.add(frame2, text='1')

notebook.add(frame3, text='2')

notebook.add(frame4, text='3')

notebook.add(frame5, text='4')

notebook.add(frame6, text='5')

notebook.add(frame7, text='6')

notebook.add(frame8, text='7')

notebook.add(frame9, text='8')

notebook.add(frame10, text='9')

notebook.add(frame11, text='10')

notebook.add(frame12, text='11')

notebook.add(frame13, text='12')

notebook.add(frame14, text='13')

notebook.add(frame15, text='14')

notebook.add(frame16, text='15')

notebook.add(frame17, text='16')

notebook.add(frame18,text='17')

notebook.add(frame19, text='18')

notebook.add(frame20, text='19')

notebook.add(frame21, text='20')

notebook.add(frame22, text='21')

######################sql data##############
mycon=sqltor.connect(host="localhost",user='root',passwd='vrishank',database='data')

#creating cursor
cursor=mycon.cursor(buffered=True)
cursor2=mycon.cursor(buffered=True)
cursor3=mycon.cursor(buffered=True)
    #selecting the data
sql = '''SELECT * from userdata'''
sql2 = '''SELECT * from gmail_id'''
sql3 = '''SELECT * from phone'''
    #Executing the query
cursor.execute(sql)
cursor2.execute(sql2)
cursor3.execute(sql3)

#fetching data from sql
userdata_sql=cursor.fetchall()
userdata_sql2=cursor2.fetchall()
userdata_sql3=cursor3.fetchall()

k=dict(userdata_sql)
#proper list in python
gmail=[]
phone=[]

#to store data in the properlist
for t in userdata_sql2:
    for x in t:
        gmail.append(x)

for t in userdata_sql3:
    for x in t:
        phone.append(x)
        
tor=gmail
torP=phone
print(tor)

    #ending
cursor.close()
cursor2.close()
cursor3.close()
mycon.close()
###################################################


#hiding the tab tiles
style=ttk.Style()
style.layout('TNotebook.Tab',[])

#variables
winsound.PlaySound('music.wav',winsound.SND_ASYNC  + winsound.SND_LOOP)


e=0

#commands(switch if and else before sumission)

def deleaC():
    eaC.place_forget()
def deleaC2():
    eaC2.place_forget()
def play_music():
    global e
    e+=1
    if e%2==0:
        print(e)
        winsound.PlaySound('music.wav',winsound.SND_ASYNC  + winsound.SND_LOOP)
    else:
        print(e)
        winsound.PlaySound(None, winsound.SND_PURGE)


def go_to_settings():
    notebook.select(1)
def go_to_entry():
    notebook.select(2)
def go_to_login():
    notebook.select(7)

def go_to_main_menu():
    notebook.select(0)

def signinG():
    username=E1.get()
    password=E2.get()
    g=E3.get()
    if E1.get()=='' or E2.get()=='' or E3.get()=='':
        global e85
        e85=Label(frame4,text="details are not filled",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='red')
        e85.place(x=600,y=300,height=30)
        ##window.after(800,dele85)
    else:
        if username in k:
            if g in tor:
                global ea5
                ea5=Label(frame4,text='gmail is already in use',font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='green')
                ea5.place(x=500,y=450)
                ##########window.after(500,del5)
            else:
                ea5=Label(frame4,text='username already taken,chose a new one',font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='green')
                ea5.place(x=500,y=450)
                #########window.after(500,del5)
        elif username not in k:
            if g not in tor:
                import smtplib
                server=smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.login("botforproject@gmail.com", "bbvogbdgqrwewvqw")#dprzhddfvxtotxxb
                import random
                x=E3.get()
                global y
                y=random.randint(1000,9999)
                global n
                n=str(y)
                if x==g:
                    server.sendmail("botforproject@gmail.com",x,n)
                    server.quit()
                else:
                    pass
                notebook.select(5)
##############################phone
def signinP():
    username=E4.get()
    password=E5.get()
    p=E6.get()#############################change
    if E4.get()=='' or E5.get()=='' or E6.get()=='':
        global e85
        e85=Label(frame5,text="details are not filled",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='red')
        e85.place(x=600,y=300,height=30)
        ############window.after(800,dele85)
    else:
        if username in k:
            if p in torP:
                global ea5
                ea5=Label(frame5,text='phone is already in use',font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='green')
                ea5.place(x=500,y=450)
                ##window.after(500,del5)
            else:
                ea5=Label(frame5,text='username already taken,chose a new one',font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='green')
                ea5.place(x=500,y=450)
                ##window.after(500,del5)
        elif username not in k:
            if p not in torP:
                print('starting')
                import random
                x=E6.get()
                global y
                y=random.randint(1000,9999)
                global n
                n=str(y)
                if x==p:
                    import twilio
                    import twilio.rest
                    from twilio.rest import Client

                    # Your Twilio account is deleted use ur own SID and auth token
                    
                    client = Client(account_sid, auth_token)
                    try:
                        message = client.messages.create(
                            from_='+13642048913',
                            body=n,
                            to='+91'+x
                            )
                        print('chala gaya message')
                    except:
                        print('failure')
                else:
                    pass
                notebook.select(6)

def login_check():
    #sql
    mycon=sqltor.connect(host="localhost",user='root',passwd='vrishank',database='data')

    #creating cursor
    cursor=mycon.cursor(buffered=True)
    #selecting the data
    sql = '''SELECT * from userdata'''

    #Executing the query
    cursor.execute(sql)


    #fetching data from sql
    userdata_sql=cursor.fetchall()

    k=dict(userdata_sql)
    username= E8.get()
    password= E9.get()
    if username in k and password ==k[username]:
        global ea
        ea=Label(frame8,text='login approved',font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='green')
        ea.place(x=500,y=450)
        notebook.select(8)
        ##window.after(800,dele)
        E9.delete(0, END)
        
    elif username not in k:
        global ea1
        ea1=Label(frame8,text='username invalid',font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='red')
        ea1.place(x=500,y=450)
        ##window.after(800,del1)
    elif username in k and password !=k[username]:
        global ea2
        ea2=Label(frame8,text='password invalid',font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='red')
        ea2.place(x=500,y=450)
        ##window.after(800,del2)
    

    #ending
    cursor.close()
    mycon.close()

    
def go_to_sign_in_gmail():
    notebook.select(3)
def go_to_sign_in_phone():
    notebook.select(4)

def otp_check():
    z=E7.get()
    u=str(z)
    if E7.get()=='':
        global e86
        e86=Label(frame6,text="otp not given",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='red')
        e86.place(x=600,y=300,height=30)
        ##window.after(800,dele86)
    else:
        username=E1.get()
        password=E2.get()
        g=E3.get()
        if u==n:
            window.after(400,go_to_main_menu)
            global ea3
            ea3=Label(frame6,text='sign up approved',font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='green')
            ea3.place(x=500,y=450)
            ##window.after(400,del3)
            #connection
            mycon=sqltor.connect(host="localhost",user='root',passwd='vrishank',database='data')

            #making cursor
            cursor=mycon.cursor()

            #adding data through cursor
            cursor.execute("insert into userdata(username,password) values(%s,%s)",(username, password))
            mycon.commit()
#insert into userdata values(%s,%s)",(username, password))
            #end
            cursor.close()
            mycon.close()
            #saving gmail id
            mycon1=sqltor.connect(host="localhost",user='root',passwd='vrishank',database='data')

            #making cursor
            cursor=mycon1.cursor()

            #adding data through cursor
            cursor.execute("insert into gmail_id(gmail) value(%s)",[g])
            mycon1.commit()

            cursor.close()
            mycon1.close()
            E1.delete(0, END)
            E2.delete(0, END)
            E3.delete(0, END)
        elif u!=n:
            global ea4
            ea4=Label(frame6,text='OTP was wrong',font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='red')
            ea4.place(x=500,y=450)
            ##window.after(800,del4)
            print('this',u)





#####################################phone
def otp_checkP():
    z=E11.get()
    u=str(z)
    if E6.get()=='':
        global e86
        e86=Label(frame7,text="otp given",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='red')
        e86.place(x=600,y=300,height=30)
        ########window.after(800,dele86)
    else:
        username=E4.get()
        password=E5.get()
        p=E6.get()###############################################change
        if u==n:
            window.after(400,go_to_main_menu)
            global ea3
            ea3=Label(frame7,text='sign up approved',font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='green')
            ea3.place(x=500,y=450)
            ####window.after(400,del3)
            #connection
            mycon=sqltor.connect(host="localhost",user='root',passwd='vrishank',database='data')

            #making cursor
            cursor=mycon.cursor()

            #adding data through cursor
            cursor.execute("insert into userdata(username,password) values(%s,%s)",(username, password))
            mycon.commit()
#insert into userdata values(%s,%s)",(username, password))
            #end
            cursor.close()
            mycon.close()
            #saving gmail id
            mycon1=sqltor.connect(host="localhost",user='root',passwd='vrishank',database='data')

            #making cursor
            cursor=mycon1.cursor()

            #adding data through cursor
            cursor.execute("insert into phone(phone) value(%s)",[p])
            mycon1.commit()

            cursor.close()
            mycon1.close()
            E1.delete(0, END)
            E2.delete(0, END)
            E3.delete(0, END)
        elif u!=n:
            global ea4
            ea4=Label(frame7,text='OTP was wrong',font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='red')
            ea4.place(x=500,y=450)
            ##window.after(800,del4)
            print('this',u)
def general():
    from chatterbot import ChatBot
    from chatterbot.trainers import ChatterBotCorpusTrainer

    # Create a new instance of a ChatBot
    bot = ChatBot(
        'StandaloneBot',
        logic_adapters=[
            'chatterbot.logic.MathematicalEvaluation',  # Add the MathematicalEvaluation logic adapter
            'chatterbot.logic.BestMatch',  # Add the BestMatch logic adapter
        ]
    )

    # Create a trainer
    trainer = ChatterBotCorpusTrainer(bot)

    # Train the bot on English language data
    trainer.train('chatterbot.corpus.english')

    # Basic greeting responses
    basic_greetings = ['hello', 'hi', 'hey', 'how are you', 'good day']
    response_to_greetings = 'Hello! How can I assist you today?'
    
    user_input = E10.get()
    global eaC
    if user_input.lower() in basic_greetings:
        eaC=Label(frame9,text="The answer from script: {}".format(response_to_greetings),font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='red')
        eaC.place(x=50,y=150)
        window.after(4000,deleaC)
        print('Bot:', response_to_greetings)
    elif user_input.lower()=='great job':
        eaC=Label(frame9,text="Thank you",font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='red')
        eaC.place(x=50,y=150)
        window.after(4000,deleaC)
        print('thank you') 
    else:
        response = bot.get_response(user_input)
        eaC=Label(frame9,text="The answer from script: {}".format(response),font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='red')
        eaC.place(x=50,y=150)
        window.after(4000,deleaC)
        print('Bot:', response)



def transformer():
    global file_path
    if clicked.get()=='general':
        general()
    elif clicked.get()=='Coal Mine Act':
        file_path = "1952.txt"
    elif clicked.get()=='Indian explosive Act':
        file_path = "1884.txt"
    elif clicked.get()=='Colliery Control order':
        file_path = "2000.txt"
    elif clicked.get()=='Colliery Control rules':
        file_path = "2004.txt"
    elif clicked.get()=='Coal Mine Regulation':
        file_path="R2017.txt"
    elif clicked.get()=='Payment of Wages':
        file_path="2017.txt"
       
    question_answering = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    question=E10.get()
    global eaC
    result = question_answering(question=question, context=text)
    eaC=Label(frame9,text="The answer from script: {}".format(result["answer"]),font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='red')
    eaC.place(x=50,y=150)
    window.after(6000,deleaC)
    print("Answer from script:", result["answer"])
'''    
def transformer2():
    global file_path
    if clicked.get()=='general':
        general()
    elif clicked.get()=='Coal Mine Act':
        file_path = "1952.txt"
    elif clicked.get()=='Indian explosive Act':
        file_path = "1884.txt"
    elif clicked.get()=='Colliery Control order':
        file_path = "2000.txt"
    elif clicked.get()=='Colliery Control rules':
        file_path = "2004.txt"
    elif clicked.get()=='Coal Mine Regulation':
        file_path="R2017"
    elif clicked.get()=='Payment of Wages':
        file_path="2017"
        
    question_answering = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    question=E10.get()
    global result
    result = question_answering(question=question, context=text)
    global eaC
    eaC=Label(frame9,text="The answer from script: {}".format(result["answer"]),font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='red')
    eaC.place(x=50,y=150)
    window.after(1500,deleaC)
    print("Answer from script:", result["answer"])

'''
def API():
    url = "https://chatgpt-api8.p.rapidapi.com/"
    question=E10.get()

    payload = [
            {
                    "content": question+' explain more about this',
                    "role": "user"
            }
    ]
    headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "da622ea81amshdb63bcf0ce1811ep118467jsnc0e72a65fff5",
            "X-RapidAPI-Host": "chatgpt-api8.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)
    global eaC2
    eaC2=Label(frame9,text="The answer from API: {}".format(response.json()),font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='red')
    eaC2.place(x=50,y=150)
    window.after(6000,deleaC2)
    print('answer from api',response.json())

###main page##
button=Button(frame1,text="settings",width=8,height=2,bg="#afd6de",font= ('Helvetica 10 bold'),command=go_to_settings)
button.place(x=1210,y=0)

button=Button(frame1,text="sign up",width=20,height=14,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_entry)
button.place(x=700,y=100)

button=Button(frame1,text="login",width=20,height=14,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_login)
button.place(x=180,y=100)



###settings page####
button=Button(frame2,text="MUSIC",width=24,height=4,bg="#afd6de",font= ('Helvetica 25 bold'),command=play_music)
button.place(x=400,y=100)

button=Button(frame2,text="MAIN MENU",width=24,height=4,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_main_menu)
button.place(x=400,y=300)

l1=Label(frame2,text="SETTINGS",font=('Helvetica 35 bold'))
l1.place(x=510,y=30,height=37)



####sign_up page- 2 buttons#########
l2=Label(frame3,text="SIGN UP",font=('Helvetica 35 bold'))
l2.place(x=550,y=50,height=37)

button=Button(frame3,text="With Gmail",width=24,height=4,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_sign_in_gmail)
button.place(x=400,y=150)

button=Button(frame3,text="With Phone Number",width=24,height=4,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_sign_in_phone)
button.place(x=400,y=350)

button=Button(frame3,text="MAIN MENU",width=16,height=2,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_main_menu)
button.place(x=485,y=550)



###main sign_up gmail pg##############
button=Button(frame4,text="MAIN MENU",width=16,height=2,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_main_menu)
button.place(x=250,y=540)

l1=Label(frame4,text="Username: ",font=('Helvetica 22 bold'))
l1.place(x=260,y=180,height=25)

Name=StringVar()
E1=Entry(frame4,textvariable=Name,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E1.place(x=430,y=175)

l2=Label(frame4,text="Password: ",font=('Helvetica 22 bold'))
l2.place(x=260,y=280,height=25)


password=StringVar()
E2=Entry(frame4,textvariable=password,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E2.place(x=430,y=275)

l3=Label(frame4,text="Gmail: ",font=('Helvetica 22 bold'))
l3.place(x=320,y=385,height=25)

gmail=StringVar()
E3=Entry(frame4,textvariable=gmail,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E3.place(x=430,y=380)

button=Button(frame4,text="verification",width=16,height=2,bg="#afd6de",font= ('Helvetica 25 bold'),command=signinG)
button.place(x=750,y=540)



#########main sign_up phone number pg#####
button=Button(frame5,text="MAIN MENU",width=16,height=2,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_main_menu)
button.place(x=250,y=540)

l1=Label(frame5,text="Username: ",font=('Helvetica 22 bold'))
l1.place(x=260,y=180,height=25)

NameP=StringVar()
E4=Entry(frame5,textvariable=NameP,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E4.place(x=430,y=175)

l2=Label(frame5,text="Password: ",font=('Helvetica 22 bold'))
l2.place(x=260,y=280,height=25)


passwordP=StringVar()
E5=Entry(frame5,textvariable=passwordP,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E5.place(x=430,y=275)

l3=Label(frame5,text="Phone No.: ",font=('Helvetica 22 bold'))
l3.place(x=250,y=385,height=25)

phone=StringVar()
E6=Entry(frame5,textvariable=phone,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E6.place(x=430,y=380)

button=Button(frame5,text="verification",width=16,height=2,bg="#afd6de",font= ('Helvetica 25 bold'),command=signinP)
button.place(x=750,y=540)


############otp page for email##########
button=Button(frame6,text="MAIN MENU",width=16,height=2,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_main_menu)
button.place(x=250,y=540)

button=Button(frame6,text="verification",width=16,height=2,bg="#afd6de",font= ('Helvetica 25 bold'),command=otp_check)
button.place(x=750,y=540)

l1=Label(frame6,text="enter OTP: ",font=('Helvetica 22 bold'))
l1.place(x=260,y=375,height=25)

ote=StringVar()
E7=Entry(frame6,textvariable=ote,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E7.place(x=430,y=370)


################otp page for phone number###########
button=Button(frame7,text="MAIN MENU",width=16,height=2,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_main_menu)
button.place(x=250,y=540)

button=Button(frame7,text="verification",width=16,height=2,bg="#afd6de",font= ('Helvetica 25 bold'),command=otp_checkP)
button.place(x=750,y=540)

l1=Label(frame7,text="enter OTP: ",font=('Helvetica 22 bold'))
l1.place(x=260,y=375,height=25)

oteP=StringVar()
E11=Entry(frame7,textvariable=oteP,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E11.place(x=430,y=370)



#################login page##############
button=Button(frame8,text="MAIN MENU",width=16,height=2,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_main_menu)
button.place(x=250,y=540)

l1=Label(frame8,text="username: ",font=('Helvetica 22 bold'))
l1.place(x=260,y=250,height=25)

Name_login=StringVar()
E8=Entry(frame8,textvariable=Name_login,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E8.place(x=430,y=245)

l2=Label(frame8,text="password: ",font=('Helvetica 22 bold'))
l2.place(x=260,y=350,height=25)

password=StringVar()
E9=Entry(frame8,textvariable=password,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E9.place(x=430,y=345)

button=Button(frame8,text="login",width=16,height=2,bg="#afd6de",font= ('Helvetica 25 bold'),command=login_check)
button.place(x=750,y=540)

#################chatbot##########

l2=Label(frame9,text="TYPE YOUR QUESTION: ",font=('Helvetica 22 bold'))
l2.place(x=20,y=600,height=25)


question=StringVar()
E10=Entry(frame9,textvariable=question,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E10.place(x=360,y=595)

'''
button=Button(frame9,text="Detailed check",width=12,height=1,bg="#afd6de",font= ('Helvetica 25 bold'),command=transformer2)
button.place(x=30,y=480)
'''

button=Button(frame9,text="More Info",width=12,height=1,bg="#afd6de",font= ('Helvetica 25 bold'),command=API)
button.place(x=1000,y=480)

button=Button(frame9,text="Enter",width=12,height=1,bg="#afd6de",font= ('Helvetica 25 bold'),command=transformer)
button.place(x=515,y=480)


button=Button(frame9,text="settings",width=6,height=1,bg="#afd6de",font= ('Helvetica 10 bold'),command=go_to_settings)
button.place(x=1210,y=0)


# Dropdown menu options
options = ['general','Coal Mine Act','Indian explosive Act','Colliery Control order','Colliery Control rules','Coal Mine Regulation','Payment of Wages']

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set("general")

# Create Dropdown menu
drop = OptionMenu(frame9 , clicked , *options )
drop.place(x=1100,y=595)


