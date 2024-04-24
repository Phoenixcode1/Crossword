import re
import time
import tkinter as tk
from tkinter import *
import exportToPdf as ePDF
from PIL import Image, ImageTk
import preparations as prep
import saveResults as sr
def main_menu_guziki_dele():
        canvas1.itemconfig(button1_canvas,state = "hidden")
        canvas1.itemconfig(button2_canvas,state = "hidden")
        canvas1.itemconfig(export_canvas, state = "hidden")

def main_menu_guziki_pokaz():
    canvas1.itemconfig(button1_canvas,state = "normal")
    canvas1.itemconfig(button2_canvas,state = "normal")
    canvas1.itemconfig(export_canvas, state="normal")
def opcje_menu_del():
    canvas1.itemconfig(back_button, state="hidden")
    canvas1.itemconfig(option_menu, state="hidden")
    canvas1.itemconfig(option_menu2, state="hidden")
    canvas1.itemconfig(next_button, state="hidden")


def opcje_menu_pokaz():
    canvas1.itemconfig(back_button, state="normal")
    canvas1.itemconfig(option_menu, state="normal")
    canvas1.itemconfig(option_menu2, state="normal")
    canvas1.itemconfig(next_button, state="normal")


def menu_nickow_pokaz():
    canvas1.itemconfig(back_nickow, state="normal")
    if variable.get() == "1Gracz":
        canvas1.itemconfig(entry1_canv, state="normal")
    elif variable.get() == "2 Graczy":
        canvas1.itemconfig(entry1_canv, state="normal")
        canvas1.itemconfig(entry2_canv, state="normal")
    elif variable.get() == "3 Graczy":
        canvas1.itemconfig(entry1_canv, state="normal")
        canvas1.itemconfig(entry2_canv, state="normal")
        canvas1.itemconfig(entry3_canv, state="normal")
    elif variable.get() == "4 Graczy":
        canvas1.itemconfig(entry1_canv, state="normal")
        canvas1.itemconfig(entry2_canv, state="normal")
        canvas1.itemconfig(entry3_canv, state="normal")
        canvas1.itemconfig(entry4_canv, state="normal")



def menu_nickow_def():
    canvas1.itemconfig(entry1_canv, state="hidden")
    canvas1.itemconfig(entry2_canv, state="hidden")
    canvas1.itemconfig(entry3_canv, state="hidden")
    canvas1.itemconfig(entry4_canv, state="hidden")
    canvas1.itemconfig(back_nickow,state="hidden")
    canvas1.itemconfig(next_button_nick,state="hidden")

def nick_checker():
    canvas1.itemconfig(next_button_nick, state="normal")


def open_opcje():
    # Hide the main menu
    canvas1.delete("wyniki_text")
    canvas1.delete("wyniki_background")
    main_menu_guziki_dele()
    opcje_menu_pokaz()

    # Show the new menu

def back_to_main_menu():
    print("okej")
    main_menu_guziki_pokaz()
    opcje_menu_del()

def menu_nickow():
    opcje_menu_del()
    menu_nickow_pokaz()
    canvas1.itemconfig(next_button_nick,state ="normal")

def back_to_opcje():
    menu_nickow_def()
    opcje_menu_pokaz()



def update_timer():
    global remaining_time
    zmiana_playera()
    if remaining_time > 0:
        timer_label.config(text=str(round(remaining_time, 2)))
        remaining_time-=0.1
        timer_label.after(100, update_timer)
    else:
        reset_timer()



def reset_timer():
    global remaining_time
    remaining_time = 15.0
    update_timer()
    kolej_gracza[0] += 1
    if  kolej_gracza[0]>=kolej_gracza[1]:
            kolej_gracza[0]=0






def zmiana_playera():
    player_playing.config(text="Teraz gra:" + lista_z_nickumi[kolej_gracza[0]].get())

def stop_timer():
    timer_label.destroy()


def punkty_graczy():
    lista_z_nickumi[kolej_gracza[0]].get()

def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    if hours > 0:
        return f"{hours}h:{minutes:02d}m:{seconds:.0f}s"
    elif minutes > 0:
        return f"{minutes}m:{seconds:.0f}s"
    else:
        return f"{seconds:.2f}s"






def check():
    pomylki = 1
    if haslo.lower() == input_uzytkownika.get().lower():
        koniec_gru=True
        player_end = Label(window, text="")
        player_end.grid(row=len(haslo) + 7, column=1, pady=5)
        player_end.config(text="Krzyzowke Wygral gracz :" + lista_z_nickumi[kolej_gracza[0]].get(),background="RED")
        osoba_wygrana = lista_z_nickumi[kolej_gracza[0]].get()
        pomylki=0
        stop_timer()
        czas_wynik = time.time()-poczatek_time
        sr.prepare_results(osoba_wygrana,format_time(czas_wynik),kolej_gracza[0]+1)



    i=0


    for key in dane.keys():

        if  key.lower()==input_uzytkownika.get().lower():
                y = 0
                for lable in my_entries[i:i+len(key)]:
                    lable.config(text=input_uzytkownika.get()[y])
                    y+=1

                pomylki=0




        i = i + len(key)




    if kolej_gracza[2] == "Do pomylki":
            add_kolejka=pomylki
            kolej_gracza[0]+=add_kolejka


    if  kolej_gracza[0]>=kolej_gracza[1]:
            kolej_gracza[0]=0


    zmiana_playera()

def start_gry():
  #  menu_nickow_def()
    kolej_gracza.append(int(re.search(r'\d+', str(variable.get())).group()))
    kolej_gracza.append(variable_tryb.get())
    if kolej_gracza[2] == "Na Czas":
        update_timer()

    canvas1.destroy()
    window.configure(background="black")
    n = len(max(dane, key=len))
    y=-1
    for key in dane.keys():
        y+=1
        for x in range(len(key)):
            game_enry = Label(window,text='')
            game_enry.grid(row=y, column=5+x,columnspan=1,padx= 5,pady=5)
            if x ==0 :
                game_enry.config(fg='#00FF00')
                game_enry.config(bg='#bd4519')

            my_entries.append(game_enry)


    variable3 = tk.StringVar(window)
    variable3.set("Numer 1")
    lista_punktow = []
    for x in range(len(haslo)):
        lista_punktow.insert(x,"Numer "+str(x+1))




    #option_menu3 = tk.OptionMenu(window, variable, *lista_punktow)
    #option_menu3.grid(row=len(haslo) + 2, column=0,rowspan=1, pady=5)


    info_lista = ''
    k = 1
    for vale in dane.values():
        info_lista = info_lista +str(k)+'.'+vale+'\n'
        info_labe.config(text=info_lista)
        k+=1

    print(liczba_graczy)


   # print(kolej_gracza)




def otworz_wyniki():
    try:
        with open("Wyniki.txt", "r") as file:
            wyniki = file.read()
        # Wyczyść tekst na ekranie
        canvas1.delete("wyniki_text")
        # Dodaj białe tło
        canvas1.create_rectangle(300, 250, 600, 350, fill="white", tag="wyniki_text")
        # Wypisz wyniki na ekranie
        canvas1.create_text(450, 300, text=wyniki, font=("Arial", 12), tag="wyniki_text", anchor="center")
    except IOError:
        canvas1.delete("wyniki_text")
        canvas1.create_text(450, 300, text="Błąd odczytu pliku wyników.", font=("Arial", 12), tag="wyniki_text", anchor="center")






def button2_click():
    otworz_wyniki()


# Create the main window
window = tk.Tk()
window.wm_title("Krzyzowka")
window.geometry("900x900")

my_entries = []
my_input = []

haslo = "zaliczone"
dane = prep.prepare_dict_words("Words.data")


input_uzytkownika = StringVar()

background_image = ImageTk.PhotoImage(file="background.png")


canvas1 = tk.Canvas(window, width = 900,
                    height = 900)
canvas1.grid(row=0,column=0)
canvas1.create_image( 0, 0, image = background_image,
                     anchor = "nw")

# Create the buttons

button1 = tk.Button(window, text="Button 1", command=open_opcje, background="blue", width=20, height=5)


button2 = tk.Button(window, text="Button 2", command=button2_click, background="red", width=20, height=5)


button1_canvas = canvas1.create_window(450, 500,
                                       anchor="center",
                                       window=button1)

button2_canvas = canvas1.create_window(450, 600,
                                       anchor="center",
                                       window=button2)


button_back = tk.Button(window, text="Back", command=back_to_main_menu)

back_button = canvas1.create_window(100, 600,
                                    anchor="center",
                                    window=button_back,state="hidden")

button_next = tk.Button(window, text="Next", command=menu_nickow)

next_button = canvas1.create_window(800, 600,
                                    anchor="center",
                                    window=button_next,state="hidden")


variable = tk.StringVar(window)
variable.set("1Gracz")
variable_tryb = tk.StringVar(window)
variable_tryb.set("Do pomylki")

option_menu = tk.OptionMenu(window, variable, "1 Gracz",
                         "2 Graczy", "3 Graczy", "4 Graczy")
option_menu = canvas1.create_window(450, 100,
                                    anchor="center",
                                    window=option_menu,state="hidden")
option_menu2 = tk.OptionMenu(window, variable_tryb, "Do pomylki",
                          "Na Czas")
option_menu2 = canvas1.create_window(450, 300,
                                     anchor="center",
                                     window=option_menu2,state="hidden")


def eksportuj_do_pdf():
    ePDF.export_to_pdf()
export_button = Button(canvas1, text="Eksport wyników do PDF", font=("Arial", 14), bg="lightgreen", fg="black",
                       command=eksportuj_do_pdf)
export_button.place(relx=0.7, rely=0.85, anchor="center")

export_canvas = canvas1.create_window(450, 700, anchor="center", window=export_button,state="normal")




def entry_clear(e):
    if entry1.get() == 'Player 1':
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)





entry1 = tk.Entry(window)
entry2 = tk.Entry(window)
entry3 = tk.Entry(window)
entry4 = tk.Entry(window)

entry1.insert(0,"Player 1")
entry2.insert(0,"Player 2")
entry3.insert(0,"Player 3")
entry4.insert(0,"Player 4")


entry1_canv = canvas1.create_window(200,400,anchor="center",window=entry1,state="hidden")
entry2_canv = canvas1.create_window(350,400,anchor="center",window=entry2,state="hidden")
entry3_canv = canvas1.create_window(500,400,anchor="center",window=entry3,state="hidden")
entry4_canv = canvas1.create_window(650,400,anchor="center",window=entry4,state="hidden")

button_back_nickow = tk.Button(window, text="Back", command=back_to_opcje)

back_nickow = canvas1.create_window(100, 600,
                                    anchor="center",
                                  window=button_back_nickow,state="hidden")


button_next_nick = tk.Button(window, text="Next", command=start_gry)

next_button_nick = canvas1.create_window(800, 600,
                                    anchor="center",
                                    window=button_next_nick,state="hidden")


entry1.bind("<Button-1>",entry_clear)
entry2.bind("<Button-1>",entry_clear)
entry3.bind("<Button-1>",entry_clear)
entry4.bind("<Button-1>",entry_clear)

lista_z_nickumi = []
lista_z_nickumi.append(entry1)
lista_z_nickumi.append(entry2)
lista_z_nickumi.append(entry3)
lista_z_nickumi.append(entry4)


liczba_graczy = 0
osoba_wygrana = ''
kolej_gracza=[]
kolej_gracza.append(0)

koniec_gru = False

game_enry2 = Entry(window,textvariable= input_uzytkownika)
game_enry2.grid(row= len(haslo)+3,column=1,pady=1)


button_checker = Button(window,text="Sprawdz",command=check)
button_checker.grid(row= len(haslo)+3,column=0,pady=1)

info_labe = Label(window,text='')
info_labe.grid(row=len(haslo)+4 ,column=0,pady=20)

player_playing = Label(window, text="")
player_playing.grid(row=len(haslo) + 4, column=4, pady=20)
player_playing.config(text="Teraz gra:"+lista_z_nickumi[kolej_gracza[0]].get())

timer_label = tk.Label(window, font=("Arial", 24))
timer_label.grid(row=len(haslo)+8,pady=20)
remaining_time = 15.0
czas_zmiana = 0
poczatek_time = time.time()
window.resizable(width=False, height=False)
window.mainloop()