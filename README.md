# Astronomy Picture of the Day wallpaper
Nasa hosts a [website](https://apod.nasa.gov/apod/astropix.html) where they choose an astronomy picture for the day. I love pictures of space and the pictures included on the APOD website are stunning. I've also had struggles trying to find decent wallpapers in the past, and I tend to get bored of the same wallpaper pretty fast. To solve my wallpaper struggles, I wrote a quick Python script that grabs the APOD and sets it as my wallpaper. I also set up Task Scheduler to run the script everyday at 12:30 AM (the APOD doesn't update immediately at 12 AM).

# How it works.
The script really is simple. It just grabs the html of the APOD website, locates the link for the image, downloads said image into a file, sets the image as the wallpaper, and then deletes the image it downloaded. **Note: This script currently only works on Windows, but if you have some Python code for MacOS or Unix to set a wallpaper, please add it!**

# Setup
Start off by cloning the repo with:  
```git clone https://github.com/jason-shepherd/apodwallpaper.git```  

Navigate into the folder:  
```cd apodwallpaper```

Install the requirements:  
```pip install -r requirements.txt```

Now you can run the script manually:  
```python apodwallpaper.py```  

Or set it up in Task Scheduler by:
```
Press Windows key and search Task Scheduler
On the right, click "Create Basic Task"
Give it a name and description and press "Next"
Select "Daily" then press "Next"
Select the time you you want to run the script and the day you want to start (12:30 AM, today for me), recurring every 1 days and press "Next"
Select "Start Program" then press "Next"
Click "Browse" and select the included batch script (.bat), set "Start in" to the script's directory. Click "Next"
Click "Finish"
```
