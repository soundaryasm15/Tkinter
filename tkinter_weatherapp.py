from tkinter import *
from PIL import ImageTk,Image
import requests
import json


root=Tk()
root.title("Weather Application")
root.iconbitmap("C:/Users/user/Desktop/college/5th sem/tkinter/home.ico")
root.geometry("600x100")
#creating zip look up function
def zipLookup():
	# zip.get()
	# zipLabel=Label(root,text=zip.get())
	# zipLabel.grid(row=1,column=0,columnspan=2)
	#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=45E095BE-7187-4970-8361-969FBF849A40


	try:
		api_request=requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+ zip.get()+"&distance=5&API_KEY=45E095BE-7187-4970-8361-969FBF849A40")
		api=json.loads(api_request.content)
		city=api[0]["ReportingArea"]
		quality=api[0]["AQI"]
		category=api[0]["Category"]["Name"]
		if category=="Good":
			weather_color="#00e400"
		elif category=="Moderate":
			weather_color="#ffff00"
		elif category=="Unhealthy for Sensitive Groups":
			weather_color="#ff7e00"
		elif category=="Unhealthy":
			weather_color="#ff0000"
		elif category=="Very Unhealthy":
			weather_color="#99004c"
		elif category=="Hazardous":
			weather_color="#7e0023"

		root.configure(background=weather_color)

		MyLabel=Label(root,text=city+" Air Quality "+str(quality)+" "+category,font=("Helvetica",15),background=weather_color)
		MyLabel.grid(row=1,column=0,columnspan=2)

	except Exception as e:
		api="Error......"



zip=Entry(root)
zip.grid(row=0,column=0,sticky=W+E+N+S)

zip_btn=Button(root,text="Lookup Zipcode",command=zipLookup)
zip_btn.grid(row=0,column=1,sticky=W+E+N+S)

root.mainloop()