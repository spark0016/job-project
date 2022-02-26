from tkinter import *
import tkinter
from tkinter.ttk import *
import random
import time

def smp():
    progress = Progressbar(tk, orient=HORIZONTAL, length=100, mode='indeterminate')

    sampeling_btn["state"] = DISABLED
    progress['value'] = 10

    # img = PhotoImage(file="/Users/hamidbeheshti/Desktop/NASA/Illustration2.png")
    # syring.configure(image=img)
    # syring.image = img

    NA = 140 / 75
    progress['value'] = 11
    K = 4 / 75
    CL = 100 / 75
    CA = 1.25 / 75
    PH = 7.38 / 75
    LI = .6 / 75

    NA2 = 110 / 55
    K2 = 8 / 55
    CL2 = 70 / 55
    CA2 = 2.5 / 55
    progress['value'] = 20
    PH2 = 6.83 / 55
    LI2 = 3 / 55
    progress['value'] = 35

    CAL1NA = random.randint(73, 78)
    progress['value'] = 40
    CAL1K = random.randint(73, 78)
    progress['value'] = 50
    CAL1CL = random.randint(73, 78)
    progress['value'] = 56
    CAL1CA = random.randint(73, 78)
    progress['value'] = 60
    CAL1PH = random.randint(73, 78)
    CAL1LI = random.randint(73, 78)

    CAL2NA = random.randint(53, 58)
    progress['value'] = 62
    CAL2K = random.randint(53, 58)
    CAL2CL = random.randint(53, 58)
    CAL2CA = random.randint(53, 58)
    CAL2PH = random.randint(53, 58)
    CAL2LI = random.randint(53, 58)

    resultNA1 = NA * CAL1NA
    resultK1 = K * CAL1K
    resultCL1 = CL * CAL1CL
    resultCA1 = CA * CAL1CA
    resultPH1 = PH * CAL1PH
    resultLI1 =  LI * CAL1LI

    resultNA2 = NA2 * CAL2NA
    resultK2 = K2 * CAL2K
    progress['value'] = 75
    resultCL2 = CL2 * CAL2CL
    resultCA2 = CA2 * CAL2CA
    resultPH2 = PH2 * CAL2PH
    progress['value'] = 80
    resultLI2 =  LI2 * CAL2LI
    progress['value'] = 85

    def on_closing():
        sampeling_btn["state"] = NORMAL
        root.destroy()
    progress['value'] = 100
    progress.pack(fill="both")

    root = Tk()
    root.protocol("WM_DELETE_WINDOW", on_closing)

    Label(root, text=f"mv1-NA: {CAL1NA} | CAL1: {resultNA1}").pack()
    Label(root, text=f"mv1-K: {CAL1K} | CAL1: {resultK1}").pack()
    Label(root, text=f"mv1-CL: {CAL1CL} | CAL1: {resultCL1}").pack()
    Label(root, text=f"mv1-CA: {CAL1CA} | CAL1: {resultCA1}").pack()
    Label(root, text=f"mv1-PH: {CAL1PH} | CAL1: {resultPH1}").pack()
    Label(root, text=f"mv1-LI: {CAL1LI} | CAL1: {resultLI1}").pack()

    Label(root, text="-----------------------------------------").pack()

    Label(root, text=f"mv2-NA: {CAL2NA} |  CAL2: {resultNA2}").pack()
    Label(root, text=f"mv2-K: {CAL2K} |  CAL2: {resultK2}").pack()
    Label(root, text=f"mv2-CL: {CAL2CL} |  CAL2: {resultCL2}").pack()
    Label(root, text=f"mv2-CA: {CAL2CA} |  CAL2: {resultCA2}").pack()
    Label(root, text=f"mv2-PH: {CAL2PH} |  CAL2: {resultPH2}").pack()
    Label(root, text=f"mv2-LI: {CAL2LI} |  CAL2: {resultLI2}").pack()

    root.mainloop()

tk = Tk()
tk.config(bg="#fff")
tk.geometry("800x600")
tk.minsize(width=800, height=600)
tk.maxsize(width=800, height=600)

sampeling_btn = tkinter.Button(text="Sampeling", command=smp)
sampeling_btn.place(relx=.8, rely=.5, width=120, height=50, anchor=CENTER)

img = PhotoImage(file='rsz_injection.png')
syring = Label(tk, image=img, borderwidth=0).place(relx=.3, rely=.5, anchor=CENTER)

tk.mainloop()
