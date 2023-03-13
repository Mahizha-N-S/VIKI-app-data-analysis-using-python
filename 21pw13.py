from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
window=Tk()
window.title("DATA ANALYSIS")
window.geometry('600x450+200+40')
TitlesDf = pd.read_csv("C:/Users/mahiz/OneDrive/Desktop/python package/title.csv")
CreditsDf = pd.read_csv("C:/Users/mahiz/OneDrive/Desktop/python package/credits.csv")
v=StringVar()
y=StringVar()
name=StringVar()
def graph1():
    screen2=Toplevel(window)
    screen2.geometry('900x600+200+40')
    screen2.resizable(False,False)
    idList = TitlesDf["id"].to_list()
    selectedActor = CreditsDf[CreditsDf.name == name.get()]["id"].to_list()

    movies = {}
    for id in selectedActor:
        movies[id] = [
                    " ".join(TitlesDf[TitlesDf.id == id]["title"].to_string().split()[1:]), 
                      float(TitlesDf[TitlesDf.id == id]["tmdb_score"].to_string().split()[1])
                      ]

    xAxis = []
    yAxis = []

    for key in movies.keys():
        xAxis.append(movies[key][0])
        yAxis.append(movies[key][1])

   # print(xAxis, yAxis)
    plt.rcParams.update({'font.size':6})
    fig=plt.Figure(figsize=(20,6), dpi=100)
    fig.add_subplot(111).bar(xAxis,yAxis,color="#57a1f8", width=0.5)
    chart=FigureCanvasTkAgg(fig,screen2)
    chart.get_tk_widget().pack()
    screen2.mainloop()
def graph2():
    screen2 = Toplevel(window)
    screen2.geometry('900x600+200+40')
    screen2.resizable(False, False)
    
    releaseYear = TitlesDf[TitlesDf.production_countries == name.get()]["release_year"].to_list()
    
    yearWiseCount = {}
    for year in releaseYear:
        if year in yearWiseCount:
            yearWiseCount[year] += 1
        else:
            yearWiseCount[year] = 1
            
    print(yearWiseCount)
    
    years = yearWiseCount.keys()
    
    count = [yearWiseCount[year] for year in years]
    
    print(years, count)
    
    plt.rcParams.update({'font.size':10})
    fig=plt.Figure(figsize=(25,6), dpi=85)
    fig.add_subplot(111).bar(years,count,color="#57a1f8", width=0.5)
    chart=FigureCanvasTkAgg(fig,screen2)
    chart.get_tk_widget().pack()
    screen2.mainloop()

def graph3():
    screen3 = Toplevel(window)
    screen3.geometry('1200x600+90+40')
    screen3.resizable(False, False)
    year=int(name.get())
    ids = TitlesDf[TitlesDf.release_year == year]["id"]
    
    ratings = []
    
    for id in ids:
        ratings.append([TitlesDf[TitlesDf.id == id]["imdb_score"].to_list(), id])
    
    ratings.sort()
    
    ratings = ratings[::-1]
    
    for rating in ratings:
        if rating[0][0] >= 0:
            pass
        else:
            ratings.remove(rating)
            
    TopRatings = ratings[:10]
    
    TopMovies = []
    TopScores = []
    for score in TopRatings:
        TopMovies.append(" ".join(TitlesDf[TitlesDf.id == score[1]]["title"].to_string().split()[1:]))
        TopScores.append(score[0][0])
    print(TopMovies)
    
    
    plt.rcParams.update({'font.size':6})
    fig=plt.Figure(figsize=(30,6), dpi=85)
    fig.add_subplot(111).bar(TopMovies, TopScores, color="#57a1f8", width=0.5)
    chart=FigureCanvasTkAgg(fig,screen3)
    chart.get_tk_widget().pack()
    screen3.mainloop()
    
def graph4():
    screen4 = Toplevel(window)
    screen4.geometry('900x600+200+40')
    screen4.resizable(False, False)
    year=int(name.get())
    countries = TitlesDf[TitlesDf.release_year == year]["production_countries"].to_list()
    
    countryList = []
    
    for country in countries:
        countryList += country[1:-1].split(", ")
    
    CountryWiseProduction = {}
    
    for country in countryList:
        if country != '':
            if country in CountryWiseProduction:
                CountryWiseProduction[country] += 1
            else:
                CountryWiseProduction[country] = 1
                
    print(CountryWiseProduction)
    
    labels = CountryWiseProduction.keys()
    
    frequencies = []
    
    for country in labels:
        frequencies.append(CountryWiseProduction[country]) 
    
    print(CountryWiseProduction)
    
    plt.rcParams.update({'font.size':10})
    fig=plt.Figure(figsize=(30,6), dpi=85)
    def autopct(pct):
        return('%.2f'% pct)if pct>0 else ""
    fig.add_subplot(111).pie(frequencies,labels=labels,autopct=autopct)
    chart=FigureCanvasTkAgg(fig, screen4)
    chart.get_tk_widget().pack()
    screen4.mainloop()

def graph5():
    screen5 = Toplevel(window)
    screen5.geometry('900x600+200+40')
    screen5.resizable(False, False)
    year=int(name.get())
    genres = TitlesDf[TitlesDf.release_year == year]["genres"].to_list()
    
    genreList = []
    
    for genre in genres:
        genreList += genre[1:-1].split(", ")
    
    genreWiseFrequency = {}
    
    for genre in genreList:
        if genre != '':
            if genre in genreWiseFrequency:
                genreWiseFrequency[genre] += 1
            else:
                genreWiseFrequency[genre] = 1
                
    print(genreWiseFrequency)
    
    labels = genreWiseFrequency.keys()
    
    frequencies = []
    
    for genre in labels:
        frequencies.append(genreWiseFrequency[genre]) 
    
    print(genreWiseFrequency)
    
    
    plt.rcParams.update({'font.size': 8})
    fig=plt.Figure(figsize=(40, 15), dpi=100)
    def autopct(pct):
        return('%.2f'% pct)if pct>0 else ""
    fig.add_subplot(111).pie(frequencies, labels=labels,autopct=autopct)
    
    chart=FigureCanvasTkAgg(fig, screen5)
    chart.get_tk_widget().pack()
    screen5.mainloop()
   
def edtech():
    if(v.get()==""):
        messagebox.showwarning("CAUTION","NO USER NAME")
    elif (v.get()!="admin"):
        messagebox.showwarning("CAUTION","INCORRECT USER NAME")
    elif(v.get()=="admin" and y.get()!="1234"):
        messagebox.showwarning("ATTENTION","INVALID PASSWORD")
    elif(v.get()!="admin" or y.get()!="1234"):
        messagebox.showwarning("ATTENTION","THE USER DOESNOT EXISTS!")
    else:
        messagebox.showinfo("LOGIN SUCCESSFULL WELCOME USER :) ",v.get())
        screen1=Toplevel(window)
        screen1.geometry('900x600+200+40')
        screen1.resizable(False,False)
        mypic=Image.open("C:/Users/mahiz/OneDrive/Desktop/menu.webp")
        resized=mypic.resize((300,325),Image.ANTIALIAS)
        newpic=ImageTk.PhotoImage(resized)
        l3=Label(screen1,image=newpic)
        l3.place(x=0,y=0)
        l4=Label(screen1,text="CLICK THE BUTTON FOR GRAPH!!",bg="lightpink",fg="white",font=("corbel",24))
       #l4.place(x=400,y=50)
        l4.pack()
        e1=Entry(screen1,font=("Corbel",14),textvariable=name)
        e1.pack()
        b1=Button(screen1,text="ACTOR",bg="orange",fg="white",font=("Corbel",14),command=graph1)
        b1.place(x=400,y=80)
        b2=Button(screen1,text="COUNTRY RELEASES",bg="orange",fg="white",font=("Corbel",14),command=graph2)
        b2.place(x=550,y=80)
        b3=Button(screen1,text="TOP TEN",bg="orange",fg="white",font=("Corbel",14),command=graph3)
        b3.place(x=400,y=150)
        b4=Button(screen1,text="COUNTRIES",bg="orange",fg="white",font=("Corbel",14),command=graph4)
        b4.place(x=550,y=150)
        b5=Button(screen1,text="GENRES",bg="orange",fg="white",font=("Corbel",14),command=graph5)
        b5.place(x=400,y=220)
        screen1.mainloop()
            
            
def clear():
    #print("button clicked")
    if(v.get()=="" and y.get()==""):
        messagebox.showerror("ERROR","NOTHING TO DELETE")
    else:
         v.set("")
         y.set("")
         messagebox.showinfo("INFORMATION","DATA CLEARED SUCCESSFULLY")
         
l1=Label(window,text="USER ID:",bg="lightblue",fg="white",font=("Corbel",14))
l1.place(x=20,y=30)
e1=Entry(window,font=("Corbel",14),textvariable=v)
e1.place(x=150,y=30)
l2=Label(window,text="PASSWORD:",bg="lightblue",fg="white",font=("Corbel",14))
l2.place(x=20,y=60)
e2=Entry(window,font=("Corbel",14),textvariable=y)
e2.place(x=150,y=60)
b1=Button(window,text="ENTER",bg="green",fg="yellow",command=edtech)
b1.place(x=200,y=120)
b2=Button(window,text="CANCEL",bg="red",fg="yellow",command=clear)
b2.place(x=250,y=120)
mypic=Image.open("C:/Users/mahiz/OneDrive/Desktop/media.jpg")
resized=mypic.resize((300,225),Image.ANTIALIAS)
newpic=ImageTk.PhotoImage(resized)
l3=Label(window,image=newpic)
l3.place(x=200,y=150)
window.mainloop()