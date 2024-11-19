import requests
import json
import time
from openpyxl import Workbook

wb = Workbook() # Create a new workbook and activate it
ws = wb.active

# Write data to the first row
ws.append(["Hash Value", "TM Category", "TM Result"])


apikey = 'YOUR-API-KEY' #enter the API key after logging in
hashes = open(r"your_hash_file_location.txt")  #txt file location 

hashes=list(hashes)
cleaned_hash_list = [hash.strip() for hash in hashes]

def check_url_status(url, headers):
    try:
        response = requests.get(url, headers=headers)
        print(f"Status Code: {response.status_code}")
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


for hashn in cleaned_hash_list:
    
    url = "https://www.virustotal.com/api/v3/files/"+hashn
    headers = {
    "accept": "application/json",
    "x-apikey":apikey 
    }
    VTlink= "https://www.virustotal.com/gui/file/"
    
    status_code = check_url_status(url, headers)
    if status_code == 200:
        print("The URL is accessible!")
    else:
        print(f"Failed to access the URL. Status code: {status_code}")
    
    print('Checking hash ' + url)
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        result = response.json()
        ws.append([hashn , "Not Found in Virus Total Database"])         
    elif response.status_code == 200:
        result = response.json()
        ws.append([ hashn ,f"{str(result['data']['attributes']['last_analysis_results']['TrendMicro']['category'])}" , f"{str(result['data']['attributes']['last_analysis_results']['TrendMicro']['result'])}" ])
    
    time.sleep(1 * 20)
    
wb.save("OUTPUT_FILENAME.xlsx")