# phpBB_PMscraper
A web scraper for extracting PM's from a phpBB forum, in this case deskthority.net

This is a web scraper made in order to extract all the PM's from deskthority.net into a .json file with a nested dictionary structure. 

Depending on interest, images might be added into this program later.  

-Installation-

Prerequisites:

python installed

firefox installed

geckodriver for selenium: https://github.com/mozilla/geckodriver/releases


Linux:

`git clone https://github.com/Redmauss/phpBB_PMscraper.git` into a directory of your choice or download the ZIP file and extract.  


In the cloned directory type `./PMScrape` The program should open a firefox window. 

The program will then ask for your DT username and password.  Use `Shift + Ctrl + V` to paste them in your terminal.

PMscraper will then log in and log all of your PM links.  It will then proceed to go through each link and save the messages. Depending on the amount of PM's you 

have, this could take from minutes to several hours. 

Once the the program is finished, the firefox window will close and all your messages with be saved to a file `Messages .json`

Windows:

You can follow the same process above if you install wsl for windows 10: https://docs.microsoft.com/en-us/windows/wsl/install-win10

Be sure to change the powershell windows settings to allow `Shift + Ctrl + V` in the popup window. 



