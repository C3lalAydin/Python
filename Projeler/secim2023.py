import datetime as dt
import time
import tkinter as tk

def tarih():
    global gun
    global saat
    global dakika
    global saniye
    tarih = dt.datetime(year=2023,month=6,day=17,hour=20,minute=00,second=00)
    bugün = dt.datetime.today()
    ara=tarih-bugün
    gun=ara.days
    saat=ara.seconds//3600
    dakika=ara.seconds %3600//60
    saniye= ara.seconds - saat*3600 - dakika*60
tarih()

counter = 0
def update_label(label):
  def count():
    global counter
    counter += 1
    tarih()
    label.config(text=str("{} Gün {} Saat {} Dakika {} Saniye".format(gun,saat,dakika,saniye)))
    label.after(1000, count)
  count()

pencere = tk.Tk()
pencere.title("2023 Seçim")
pencere.geometry("500x200+450+50")
pencere.overrideredirect(True)
pencere.wm_attributes("-topmost", True)
pencere.wm_attributes("-transparentcolor", "white")


labell = tk.Label(
    pencere,
    fg="red",
    text="{} Gün {} Saat {} Dakika {} Saniye".format(gun,saat,dakika,saniye),
    font=("Comic Sans MS",20)
    )


labell.config(bg = "#cd0000")
pencere.config(bg = "#cd0000")
pencere.wm_attributes("-transparentcolor","#cd0000")
update_label(labell)

pencere.lower()
labell.pack()
pencere.mainloop()
