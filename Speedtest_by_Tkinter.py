import speedtest
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk

def down():
    st = speedtest.Speedtest()
    #print(st.download())
    sp=str(st.download())
    msg = messagebox.showinfo( "Download Speed",sp[:2]+"mbps" )
def up():
    st = speedtest.Speedtest()
    #print(st.upload())
    sp=str(st.upload())
    msg = messagebox.showinfo( "Upload Speed",sp[:2]+"mbps" )

root = Tk()
root.iconbitmap("Computer_icon.ico")
root.title("SpeedTest By Okala")
# root.geometry("224x300") # todo : This is the default size of window
root.minsize(220,295)
root.maxsize(230,305)
framehome=Frame(root,bg="red")
framehome.pack(fill=BOTH,expand=True)
imagehome=PhotoImage(file="speed_test.png")
label1=ttk.Label(framehome,image=imagehome)
label1.pack(fill=BOTH,expand=True)

create_button_1 = Button(framehome, text = "Download Speed", command = down,fg="white",bg="black",padx=10,pady=8)
# B.place(x = 50,y = 50)
create_button_1.pack()
create_button_2 = Button(framehome, text = "Upload Speed", command = up,fg="white",bg="black",padx=18,pady=8)
# B.place(x = 50,y = 90)
create_button_2.pack()
root.mainloop()

"""
down(st)
up(st)
"""
