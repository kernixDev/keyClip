# 💡 keyclip's usage
keyclip is a short script used to add custom shortcuts into your windows 10/11 environment  
it currently supports 3 shortcuts; ctrl+f1 which transforms your selected text into uppercase, ctrl+f2 which transforms your selected text into (you guessed it) lowercase and ctrl+f3 which transforms your selected text into camelcase.

# 🛠 Installation
in order to setup keyclip, please execute this line in your command prompt  
```bash 
git clone https://github.com/kernixdev/keyClip
cd keyClip
pip install -r requirements.txt
```  
  
if you want keyclip to run at every startup, follow the next guide  

# ⚙️ adding keyclip to startup
firstly, you will need to create a shortcut leading to the keyclip.pyw file  
to do so, you can go into the folder where keyclip is located and right click the background  
click "new" then "shortcut"  
in the path, make sure to put the file location of keyclip.pyw  
then, right click the shortcut and click "cut"  
once you've done that, press windows + r and enter  
```shell:startup```  
now right click the background of the folder that opens up and select "paste".  
you're done, keyclip.pyw should now run every time you start up your computer  
enjoy the script, and i hope you find it as useful as i do

Please note that the shortcuts may cause conflicts with other softwares' shortcuts  
If you wish to, you can easily change the shortcuts by editing the first attribute in add_hotkey()
Furthermore, if you wish to add your own custom shortcuts, you can do so easily using the logic that is already implemented into the script, and editing it to fit your criteria