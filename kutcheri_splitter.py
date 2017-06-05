from tkinter import Tk, Label, Button, StringVar
from telnetlib import Telnet
import time

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.labeltext = StringVar()
        self.labeltext.set("This is our first GUI!")
        self.label = Label(master, textvariable=self.labeltext)
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.pause_button = Button(master, text="Pause", command=self.pause)
        self.pause_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

    def pause(self):
        print("attempting to pause")
        t = Telnet('localhost',4212)
        t.write('pause\n'.encode('ascii'))
        t.close();

    def update(self):
        print("attempting to update")
        current_time = time.strftime('%H:%M:%S', time.gmtime(self.get_current_time()))
        self.labeltext.set("Current time: "+current_time)
        self.master.after(200, self.update)

    def get_current_time(self):

        t = Telnet('localhost', 4212)
        t.read_very_eager() #clear the buffer
        t.write('get_time\n'.encode('ascii'))
        time.sleep(0.1)
        current_time = int(t.read_very_eager().decode('unicode_escape'))
        return current_time

root = Tk()
my_gui = MyFirstGUI(root)
root.after(1000,my_gui.update)
root.mainloop()
root.destroy()
