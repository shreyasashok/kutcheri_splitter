from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import *
from telnetlib import Telnet
import time
from tkentrycomplete import AutocompleteEntry, AutocompleteCombobox
import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import httplib2
from pydub import AudioSegment
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

class Track:
    def __init__(self, master, autocomplete_dict, track_number):
        self.master = master
        self.track_number = track_number

        self.track_no = Label(self.master, text=track_number)
        self.track_no.grid(row=track_number, column=0, padx=3, pady=2)
        
        self.track_start = Entry(self.master, width=6)
        self.track_start.grid(row=track_number, column=1, padx=3, pady=2)
        
        self.track_end = Entry(self.master, width=6)
        self.track_end.grid(row=track_number, column=2, padx=3, pady=2)
        
        self.track_title = AutocompleteCombobox(self.master, width=33)
        self.track_title.bind('<FocusOut>', self.track_select)
        self.track_title.grid(row=track_number, column=3, padx=3, pady=2)
        
        self.track_type = AutocompleteCombobox(self.master, width=10)
        self.track_type.grid(row=track_number, column=4, padx=3, pady=2)
        
        self.track_ragam = AutocompleteCombobox(self.master, width=23)
        self.track_ragam.grid(row=track_number, column=5, padx=3, pady=2)
        
        self.track_talam = AutocompleteCombobox(self.master, width=10)
        self.track_talam.grid(row=track_number, column=6, padx=3, pady=2)
        
        self.track_composer = AutocompleteCombobox(self.master, width=23)
        self.track_composer.grid(row=track_number, column=7, padx=3, pady=2)
        
        self.alapana_var = StringVar()
        self.niraval_var = StringVar()
        self.swaram_var = StringVar()
        self.alapana_var.set('n')
        self.niraval_var.set('n')
        self.swaram_var.set('n')
        
        self.track_alapana = Checkbutton(self.master, variable=self.alapana_var, onvalue='y', offvalue='n')
        self.track_alapana.grid(row=track_number, column=8, padx=3, pady=2)
        
        self.track_niraval = Checkbutton(self.master, variable=self.niraval_var, onvalue='y', offvalue='n')
        self.track_niraval.grid(row=track_number, column=9, padx=3, pady=2)
        
        self.track_swaram = Checkbutton(self.master, variable=self.swaram_var, onvalue='y', offvalue='n')
        self.track_swaram.grid(row=track_number, column=10, padx=3, pady=2)
        
        self.track_comments = Entry(self.master, width=25)
        self.track_comments.grid(row=track_number, column=11, padx=3, pady=2)

        self.autocomplete_dict = autocomplete_dict

        self.track_type.set_completion_list(self.autocomplete_dict['type'])
        self.track_ragam.set_completion_list(self.autocomplete_dict['ragam'])
        self.track_talam.set_completion_list(self.autocomplete_dict['talam'])
        self.track_composer.set_completion_list(self.autocomplete_dict['composer'])
        self.track_title.set_completion_list(list(self.autocomplete_dict['krithi'].keys()))
    
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

    def track_select(self, event):
        print("Unfocus: attempting to autocomplete krithi")
        krithi_name = self.track_title.get()
        if krithi_name in self.autocomplete_dict['krithi']:
            self.track_type.set(self.autocomplete_dict['krithi'][krithi_name][0])
            self.track_ragam.set(self.autocomplete_dict['krithi'][krithi_name][1])
            self.track_talam.set(self.autocomplete_dict['krithi'][krithi_name][2])
            self.track_composer.set(self.autocomplete_dict['krithi'][krithi_name][3])

    def set_start(self, time):
        self.track_start.delete(0, END)
        self.track_start.insert(0,str(time))

    def set_end(self, time):
        self.track_end.delete(0, END)
        self.track_end.insert(0, str(time))

    def get_start(self):
        return float(self.track_start.get().strip())

    def get_end(self):
        return float(self.track_end.get().strip())

    def get_label(self):
        if self.track_ragam.get() == '':
            return self.track_start.get().strip()+'\t'+self.track_end.get().strip()+'\t'+self.track_title.get().strip()+'\n'
        else:
            return self.track_start.get().strip()+'\t'+self.track_end.get().strip()+'\t'+self.track_title.get().strip()+', '+self.track_ragam.get().strip()+'\n'

    def get_filename(self):
        if self.track_ragam.get() == '':
            return self.track_title.get().strip()+'.mp3'
        else:
            return self.track_title.get().strip()+', '+self.track_ragam.get().strip()+'.mp3'
        
    def get_title(self):
        if self.track_ragam.get() == '':
            return self.track_title.get().strip()
        else:
            return self.track_title.get().strip()+', '+self.track_ragam.get().strip()

    def get_csv(self):
        return [self.track_title.get(), self.track_type.get(), self.track_ragam.get(), self.track_talam.get(), self.track_composer.get(), self.alapana_var.get(), self.niraval_var.get(), self.swaram_var.get(), self.track_comments.get()]

    def get_save_string(self):
        return self.track_start.get()+'|'+self.track_end.get()+'|'+self.track_title.get()+'|'+self.track_type.get()+'|'+self.track_ragam.get()+'|'+self.track_talam.get()+'|'+self.track_composer.get()+'|'+self.alapana_var.get()+'|'+self.niraval_var.get()+'|'+self.swaram_var.get()+'|'+self.track_comments.get()+'\n'

    def set_save_string(self, save_string):
        save_string_split = save_string.split('|')
        self.track_start.delete(0,END)
        self.track_start.insert(0,save_string_split[0])
        self.track_end.delete(0,END)
        self.track_end.insert(0,save_string_split[1])
        self.track_title.delete(0,END)
        self.track_title.insert(0,save_string_split[2])
        self.track_type.delete(0,END)
        self.track_type.insert(0,save_string_split[3])
        self.track_ragam.delete(0,END)
        self.track_ragam.insert(0,save_string_split[4])
        self.track_talam.delete(0,END)
        self.track_talam.insert(0,save_string_split[5])
        self.track_composer.delete(0,END)
        self.track_composer.insert(0,save_string_split[6])
        self.alapana_var.set(save_string_split[7])
        self.niraval_var.set(save_string_split[8])
        self.swaram_var.set(save_string_split[9])
        self.track_comments.delete(0,END)
        self.track_comments.insert(0,save_string_split[10])
            
class KutcheriSplitterGUI:
    def __init__(self, master):

        self.version = '0.1beta'
        
        self.master = master
        master.title("Kutcheri Splitter "+self.version)

        self.kutcheri_details = Frame(master, relief=GROOVE)
        self.kutcheri_details.pack(side=LEFT, padx=(5,0), pady=5)
        self.kutcheri_details.grid_columnconfigure(0, weight=1)

        self.status_label_text = StringVar()
        self.set_status("Loading autocompletes...")
        self.status_label = Label(self.kutcheri_details,
                                  textvariable=self.status_label_text,
                                  font=(None,13))
        self.status_label.grid(row=0, column=0, columnspan=5, sticky=W, pady=(5,1), padx=5);

        self.browse_label = Label(self.kutcheri_details, text="Music folder location: ")
        self.browse_label.grid(row=1, column=0, sticky=W, pady=(5,1), padx=5, columnspan=6)

        self.music_dir_entry = Entry(self.kutcheri_details, font=(None,12), width=25)
        self.music_dir_entry.grid(row=2, column=0, padx=5, pady=1, columnspan=6, sticky=W)
        default_path = os.path.expanduser('~\Music')
        self.music_dir_entry.insert(0, default_path)
        
        self.music_dir_browse = Button(self.kutcheri_details, text="Browse", command=self.browse)
        self.music_dir_browse.grid(row=2, column=6, padx=5, pady=1)

        self.file_browse_label = Label(self.kutcheri_details, text="Concert file location: ")
        self.file_browse_label.grid(row=3, column=0, sticky=W, pady=(5,1), padx=5, columnspan=6)

        self.file_browse_entry = Entry(self.kutcheri_details, font=(None,12), width=25)
        self.file_browse_entry.grid(row=4, column=0, padx=5, pady=1, columnspan=6, sticky=W)
                
        self.file_browse = Button(self.kutcheri_details, text="Browse", command=self.file_browse)
        self.file_browse.grid(row=4, column=6, padx=5, pady=1)

        self.main_artist_label = Label(self.kutcheri_details, text="Main Artist")
        self.main_artist_label.grid(row=5, column=0, sticky=W, pady=(4,1), padx=5, columnspan=5)

        self.main_artist_entry = AutocompleteEntry(self.kutcheri_details, font=(None,12), width=25)
        self.main_artist_entry.grid(row=6, column=0, padx=5, pady=1, columnspan=5, sticky=W)

        self.violin_label = Label(self.kutcheri_details, text="Violin")
        self.violin_label.grid(row=7, column=0, sticky=W, pady=(4,1), padx=5, columnspan=5)

        self.violin_entry = AutocompleteEntry(self.kutcheri_details, font=(None,12), width=25)
        self.violin_entry.grid(row=8, column=0, padx=5, pady=1, columnspan=5, sticky=W)

        self.mridangam_label = Label(self.kutcheri_details, text="Mridangam")
        self.mridangam_label.grid(row=9, column=0, sticky=W, pady=(4,1), padx=5, columnspan=5)

        self.mridangam_entry = AutocompleteEntry(self.kutcheri_details, font=(None,12), width=25)
        self.mridangam_entry.grid(row=10, column=0, padx=5, pady=1, columnspan=5, sticky=W)

        self.ghatam_label = Label(self.kutcheri_details, text="Ghatam")
        self.ghatam_label.grid(row=11, column=0, sticky=W, pady=(4,1), padx=5, columnspan=5)

        self.ghatam_entry = AutocompleteEntry(self.kutcheri_details, font=(None,12), width=25)
        self.ghatam_entry.grid(row=12, column=0, padx=5, pady=1, columnspan=5, sticky=W)

        self.kanjira_label = Label(self.kutcheri_details, text="Kanjira")
        self.kanjira_label.grid(row=13, column=0, sticky=W, pady=(4,1), padx=5, columnspan=5)

        self.kanjira_entry = AutocompleteEntry(self.kutcheri_details, font=(None,12), width=25)
        self.kanjira_entry.grid(row=14, column=0, padx=5, pady=1, columnspan=5, sticky=W)

        self.morsing_label = Label(self.kutcheri_details, text="Morsing")
        self.morsing_label.grid(row=15, column=0, sticky=W, pady=(4,1), padx=5, columnspan=5)

        self.morsing_entry = AutocompleteEntry(self.kutcheri_details, font=(None,12), width=25)
        self.morsing_entry.grid(row=16, column=0, padx=5, pady=1, columnspan=5, sticky=W)

        self.vocal_support_label = Label(self.kutcheri_details, text="Vocal Support")
        self.vocal_support_label.grid(row=17, column=0, sticky=W, pady=(4,1), padx=5, columnspan=5)

        self.vocal_support_entry = AutocompleteEntry(self.kutcheri_details, font=(None,12), width=25)
        self.vocal_support_entry.grid(row=18, column=0, padx=5, pady=1, columnspan=5, sticky=W)

        self.other_artist_label = Label(self.kutcheri_details, text="Other Artist")
        self.other_artist_label.grid(row=19, column=0, sticky=W, pady=(4,1), padx=5, columnspan=5)

        self.other_artist_entry = AutocompleteEntry(self.kutcheri_details, font=(None,12), width=25)
        self.other_artist_entry.grid(row=20, column=0, padx=5, pady=1, columnspan=5, sticky=W)

        self.audio_quality_label = Label(self.kutcheri_details, text="Audio Quality")
        self.audio_quality_label.grid(row=21, column=0, sticky=W, pady=(4,1), padx=5, columnspan=5)

        self.audio_quality_combobox = Combobox(self.kutcheri_details)
        self.audio_quality_combobox['values'] = ('good', 'average', 'potato')
        self.audio_quality_combobox.state(['readonly'])
        self.audio_quality_combobox.grid(row=22, column=0, sticky=W, pady=(4,1), padx=5, columnspan=5)

        self.sabha_label = Label(self.kutcheri_details, text="Sabha Name")
        self.sabha_label.grid(row=23, column=0, sticky=W, pady=(4,1), padx=5, columnspan=5)

        self.sabha_entry = AutocompleteEntry(self.kutcheri_details, font=(None,12), width=25)
        self.sabha_entry.grid(row=24, column=0, padx=5, pady=1, columnspan=5, sticky=W)

        self.location_label = Label(self.kutcheri_details, text="Location (City if in India, City, State if in US)")
        self.location_label.grid(row=25, column=0, sticky=W, pady=(4,1), padx=5, columnspan=5)

        self.location_entry = AutocompleteEntry(self.kutcheri_details, font=(None,12), width=25)
        self.location_entry.grid(row=26, column=0, padx=5, pady=1, columnspan=5, sticky=W)

        self.date_label = Label(self.kutcheri_details, text="Date (YYYY-MM-DD)")
        self.date_label.grid(row=27, column=0, sticky=W, pady=(4,1), padx=5, columnspan=5)

        self.date_frame = Frame(self.kutcheri_details)
        self.date_frame.grid(row=28, column=0, sticky=W, pady=(0,5), padx=2)
        
        self.year_combobox = Combobox(self.date_frame, width=7)
        self.year_combobox['values'] = ('1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025') #temporary
        self.year_combobox.state(['readonly'])
        self.year_combobox.grid(row=0, column=0, pady=(4,1), padx=5)

        self.date_separator_1 = Label(self.date_frame, text="-", font=(None,12))
        self.date_separator_1.grid(row=0, column=1, pady=2)

        self.month_combobox = Combobox(self.date_frame, width=3)
        self.month_combobox['values'] = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12') #temporary
        self.month_combobox.state(['readonly'])
        self.month_combobox.grid(row=0, column=2, pady=(4,1), padx=5)

        self.date_separator_2 = Label(self.date_frame, text="-", font=(None,12))
        self.date_separator_2.grid(row=0, column=3, pady=2)

        self.day_combobox = Combobox(self.date_frame, width=3)
        self.day_combobox['values'] = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31') #temporary
        self.day_combobox.state(['readonly'])
        self.day_combobox.grid(row=0, column=4, pady=(4,1), padx=5)

        self.controls_frame = Frame(self.kutcheri_details)
        self.controls_frame.grid(row=29, column=0, sticky=W, pady=15, padx=2)
        
        self.save_button = Button(self.controls_frame, text="Save", command=self.save)
        self.save_button.grid(row=0, column=0, padx=5)
        
        self.load_button = Button(self.controls_frame, text="Load", command=self.load)
        self.load_button.grid(row=0, column=1, padx=5)

        self.generate_button = Button(self.controls_frame, text="Generate", command=self.generate)
        self.generate_button.grid(row=0, column=2, padx=5)
        

        self.track_details = Frame(master, relief=GROOVE)
        self.track_details.pack(side=LEFT, padx=(20,5), pady=5, fill=BOTH)

        self.back_10 = Button(self.track_details, text="<10s", command=lambda: self.seek(-10))
        self.back_10.grid(row=0, column=0, padx=3, pady=3)
        self.back_5 = Button(self.track_details, text="<5s", command=lambda: self.seek(-5))
        self.back_5.grid(row=0, column=1, padx=3, pady=3)
        self.back_1 = Button(self.track_details, text="<1s", command=lambda: self.seek(-1))
        self.back_1.grid(row=0,column=2, padx=3, pady=3)
        self.pause = Button(self.track_details, text="Pause/Play", command=self.pause)
        self.pause.grid(row=0, column=3, padx=3, pady=3)
        self.forward_1 = Button(self.track_details, text="1s>", command=lambda: self.seek(1))
        self.forward_1.grid(row=0, column=4, padx=3, pady=3)
        self.forward_5 = Button(self.track_details, text="5s>", command=lambda: self.seek(5))
        self.forward_5.grid(row=0, column=5, padx=3, pady=3)
        self.forward_10 = Button(self.track_details, text="10s>", command=lambda: self.seek(10))
        self.forward_10.grid(row=0, column=6, padx=3, pady=3)

        self.splitting = False
        self.start_split = Button(self.track_details, text="Start Split", command=self.start_split)
        self.start_split.grid(row=1, column=0, padx=3, pady=3)
        self.end_split = Button(self.track_details, text="End Split", command=self.end_split)
        #self.end_split.config(state='disabled') #deferring button disabling till a later release
        self.end_split.grid(row=1, column=1, padx=3, pady=3)
        self.end_start_split = Button(self.track_details, text="End/Start Split", command=self.end_start_split)
        #self.end_start_split.config(state='disabled') #deferring button disabling till a later release
        self.end_start_split.grid(row=1, column=2, padx=3, pady=3)
        self.new_track = Button(self.track_details, text="New Track", command=self.add_track)
        self.new_track.grid(row=1, column=3, padx=3, pady=3)
        self.delete_last_track = Button(self.track_details, text="Delete Last Track", command=self.delete_last_track)
        self.delete_last_track.grid(row=1, column=4, padx=3, pady=3)

        self.track_list = Frame(self.track_details)
        self.track_list.grid(row=2, column=0, columnspan=7, pady=(15,0), padx=2)

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

        self.has_loaded_autocompletes=False

        self.tracks = []
        self.client = None

    def load_google_credentials(self):
        try: 
            scope = ['https://spreadsheets.google.com/feeds']
            creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
            self.client = gspread.authorize(creds)
        except TimeoutError:
            print('Request timed out. Trying again.')
            self.load_google_credentials()
        except httplib2.ServerNotFoundError:
            print('Can''t connect to database. Google credentials will not be loaded.')

    def load_autocompletes(self):
        print('Loading autocompletes')
        flatten = lambda l: [item for sublist in l for item in sublist]
        try:
            if self.client is not None:
                database = self.client.open('Kutcheri Splitter Database')
            else:
                print('Google credentials don''t seem to be loaded. Will not attempt to connect to database.')
                return
        except IOError:
            print('Can''t connect to database. Autocompletes will not be loaded.')
            return
                    
        self.autocomplete_dict = dict()
        
        type_sheet = database.get_worksheet(1)
        self.autocomplete_dict['type'] = flatten(type_sheet.get_all_values())
        
        ragam_sheet = database.get_worksheet(2)
        self.autocomplete_dict['ragam'] = flatten(ragam_sheet.get_all_values())

        talam_sheet = database.get_worksheet(3)
        self.autocomplete_dict['talam'] = flatten(talam_sheet.get_all_values())

        composer_sheet = database.get_worksheet(4)
        self.autocomplete_dict['composer'] = flatten(composer_sheet.get_all_values())

        main_artist_sheet = database.get_worksheet(5)
        self.autocomplete_dict['main_artist'] = flatten(main_artist_sheet.get_all_values())

        violin_sheet = database.get_worksheet(6)
        self.autocomplete_dict['violin'] = flatten(violin_sheet.get_all_values())

        mridangam_sheet = database.get_worksheet(7)
        self.autocomplete_dict['mridangam'] = flatten(mridangam_sheet.get_all_values())

        ghatam_sheet = database.get_worksheet(8)
        self.autocomplete_dict['ghatam'] = flatten(ghatam_sheet.get_all_values())

        kanjira_sheet = database.get_worksheet(9)
        self.autocomplete_dict['kanjira'] = flatten(kanjira_sheet.get_all_values())

        morsing_sheet = database.get_worksheet(10)
        self.autocomplete_dict['morsing'] = flatten(morsing_sheet.get_all_values())

        vocal_support_sheet = database.get_worksheet(11)
        self.autocomplete_dict['vocal_support'] = flatten(vocal_support_sheet.get_all_values())

        other_artist_sheet = database.get_worksheet(12)
        self.autocomplete_dict['other_artist'] = flatten(other_artist_sheet.get_all_values())

        sabha_sheet = database.get_worksheet(13)
        self.autocomplete_dict['sabha'] = flatten(sabha_sheet.get_all_values())

        krithi_sheet = database.get_worksheet(0)
        krithi_info_raw = krithi_sheet.get_all_records()        
        krithi_info = dict()
        for record in krithi_info_raw:
            krithi_info[record['krithi']] = (record['type'], record['ragam'], record['talam'], record['composer'])
        self.autocomplete_dict['krithi'] = krithi_info
                
        self.main_artist_entry.set_completion_list(self.autocomplete_dict['main_artist'])
        self.violin_entry.set_completion_list(self.autocomplete_dict['violin'])
        self.mridangam_entry.set_completion_list(self.autocomplete_dict['mridangam'])
        self.ghatam_entry.set_completion_list(self.autocomplete_dict['ghatam'])
        self.kanjira_entry.set_completion_list(self.autocomplete_dict['kanjira'])
        self.morsing_entry.set_completion_list(self.autocomplete_dict['morsing'])
        self.vocal_support_entry.set_completion_list(self.autocomplete_dict['vocal_support'])
        self.other_artist_entry.set_completion_list(self.autocomplete_dict['other_artist'])
        self.sabha_entry.set_completion_list(self.autocomplete_dict['sabha'])
        
    def add_track(self):
        self.tracks.append(Track(self.track_list, self.autocomplete_dict, len(self.tracks)+1))

    def delete_last_track(self):
        if (len(self.tracks) > 1):
            self.tracks[-1].destroy()
            self.tracks.pop() #take it off the stack

    def start_split(self):
        current_time = self.get_current_time()
        self.tracks[-1].set_start(current_time)

    def end_split(self):
        current_time = self.get_current_time()
        self.tracks[-1].set_end(current_time)

    def end_start_split(self):
        current_time = self.get_current_time()
        self.tracks[-1].set_end(current_time)
        self.add_track()
        self.tracks[-1].set_start(current_time)

    def pause(self):
        print("Attempting to pause")
        t = Telnet('localhost', 4212)
        t.write('pause\n'.encode('ascii'))
        t.close();

    def seek(self, seek_amount):
        print("Attempting to seek")
        current_time_raw = self.get_current_time()
        if (current_time_raw == -1):
            print("VLC connection problem, can't seek")
        else:
            new_time = current_time_raw+seek_amount
            t = Telnet('localhost', 4212)
            command ='seek '+str(new_time)+'\n'
            t.write(command.encode('ascii'))
            t.close()
            new_time_raw = self.get_current_time()
            if (new_time_raw == current_time_raw): #this means that we were paused, so we need to unpause, seek, then pause again
                print('Quick unpause to seek')
                t = Telnet('localhost', 4212)
                command ='pause\nseek '+str(new_time)+'\npause'
                t.write(command.encode('ascii'))
                t.read_very_eager()
                time.sleep(0.1)
                t.close()

    def browse(self):
        print("Opening file browser")
        filename = filedialog.askdirectory(initialdir = "~", title = "Select music folder")
        filename = os.path.normcase(filename)
        print(filename)
        self.music_dir_entry.delete(0, END)
        self.music_dir_entry.insert(0,str(filename))

    def file_browse(self):
        print("Opening file browser")
        filename = filedialog.askopenfilename(initialdir = "~", title = "Select concert file")
        filename = os.path.normcase(filename)
        print(filename)
        self.file_browse_entry.delete(0, END)
        self.file_browse_entry.insert(0,str(filename))

    def save(self):
        print("Opening file browser")
        filename = filedialog.asksaveasfilename(initialdir = "~", title = "Create save file", defaultextension=".split", filetypes=[("Split files", "*.split")])
        filename = os.path.normcase(filename)
        if not filename:
            return
        with open(filename, "w") as save_file:
            save_file.write(self.file_browse_entry.get()+'|'+self.main_artist_entry.get()+'|'+self.violin_entry.get()+'|'+self.mridangam_entry.get()+'|'+self.ghatam_entry.get()+'|'+
                            self.kanjira_entry.get()+'|'+self.morsing_entry.get()+'|'+self.vocal_support_entry.get()+'|'+self.other_artist_entry.get()+'|'+self.audio_quality_combobox.get()+'|'+
                            self.sabha_entry.get()+'|'+self.location_entry.get()+'|'+self.year_combobox.get()+'|'+self.month_combobox.get()+'|'+self.day_combobox.get())
            for track in self.tracks:
                save_file.write(track.get_save_string())
                

    def load(self):
        print("Opening file browser")
        filename = filedialog.askopenfilename(initialdir = "~", title = "Open save file", defaultextension=".split", filetypes=[("Split files", "*.split")])
        filename = os.path.normcase(filename)
        if not filename:
            return

        while (len(self.tracks) > 1):
            self.tracks[-1].destroy()
            self.tracks.pop()

        with open(filename, "r") as load_file:
            album_data = load_file.readline()
            album_data_split = album_data.split("|")
            self.file_browse_entry.delete(0,END)
            self.file_browse_entry.insert(0,album_data_split[0])
            self.main_artist_entry.delete(0,END)
            self.main_artist_entry.insert(0,album_data_split[1])
            self.violin_entry.delete(0,END)
            self.violin_entry.insert(0,album_data_split[2])
            self.mridangam_entry.delete(0,END)
            self.mridangam_entry.insert(0,album_data_split[3])
            self.ghatam_entry.delete(0,END)
            self.ghatam_entry.insert(0,album_data_split[4])
            self.kanjira_entry.delete(0,END)
            self.kanjira_entry.insert(0,album_data_split[5])
            self.morsing_entry.delete(0,END)
            self.morsing_entry.insert(0,album_data_split[6])
            self.vocal_support_entry.delete(0,END)
            self.vocal_support_entry.insert(0,album_data_split[7])
            self.other_artist_entry.delete(0,END)
            self.other_artist_entry.insert(0,album_data_split[8])
            self.audio_quality_combobox.set(album_data_split[9])
            self.sabha_entry.delete(0,END)
            self.sabha_entry.insert(0,album_data_split[10])
            self.location_entry.delete(0,END)
            self.location_entry.insert(0,album_data_split[11])
            self.year_combobox.set(album_data_split[12])
            self.month_combobox.set(album_data_split[13])
            self.day_combobox.set(album_data_split[14])

            first_track = True
            while True:
                current_line = load_file.readline()
                if not current_line:
                    break
                if first_track:
                    self.tracks[0].set_save_string(current_line)
                    first_track = False
                else:
                    self.add_track()
                    self.tracks[-1].set_save_string(current_line)
            
        
    def update(self):
        print("Update")
        if (self.has_loaded_autocompletes == False):
            self.load_google_credentials()
            self.load_autocompletes()
            self.has_loaded_autocompletes = True
            self.tracks.append(Track(self.track_list, self.autocomplete_dict, len(self.tracks)+1))
            self.set_status("Connecting to VLC...")
        current_time_raw = self.get_current_time()
        if (current_time_raw == -1):
            self.set_status("Error connecting to VLC")
        else:
            current_time = time.strftime('%H:%M:%S', time.gmtime(current_time_raw))
            self.set_status("Current time: "+current_time+" ("+str(current_time_raw)+"s)")
        self.master.after(450, self.update)

    def set_status(self, status):
        self.status_label_text.set(status)
    
    def get_current_time(self):
    
        try:
            t = Telnet('localhost', 4212)
            t.read_very_eager() #clear the buffer
            t.write('get_time\n'.encode('ascii'))
            time.sleep(0.1)
            message = t.read_very_eager().decode('unicode_escape')
            t.close()

            messages = message.splitlines()
            for current_message in messages:
                if (current_message.isdigit()):
                    current_time = int(current_message)
                    return current_time
            print("No messages matched spec")
            return -1
        except ConnectionRefusedError:
            print("ConnectionRefusedError")
            return -1
        except ValueError:
            print("ValueError")
            print(message)
            return -1
        except ConnectionResetError:
            print("ConnectionResetError")
            return -1

    def generate(self):
        print('Generating the files...')
        self.set_status('Generating...(takes a while)')
        all_artists_name = ', '.join(filter(None,[self.main_artist_entry.get(), self.violin_entry.get(), self.mridangam_entry.get(), self.ghatam_entry.get(), self.kanjira_entry.get(), self.morsing_entry.get(), self.vocal_support_entry.get(), self.other_artist_entry.get()]))
        main_artists_name = ', '.join(filter(None,[self.main_artist_entry.get(), self.violin_entry.get(), self.mridangam_entry.get()]))
        album_date = self.year_combobox.get()+'-'+self.month_combobox.get()+'-'+self.day_combobox.get()
        album_title = main_artists_name+' - '+', '.join(filter(None,[self.sabha_entry.get(), self.location_entry.get()]))+' - '+album_date
        year = self.year_combobox.get()
        genre = 'Carnatic'

        music_folder = self.music_dir_entry.get()
        metadata_file_path = music_folder+'/'+album_title+"/Tags.xml"
        metadata_file_path = os.path.normpath(metadata_file_path)
        labels_file_path = music_folder+'/'+album_title+"/Labels.txt"
        labels_file_path = os.path.normpath(labels_file_path)
        csv_file_path = music_folder+'/'+album_title+"/Spreadsheet.csv"
        csv_file_path = os.path.normpath(csv_file_path)
        print("Metadata path: "+metadata_file_path)
        print("Labels path: "+labels_file_path)
        print("CSV path: "+csv_file_path)

        os.makedirs(music_folder+'/'+album_title, exist_ok=True)
        print("Writing Metadata File")
        with open(metadata_file_path, "w") as metadata_file:
            metadata_file.write('<tags>\n')
            metadata_file.write('\t<tag name="ALBUM" value="'+album_title+'"/>\n')
            metadata_file.write('\t<tag name="ARTIST" value="'+all_artists_name+'"/>\n')
            metadata_file.write('\t<tag name="YEAR" value="'+year+'"/>\n')
            metadata_file.write('\t<tag name="GENRE" value="Carnatic"/>\n')
            metadata_file.write('</tags>')

        print("Writing Labels File")
        with open(labels_file_path, "w") as labels_file:
            for track in self.tracks:
                labels_file.write(track.get_label())

        #now generate csv file
        print("Writing CSV File")
        album_csv_data = ["", self.audio_quality_combobox.get(), self.main_artist_entry.get(), self.violin_entry.get(), self.mridangam_entry.get(), self.ghatam_entry.get(), self.kanjira_entry.get(), self.morsing_entry.get(), self.vocal_support_entry.get(), self.other_artist_entry.get(), self.sabha_entry.get(), self.location_entry.get(), self.year_combobox.get(), album_date]
        with open(csv_file_path, "w") as csv_file:
            for track in self.tracks:
                track_csv_data = track.get_csv()
                full_csv_data = track_csv_data + album_csv_data
                full_csv_data_string = ','.join('"{0}"'.format(d) for d in full_csv_data)
                full_csv_data_string = full_csv_data_string+'\n'
                csv_file.write(full_csv_data_string)

        #split audio 
        print("Splitting audio")
        input_file = AudioSegment.from_file(self.file_browse_entry.get())
        output_tracks = []
        for track in self.tracks:
            track_start = int(track.get_start()*1000)
            track_end = int(track.get_end()*1000)
            track_file = input_file[track_start:track_end]
            track_file.export(music_folder+'/'+album_title+'/'+track.get_filename(), format='mp3', tags={'title':track.get_title(),'album':album_title, 'artist':all_artists_name, 'year':year, 'genre':'Carnatic'}, parameters=['-write_xing', '0'])

        #generate YouTube background
        print("Generating YouTube background")
        font = ImageFont.truetype("arial.ttf", 25)
        font_color = (230,230,230)
        for track in self.tracks:
            blank_bg = Image.open("background.png")
            draw_bg = ImageDraw.Draw(blank_bg)
            draw_bg.text((300,210), track.get_title(), font_color, font=font)
            draw_bg.text((300,290), self.sabha_entry.get()+', '+self.location_entry.get()+' '+year, font_color, font=font)
            draw_bg.text((300,370), "Main Artist: "+self.main_artist_entry.get(), font_color, font=font)
            draw_bg.text((300,410), "Violinist: "+self.violin_entry.get(), font_color, font=font)
            draw_bg.text((300,450), "Mridangist: "+self.mridangam_entry.get(), font_color, font=font)
            current_y = 490

            if self.ghatam_entry.get():
                draw_bg.text((300,current_y), "Ghatam: "+self.ghatam_entry.get(), font_color, font=font)
                current_y += 40
            if self.kanjira_entry.get():
                draw_bg.text((300,current_y), "Kanjira: "+self.kanjira_entry.get(), font_color, font=font)
                current_y += 40
            if self.morsing_entry.get():
                draw_bg.text((300,current_y), "Morsing: "+self.morsing_entry.get(), font_color, font=font)
                current_y += 40
            if self.vocal_support_entry.get():
                draw_bg.text((300,current_y), "Vocal Support: "+self.vocal_support_entry.get(), font_color, font=font)
                current_y += 40
            if self.other_artist_entry.get():
                draw_bg.text((300,current_y), "Other Artist: "+self.other_artist_entry.get(), font_color, font=font)
                current_y += 40    
            
            blank_bg.save(music_folder+'/'+album_title+'/'+track.get_title()+'.png')
               
        #Write to google docs
        if self.client is not None:
            print("Writing to Google Docs")
            print("Reauthenticating with API")
            self.load_google_credentials()
            print("Opening Database Sheet")
            archive = self.client.open('Carnatic Concert Recording Archive')
            staging_sheet = archive.get_worksheet(1)
                    
            for track in self.tracks:
                print("Writing row to google docs...")
                track_csv_data = track.get_csv()
                full_csv_data = track_csv_data + album_csv_data
                staging_sheet.insert_row(full_csv_data,2)

            print("Done generating!")
            messagebox.showinfo("Kutcheri Splitter", "Generation Complete!")
        else:
            print('Google credentials don''t seem to be loaded. Will not write to Google Docs.')
                               

def flatten_list(l):
    return [item for sublist in l for item in sublist] 
    
root = Tk()
my_gui = KutcheriSplitterGUI(root)
root.after(100,my_gui.update)
root.mainloop()

    
