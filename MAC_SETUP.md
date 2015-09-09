#Creating a Twitter Bot using Python
##September 10, 2015

# Instructions


## Step 1 - SSH


Open up terminal, type 
```
  ssh digitalwomen@thomasmoll.co
```

Ask Gabby for the password! 
	

## Step 2 - Authorize yourself

Now that you're into the environment. We've already gone ahead and installed both Python and Python-Twitter
for you! MAGIC! Now you've got to do some work.

Make sure that you're logged into Twitter on your computer (or make an account). Then, type the following into your prompt window:
Replace "your_name" with your name

```
(env) bot> python get_access_token.py your_name
```

Copy the url that gets printed into your Web Browser. Click ``Authorize`` and then type the pin into your terminal where it says
"Pincode?:"

![step3](http://i.imgur.com/OxkQRmD.png)

![Imgur](http://i.imgur.com/WLiCrQk.png)

![Imgur](http://i.imgur.com/Jg26MvY.png)
	
## Step 3 - Check Authentication!

If you've gotten this far it's time to see if you can successfully log in with python-twitter and 
start writing your bot! Again IMPORTANT, please replace your_name with the name you used earlier!

```
(env) bot> python check_authorization.py your_name
```

You should see the following if everything went well:
![Imgur](http://i.imgur.com/hEEW4My.png)
