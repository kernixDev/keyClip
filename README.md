# keyClip's usage
keyClip is a short script used to add custom shortcuts into your Windows 10/11 environment  
it currently supports 3 shortcuts; CTRL+F1 which transforms your selected text into uppercase, CTRL+F2 which transforms your selected text into (you guessed it) lowercase and CTRL+F3 which transforms your selected text into camelCase.

# setting up keyClip
In order to setup keyClip, please execute this line in your command prompt  
```git clone https://github.com/kernixDev/keyClip```  
Then, execute this line in order to install the python **requirements** needed for this script  
```pip install -r requirements.txt```  
If you want keyClip to run at every startup, follow the next guide  

# adding keyClip to startup
Firstly, you will need to create a shortcut leading to the keyClip.pyw file  
To do so, you can go into the folder where keyClip is located and right click the background  
Click "New" then "Shortcut"  
In the path, make sure to put the file location of keyClip.pyw  
Then, right click the shortcut and click "cut"  
Once you've done that, press Windows + R and enter  
```shell:startup```  
Now right click the background of the folder that opens up and select "Paste".  
You're done, keyClip.pyw should now run every time you start up your computer  
Enjoy the script, and I hope you find it as useful as I do