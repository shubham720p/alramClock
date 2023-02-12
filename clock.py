import datetime
from threading import Thread
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
from pygame import mixer
from time import sleep

bg1 = "white"
bg2 = "violet"
bg3 = "orange"
window = Tk()
window.geometry("350x150")
window.title("MyClock")
photo = PhotoImage(file="clock.png")
window.iconphoto(False, photo)
window.configure(bg=bg1)
# frame
frame_up = Frame(window, width=400, height=5, bg=bg2)
frame_up.grid(row=0, column=0)
frame_body = Frame(window, width=400, height=145, bg=bg3)
frame_body.grid(row=1, column=0)
img = Image.open("clock1.png")
img.resize((150, 150))
img = ImageTk.PhotoImage(img)
app_image = Label(frame_body, height=100, image=img, bg=bg3)
app_image.place(x=10, y=10)
name = Label(frame_body, text="Alarm", height=1, font=("ivy 20 bold"), bg=bg3)
name.place(x=125, y=10)

minu = Label(frame_body, text="HR", height=1,
             font=("ivy 9 bold"), bg=bg3, fg="blue")
minu.place(x=127, y=40)
c_hr = Combobox(frame_body, width=2, font=('ivy 9 '))
c_hr['values'] = ('00', '01', '02', '03', '04', '05',
                  '06', '07', '08', '09', '10', '11', '12')
c_hr.current(0)
c_hr.place(x=130, y=65)
# min
minu = Label(frame_body, text="MIN", height=1,
             font=("ivy 9 bold"), bg=bg3, fg="blue")
minu.place(x=175, y=40)
c_min = Combobox(frame_body, width=2, font=('ivy 9 '))
c_min['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '23', '24', '25', '26', '27',
                   '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
c_min.current(0)
c_min.place(x=178, y=65)
# sec
sec = Label(frame_body, text="SEC", height=1,
            font=("ivy 9 bold"), bg=bg3, fg="blue")
sec.place(x=220, y=40)
c_sec = Combobox(frame_body, width=2, font=('ivy 9 '))
c_sec['values'] =('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '23', '24', '25', '26', '27',
                   '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
c_sec.current(0)
c_sec.place(x=227, y=65)
# perd
perd = Label(frame_body, text="  period", height=1,
            font=("ivy 9 bold"), bg=bg3, fg="blue")
perd.place(x=265, y=40)
c_perd = Combobox(frame_body, width=3, font=('ivy 9 '))
c_perd['values'] =('AM','PM')
c_perd.current(0)
c_perd.place(x=277, y=65)

def act_alarm():
    t = Thread(target = alr)
    t.start()
def deact_alarm():
    selected.get()
    mixer.music.stop()
selected = IntVar()
rad1 = Radiobutton(frame_body , font = ("arial 10 bold"), value = 1, text = "Activate" , bg = bg3, command = act_alarm, variable = selected)
rad1.place(x = 187, y = 95)

def alarm():
    mixer.music.load('alram.mp3')
    mixer.music.play()
    selected.set(0)

    rad2= Radiobutton(frame_body , font = ("arial 10 bold"), value = 2, text = "Off" , bg = bg3, command = deact_alarm, variable = selected)
    rad2.place(x = 125 , y = 95)


def alr():
    while True :
        control = selected.get()
        alarm_hr = c_hr.get()
        alarm_min = c_min.get()
        alarm_sec = c_sec.get()
        alarm_perd =c_perd.get()
        alarm_period = str(alarm_perd).upper()


        now = datetime.now()

        hr = now.strftime("%I")
        minut = now.strftime("%M")
        secd = now.strftime("%S")
        period = now.strftime("%p")
        
        if control ==1:
            if alarm_perd ==period:
                if alarm_hr == hr:
                    if alarm_min == minut:
                        if alarm_sec ==secd:
                            print("time to take break")
                            alarm()
        sleep(1)
        
mixer.init()


window.mainloop()
