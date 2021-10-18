from fastapi import FastAPI
import json
from scraper import Scraper
from pydantic import BaseModel
from data_store import post_data
import datetime
import sys


app = FastAPI()
data = Scraper()

def defaultconverter(o):
  if isinstance(o, datetime.datetime):
      return o.__str__()

"""
#Base model
class Options (BaseModel):
    FileName: str = "data_store"
    FileDesc: str = "Upload demonstration"

"""

"""
@app.get("/")
async def root():
    return {"message": "Hello World"}
"""    
    
    
@app.get("/")

async def read_item():
	
	url = "DeepLearningAI" # Pass the URL of the page
	
	list_data= data.scrape_data(url)  
	
	# store the scraped data in JSON file
	with open("facebook_data.json", 'a') as f:
		for item in list_data :
			item["time"] = defaultconverter(item["time"])
			json.dump(item, f, ensure_ascii = False, indent=1 , separators= (',', ':'))
	### insert data in MongoDB 
	ok = post_data().pydata("facebook_data.json")
	
	return list_data





"""
@app.post("/uploadfiles/")
def save_item():
	list_data= data.scrapedata("RadioIfm")
	with open("facebook_data.json", 'a') as f:
		for item in list_data :
			json.dump(item, f)
	return {"data_in_file": facebook_data.json}
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0')
