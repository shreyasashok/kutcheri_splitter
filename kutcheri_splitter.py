from tkinter import *
from tkinter.ttk import *
from telnetlib import Telnet
import time
from tkentrycomplete import AutocompleteEntry
import csv

class KutcheriSplitterGUI:
    def __init__(self, master):

        self.version = '0.1beta'
        
        self.master = master
        master.title("Kutcheri Splitter "+self.version)

        self.kutcheri_details = Frame(master)
        self.kutcheri_details.pack()
        self.kutcheri_details.grid_columnconfigure(0, weight=1)

        self.status_label_text = StringVar()
        self.status_label_text.set("Status: Status goes here")
        self.status_label = Label(self.kutcheri_details,
                                  textvariable=self.status_label_text,
                                  font=(None,13))
        self.status_label.grid(row=0, column=0, columnspan=5, sticky=W, pady=(5,1), padx=5);

        self.browse_label = Label(self.kutcheri_details, text="Music folder location: ")
        self.browse_label.grid(row=1, column=0, sticky=W, pady=(5,1), padx=5, columnspan=6)

        self.music_dir_entry = Entry(self.kutcheri_details, font=(None,12), width=40)
        self.music_dir_entry.grid(row=2, column=0, padx=5, pady=1, columnspan=6, sticky=W)
        self.music_dir_browse = Button(self.kutcheri_details, text="Browse")
        self.music_dir_browse.grid(row=2, column=6, padx=5, pady=1)

        self.main_artist_label = Label(self.kutcheri_details, text="Main Artist")
        self.main_artist_label.grid(row=3, column=0, sticky=W, pady=(5,1), padx=5, columnspan=5)

        self.main_artist_entry = AutocompleteEntry(self.kutcheri_details, font=(None,12), width=40)
        self.main_artist_entry.grid(row=4, column=0, padx=5, pady=1, columnspan=5, sticky=W)

        self.violin_label = Label(self.kutcheri_details, text="Violin")
        self.violin_label.grid(row=5, column=0, sticky=W, pady=(5,1), padx=5, columnspan=5)

        self.violin_entry = AutocompleteEntry(self.kutcheri_details, font=(None,12), width=40)
        self.violin_entry.grid(row=6, column=0, padx=5, pady=1, columnspan=5, sticky=W)

        self.mridangam_label = Label(self.kutcheri_details, text="Mridangam")
        self.mridangam_label.grid(row=7, column=0, sticky=W, pady=(5,1), padx=5, columnspan=5)

        self.mridangam_entry = AutocompleteEntry(self.kutcheri_details, font=(None,12), width=40)
        self.mridangam_entry.grid(row=8, column=0, padx=5, pady=1, columnspan=5, sticky=W)

        self.ghatam_label = Label(self.kutcheri_details, text="Ghatam")
        self.ghatam_label.grid(row=9, column=0, sticky=W, pady=(5,1), padx=5, columnspan=5)

        self.ghatam_entry = AutocompleteEntry(self.kutcheri_details, font=(None,12), width=40)
        self.ghatam_entry.grid(row=10, column=0, padx=5, pady=1, columnspan=5, sticky=W)

        self.kanjira_label = Label(self.kutcheri_details, text="Kanjira")
        self.kanjira_label.grid(row=11, column=0, sticky=W, pady=(5,1), padx=5, columnspan=5)

        self.kanjira_entry = AutocompleteEntry(self.kutcheri_details, font=(None,12), width=40)
        self.kanjira_entry.grid(row=12, column=0, padx=5, pady=1, columnspan=5, sticky=W)

        self.morsing_label = Label(self.kutcheri_details, text="Morsing")
        self.morsing_label.grid(row=11, column=0, sticky=W, pady=(5,1), padx=5, columnspan=5)

        self.morsing_entry = AutocompleteEntry(self.kutcheri_details, font=(None,12), width=40)
        self.morsing_entry.grid(row=12, column=0, padx=5, pady=1, columnspan=5, sticky=W)

        self.vocal_support_label = Label(self.kutcheri_details, text="Vocal Support")
        self.vocal_support_label.grid(row=13, column=0, sticky=W, pady=(5,1), padx=5, columnspan=5)

        self.vocal_support_entry = AutocompleteEntry(self.kutcheri_details, font=(None,12), width=40)
        self.vocal_support_entry.grid(row=14, column=0, padx=5, pady=1, columnspan=5, sticky=W)

        self.other_artist_label = Label(self.kutcheri_details, text="Other Artist")
        self.other_artist_label.grid(row=15, column=0, sticky=W, pady=(5,1), padx=5, columnspan=5)

        self.other_artist_entry = AutocompleteEntry(self.kutcheri_details, font=(None,12), width=40)
        self.other_artist_entry.grid(row=16, column=0, padx=5, pady=1, columnspan=5, sticky=W)

        self.sabha_label = Label(self.kutcheri_details, text="Sabha Name")
        self.sabha_label.grid(row=17, column=0, sticky=W, pady=(25,1), padx=5, columnspan=5)

        self.sabha_entry = AutocompleteEntry(self.kutcheri_details, font=(None,12), width=40)
        self.sabha_entry.grid(row=18, column=0, padx=5, pady=1, columnspan=5, sticky=W)

        self.location_label = Label(self.kutcheri_details, text="Location (City if in India, City, State if in US)")
        self.location_label.grid(row=19, column=0, sticky=W, pady=(5,1), padx=5, columnspan=5)

        self.location_entry = AutocompleteEntry(self.kutcheri_details, font=(None,12), width=40)
        self.location_entry.grid(row=20, column=0, padx=5, pady=1, columnspan=5, sticky=W)

        self.date_label = Label(self.kutcheri_details, text="Date (YYYY-MM-DD)")
        self.date_label.grid(row=21, column=0, sticky=W, pady=(5,1), padx=5, columnspan=5)

        self.date_frame = Frame(self.kutcheri_details)
        self.date_frame.grid(row=22, column=0, sticky=W, pady=(0,5))
        
        self.year_combobox = Combobox(self.date_frame, width=20)
        self.year_combobox['values'] = ('2015', '2016', '2017') #temporary
        self.year_combobox.state(['readonly'])
        self.year_combobox.grid(row=0, column=0, pady=(5,1), padx=5)

        self.date_separator_1 = Label(self.date_frame, text="-", font=(None,12))
        self.date_separator_1.grid(row=0, column=1, pady=3)

        self.month_combobox = Combobox(self.date_frame, width=3)
        self.month_combobox['values'] = ('01', '02', '03', '04', '05', '06', '07') #temporary
        self.month_combobox.state(['readonly'])
        self.month_combobox.grid(row=0, column=2, pady=(5,1), padx=5)

        self.date_separator_2 = Label(self.date_frame, text="-", font=(None,12))
        self.date_separator_2.grid(row=0, column=3, pady=3)

        self.day_combobox = Combobox(self.date_frame, width=3)
        self.day_combobox['values'] = ('01', '02', '03', '04', '05', '06', '07','08') #temporary
        self.day_combobox.state(['readonly'])
        self.day_combobox.grid(row=0, column=4, pady=(5,1), padx=5)


##        self.test_combobox = Combobox(self.kutcheri_details, textvariable=self.status_label_text)
##        self.test_combobox['values'] = ('test1', 'test2', 'test3')
##        #self.test_combobox.state(['readonly'])
##        self.test_combobox.grid(row=3, column=0)

        #self.filedialog = filedialog.asksaveasfilename(initialdir = "/", title = "Select file")

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


#with open('RagamDatabase/ragam_list.csv', newline='') as csvfile:
#    reader = csv.reader(csvfile, delimiter=',')
#    for row in reader:
#        print(''.join(row))
    
root = Tk()
my_gui = KutcheriSplitterGUI(root)
#root.after(1000,my_gui.update)
root.mainloop()
root.destroy()
