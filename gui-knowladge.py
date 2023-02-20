from tkinter import *
from tkinter import ttk  #theme of tk
from tkinter import messagebox
import random

gui = Tk()  #หน้าจอหลักของโปรแกรม
gui.title('พยากรสำหรับวันนี้ของคุณ')
gui.geometry('500x400')

L1 = Label(gui,text = 'วันนี้คุณจะรู้สึกเช่นไร',font =('Angsana New',18), fg = 'green')
L1.place(x=180, y=80)
#b1 = ttk.Button(gui,text = 'เงินมีอยู่กี่บาท')
#b1.pack(ipadx = 20, ipady = 20) #แนวแกน x,y จะถูกบวกขึ้นอีก 20
############################################
def button2 (): #button2 ชื่อฟังก์ชั่น    
    randomnum = random.randint(1, 3)    
    if randomnum == 1:
        text = 'วันนี้เป็นวันที่ดีมากจริงๆ '
        messagebox.showwarning('Have a good Day', text) #มี show info / warning / error
    elif randomnum == 2:
        text = 'ว้าว...วันนี้มันสุดยอดจริงๆ'
        messagebox.showinfo ('Have a Nice Day', text) #มี show info / warning / error
    else:
        text = 'ก็แค่วันธรรมดาวันหนึ่ง เดี๋ยวมันก็ผ่านไป'
        messagebox.showerror ('Normal Day', text) #มี show info / warning / error
fb1 = Frame(gui) #มี labelFrame(gui,text = 'Money')
fb1.place(x=190, y=130)
b2 = ttk.Button(fb1,text = 'พยากรวันนี้', command = button2)#เอา button ไปไว้ใน กระดาน fb1
#b2.pack(ipadx = 20, ipady = 20) #แนวแกน x,y จะถูกบวกขึ้นอีก 20
b2.pack(ipadx = 20, ipady = 20)  #กำหนดโลเคชั่นให้ปุ่ม สามารถเพิ่ม padx กับ pady ได้อีกเพื่อ labelframe ห่างจากปุ่ม
##############################################
gui.mainloop()
