import datetime as dt
import tkinter as tk



def tarih():
    global gun
    bugün = dt.datetime.today()
    tarih = dt.datetime(year=bugün.year+1,month=2,day=1)
    ara=tarih-bugün
    gun=ara.days
tarih()

counter = 0

#Label Update
def update_label(label):
  def count():
    global counter
    counter += 1
    tarih()
    label.config(text=str("Doğum Gününe {} Gün Kaldı".format(gun)))
    label.after(1000, count)
  count()

pencere = tk.Tk()
pencere.geometry("500x200+450+50")
pencere.overrideredirect(True)
pencere.wm_attributes("-topmost", True)
pencere.wm_attributes("-transparentcolor", "white")


labell = tk.Label(
    pencere,
    fg="red",
    text="Doğum Gününe {} Gün Kaldı".format(gun),
    font=("Comic Sans MS",20)
    )

#Arka Plan Silme
labell.config(bg = "#cd0000")
pencere.config(bg = "#cd0000")
pencere.wm_attributes("-transparentcolor","#cd0000")
update_label(labell)

pencere.lower()
labell.pack()
pencere.mainloop()
