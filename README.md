This is a  python script which can be used for static analysis of hashes in bulk.
It utilises VirusTotal API V3 for checking the hashes. It creates a table out of API's json output and writes the desired output down to a file of your choice. 
Hashes can be fed via txt file. 
Due to 4 lookups/min limitation, there is a 20 seconds sleep command in between checking hashes , we can check upto 499 hashes/day.

NOTE:- Conversion of output file as excel will only by supported till Python version 3.11 
(If any other verions of Python are installed , change the interpreter to Python 3.11 or lower )

Requisites:- Code Editor  , Python 3.11(or lower) , pip

Steps:-
1) Clone the repository by the command 
    git clone https://github.com/VarunAgarwal11/VirusTotal_TrendMicro.git 
2) Open terminal and Run the "requirements.txt" file by entering the command 
    pip install -r requirements.txt
3) SignIn/SignUp to Virus Total websiite https://www.virustotal.com/gui/sign-in and then retrieve the free API key.
4) Replace the 'YOUR-API-KEY' in script.py from the key retrieved in Step 3.
5) Create a file in the same folder and place the hashes to be validated in the file.
6) Copy the path of the file and replace it in "your_hash_file_location.txt" in script.py
7) Enter the output file name to be saved in "OUTPUT_FILENAME.xlsx"
8) Run the script.py


