#Creating a Twitter Bot using Python
##September 10, 2015

# Instructions


## Step 1 - Download the Code
	
If you're seeing these instructions you're already in the right place!
Go ahead and click on the "Download ZIP" button in the lower left corner

![step1](http://i.imgur.com/qVQrpd3.png)

Unzip the folder, and click on either ``windows_start.bat`` or ``mac_osx_start.sh`` 
depending on your platform. 

![step2](http://i.imgur.com/cei5bqp.png)

Next, check that your prompt has the ``(env)`` tag. If so you're good to go!


## Step 2 - Authorize yourself

Now that you're into the environment. We've already gone ahead and installed both Python and Python-Twitter
for you! MAGIC! Now you've got to do some work.

Make sure that you're logged into Twitter on your computer (or make an account). Then, type the following into your prompt window:

```
(env) bot> python get_access_token.py
```

Follow the instructions and type the pin code into the script after you click "Authorize App"

![step3](http://i.imgur.com/OxkQRmD.png)

![Imgur](http://i.imgur.com/WLiCrQk.png)

![Imgur](http://i.imgur.com/Jg26MvY.png)
	
## Step 3 - Check Authentication!

If you've gotten this far it's time to see if you can successfully log in with python-twitter and 
start writing your bot!

```
(env) bot> python check_authorization.py
```

You should see the following if everything went well:
![Imgur](http://i.imgur.com/hEEW4My.png)