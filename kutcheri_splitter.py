from tkinter import *
from tkinter.ttk import *
from telnetlib import Telnet
import time
from tkentrycomplete import AutocompleteEntry
import csv

class Track:
    def __init__(self, master, track_number):
        self.master = master
        self.track_number = track_number

        self.track_no = Label(self.master, text=track_number)
        self.track_no.grid(row=track_number, column=0, padx=5, pady=3)
        self.track_start = Entry(self.master, width=6)
        self.track_start.grid(row=track_number, column=1, padx=5, pady=3)
        self.track_end = Entry(self.master, width=6)
        self.track_end.grid(row=track_number, column=2, padx=5, pady=3)
        self.track_title = AutocompleteEntry(self.master, width=25)
        self.track_title.grid(row=track_number, column=3, padx=5, pady=3)
        self.track_type = AutocompleteEntry(self.master, width=8)
        self.track_type.grid(row=track_number, column=4, padx=5, pady=3)
        self.track_ragam = AutocompleteEntry(self.master, width=10)
        self.track_ragam.grid(row=track_number, column=5, padx=5, pady=3)
        self.track_talam = AutocompleteEntry(self.master, width=10)
        self.track_talam.grid(row=track_number, column=6, padx=5, pady=3)
        self.track_composer = AutocompleteEntry(self.master, width=13)
        self.track_composer.grid(row=track_number, column=7, padx=5, pady=3)
        self.alapana_var = IntVar()
        self.niraval_var = IntVar()
        self.swaram_var = IntVar()
        self.track_alapana = Checkbutton(self.master, variable=self.alapana_var)
        self.track_alapana.grid(row=track_number, column=8, padx=5, pady=3)
        self.track_niraval = Checkbutton(self.master, variable=self.niraval_var)
        self.track_niraval.grid(row=track_number, column=9, padx=5, pady=3)
        self.track_swaram = Checkbutton(self.master, variable=self.swaram_var)
        self.track_swaram.grid(row=track_number, column=10, padx=5, pady=3)
        self.track_comments = Entry(self.master, width=25)
        self.track_comments.grid(row=track_number, column=11, padx=5, pady=3)
    
    def destroy(self):
        self.track_no.destroy()
        self.track_start.destroy()
        self.track_end.destroy()
        self.track_title.destroy()
        self.track_type.destroy()
        self.track_ragam.destroy()
        self.track_talam.destroy()
        self.track_composer.destroy()
        self.track_alapana.destroy()
        self.track_niraval.destroy()
        self.track_swaram.destroy()
        self.track_comments.destroy()

class KutcheriSplitterGUI:
    def __init__(self, master):

        self.version = '0.1beta'
        
        self.master = master
        master.title("Kutcheri Splitter "+self.version)

        self.kutcheri_details = Frame(master, relief=GROOVE)
        self.kutcheri_details.pack(side=LEFT, padx=5, pady=5)
        self.kutcheri_details.grid_columnconfigure(0, weight=1)

        self.status_label_text = StringVar()
        self.status_label_text.set("Status: Status goes here")
        self.status_label = Label(self.kutcheri_details,
                                  textvariable=self.status_label_text,
                                  font=(None,13))
        self.status_label.grid(row=0, column=0, columnspan=5, sticky=W, pady=(5,1), padx=5);

        self.browse_label = Label(self.kutcheri_details, text="Music folder location: ")
        self.browse_label.grid(row=1, column=0, sticky=W, pady=(5,1), padx=5, columnspan=6)

        self.music_dir_entry = Entry(self.kutcheri_details, font=(None,12), width=30)
        self.music_dir_entry.grid(row=2, column=0, padx=5, pady=1, columnspan=6, sticky=W)
        
        self.music_dir_browse = Button(self.kutcheri_details, text="Browse")
        self.music_dir_browse.grid(row=2, column=6, padx=5, pady=1)

        self.main_artist_label = Label(self.kutcheri_details, text="Main Artist")
        self.main_artist_label.grid(row=3, column=0, sticky=W, pady=(5,1), padx=5, columnspan=5)

        self.main_artist_entry = AutocompleteEntry(self.kutcheri_details, font=(None,12), width=30)
        self.main_artist_entry.grid(row=4, column=0, padx=5, pady=1, columnspan=5, sticky=W)

        self.violin_label = Label(self.kutcheri_details, text="Violin")
        self.violin_label.grid(row=5, column=0, sticky=W, pady=(5,1), padx=5, columnspan=5)

        self.violin_entry = AutocompleteEntry(self.kutcheri_details, font=(None,12), width=30)
        self.violin_entry.grid(row=6, column=0, padx=5, pady=1, columnspan=5, sticky=W)

        self.mridangam_label = Label(self.kutcheri_details, text="Mridangam")
        self.mridangam_label.grid(row=7, column=0, sticky=W, pady=(5,1), padx=5, columnspan=5)

        self.mridangam_entry = AutocompleteEntry(self.kutcheri_details, font=(None,12), width=30)
        self.mridangam_entry.grid(row=8, column=0, padx=5, pady=1, columnspan=5, sticky=W)

        self.ghatam_label = Label(self.kutcheri_details, text="Ghatam")
        self.ghatam_label.grid(row=9, column=0, sticky=W, pady=(5,1), padx=5, columnspan=5)

        self.ghatam_entry = AutocompleteEntry(self.kutcheri_details, font=(None,12), width=30)
        self.ghatam_entry.grid(row=10, column=0, padx=5, pady=1, columnspan=5, sticky=W)

        self.kanjira_label = Label(self.kutcheri_details, text="Kanjira")
        self.kanjira_label.grid(row=11, column=0, sticky=W, pady=(5,1), padx=5, columnspan=5)

        self.kanjira_entry = AutocompleteEntry(self.kutcheri_details, font=(None,12), width=30)
        self.kanjira_entry.grid(row=12, column=0, padx=5, pady=1, columnspan=5, sticky=W)

        self.morsing_label = Label(self.kutcheri_details, text="Morsing")
        self.morsing_label.grid(row=11, column=0, sticky=W, pady=(5,1), padx=5, columnspan=5)

        self.morsing_entry = AutocompleteEntry(self.kutcheri_details, font=(None,12), width=30)
        self.morsing_entry.grid(row=12, column=0, padx=5, pady=1, columnspan=5, sticky=W)

        self.vocal_support_label = Label(self.kutcheri_details, text="Vocal Support")
        self.vocal_support_label.grid(row=13, column=0, sticky=W, pady=(5,1), padx=5, columnspan=5)

        self.vocal_support_entry = AutocompleteEntry(self.kutcheri_details, font=(None,12), width=30)
        self.vocal_support_entry.grid(row=14, column=0, padx=5, pady=1, columnspan=5, sticky=W)

        self.other_artist_label = Label(self.kutcheri_details, text="Other Artist")
        self.other_artist_label.grid(row=15, column=0, sticky=W, pady=(5,1), padx=5, columnspan=5)

        self.other_artist_entry = AutocompleteEntry(self.kutcheri_details, font=(None,12), width=30)
        self.other_artist_entry.grid(row=16, column=0, padx=5, pady=1, columnspan=5, sticky=W)

        self.audio_quality_label = Label(self.kutcheri_details, text="Audio Quality")
        self.audio_quality_label.grid(row=17, column=0, sticky=W, pady=(5,1), padx=5, columnspan=5)

        self.audio_quality_combobox = Combobox(self.kutcheri_details)
        self.audio_quality_combobox['values'] = ('good', 'average', 'potato') #temporary
        self.audio_quality_combobox.state(['readonly'])
        self.audio_quality_combobox.grid(row=18, column=0, sticky=W, pady=(5,1), padx=5, columnspan=5)

        self.sabha_label = Label(self.kutcheri_details, text="Sabha Name")
        self.sabha_label.grid(row=19, column=0, sticky=W, pady=(25,1), padx=5, columnspan=5)

        self.sabha_entry = AutocompleteEntry(self.kutcheri_details, font=(None,12), width=30)
        self.sabha_entry.grid(row=20, column=0, padx=5, pady=1, columnspan=5, sticky=W)

        self.location_label = Label(self.kutcheri_details, text="Location (City if in India, City, State if in US)")
        self.location_label.grid(row=21, column=0, sticky=W, pady=(5,1), padx=5, columnspan=5)

        self.location_entry = AutocompleteEntry(self.kutcheri_details, font=(None,12), width=30)
        self.location_entry.grid(row=22, column=0, padx=5, pady=1, columnspan=5, sticky=W)

        self.date_label = Label(self.kutcheri_details, text="Date (YYYY-MM-DD)")
        self.date_label.grid(row=23, column=0, sticky=W, pady=(5,1), padx=5, columnspan=5)

        self.date_frame = Frame(self.kutcheri_details)
        self.date_frame.grid(row=24, column=0, sticky=W, pady=(0,5), padx=2)
        
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

        self.track_details = Frame(master, relief=GROOVE)
        self.track_details.pack(side=LEFT, padx=(20,5), pady=5, fill=BOTH)

        self.back_10 = Button(self.track_details, text="<10s")
        self.back_10.grid(row=0, column=0, padx=3, pady=3)
        self.back_5 = Button(self.track_details, text="<5s")
        self.back_5.grid(row=0, column=1, padx=3, pady=3)
        self.back_1 = Button(self.track_details, text="<1s")
        self.back_1.grid(row=0,column=2, padx=3, pady=3)
        self.pause = Button(self.track_details, text="Pause/Play")
        self.pause.grid(row=0, column=3, padx=3, pady=3)
        self.forward_1 = Button(self.track_details, text="1s>")
        self.forward_1.grid(row=0, column=4, padx=3, pady=3)
        self.forward_5 = Button(self.track_details, text="5s>")
        self.forward_5.grid(row=0, column=5, padx=3, pady=3)
        self.forward_10 = Button(self.track_details, text="10s>")
        self.forward_10.grid(row=0, column=6, padx=3, pady=3)

        self.track_list = Frame(self.track_details)
        self.track_list.grid(row=1, column=0, columnspan=7, pady=(15,0), padx=2)

        self.track_no_label = Label(self.track_list, text="Track No.")
        self.track_no_label.grid(row=0, column=0, padx=(5,0))
        self.track_start_label = Label(self.track_list, text="Start")
        self.track_start_label.grid(row=0, column=1)
        self.track_end_label = Label(self.track_list, text="End")
        self.track_end_label.grid(row=0, column=2)
        self.track_title_label = Label(self.track_list, text="Song/Piece Title")
        self.track_title_label.grid(row=0, column=3)
        self.track_type_label = Label(self.track_list, text="Type")
        self.track_type_label.grid(row=0, column=4)
        self.track_ragam_label = Label(self.track_list, text="rAgam")
        self.track_ragam_label.grid(row=0, column=5)
        self.track_talam_label = Label(self.track_list, text="tALam")
        self.track_talam_label.grid(row=0, column=6)
        self.track_composer_label = Label(self.track_list, text="Composer")
        self.track_composer_label.grid(row=0, column=7)
        self.track_alapana_label = Label(self.track_list, text="A")
        self.track_alapana_label.grid(row=0, column=8)
        self.track_niraval_label = Label(self.track_list, text="N")
        self.track_niraval_label.grid(row=0, column=9)
        self.track_swaram_label = Label(self.track_list, text="S")
        self.track_swaram_label.grid(row=0, column=10)
        self.track_comments_label = Label(self.track_list, text="Comments")
        self.track_comments_label.grid(row=0, column=11)

        #self.filedialog = filedialog.asksaveasfilename(initialdir = "/", title = "Select file")
        self.t1 = Track(self.track_list, 1)
        self.t2 = Track(self.track_list, 2)
        

    def greet(self):
        print("Greetings!")

    def pause(self):
        print("attempting to pause")
        t = Telnet('localhost',4212)
        t.write('pause\n'.encode('ascii'))
        t.close();

    def update(self):
        print("attempting to update")
##        current_time = time.strftime('%H:%M:%S', time.gmtime(self.get_current_time()))
##        self.labeltext.set("Current time: "+current_time)
##        self.master.after(200, self.update)
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
root.after(1000,my_gui.update)
root.mainloop()
root.destroy()
