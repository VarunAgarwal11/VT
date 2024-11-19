This is a  python script which can be used for static analysis of hashes in bulk.
It utilises VirusTotal API V3 for checking the hashes. It creates a table out of API's json output and writes the desired output down to a file of your choice. 
Hashes can be fed via txt file. 
Due to 4 lookups/min limitation, there is a 20 seconds sleep command in between checking hashes , we can check upto 499 hashes/day.