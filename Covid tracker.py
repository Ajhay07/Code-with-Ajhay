import tkinter as tk
import requests
import datetime

def getCovidData():
    api = "https://disease.sh/v3/covid-19/all"
    json_data = requests.get(api).json()
    total_cases=str(json_data['cases'])
    total_deaths=str(json_data['deaths'])
    today_cases=str(json_data['todayCases'])
    today_deaths=str(json_data['todayDeaths'])
    today_recovered=str(json_data['todayRecovered'])
    updated_at = json_data['updated']
    label.config(text = "Total Cases: "+total_cases+"\n"+"Total Deaths: "+total_deaths
                 +"\n"+"Today Cases: "+today_cases+"\n"+"Today Deaths: "+today_deaths
                 +"\n"+"Today Recovered: "+today_recovered)
    date=datetime.datetime.fromtimestamp(updated_at/1e3)
    label2.config(text=date)

canvas = tk.Tk()
canvas.geometry("400x400")
canvas.title("Covid Tracker")

f = ("copperplate", 15, "bold")

btn = tk.Button(canvas, font = f, text = "Load",command = getCovidData)
btn.pack(pady = 20)

label = tk.Button(canvas, font = f)
label.pack(pady = 20)

label2 = tk.Label(canvas, font = f)
label2.pack()
getCovidData()

canvas.mainloop()
