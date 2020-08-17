# DiscordNukebot
An easy to use, fully customizable discord nukebot, complete with webhook spamming. Note that I'll hardly update this, if ever.

# Setup and Usage
To set up the bot, you'll need the bot token and a prefix. If you don't know how to get a discord bot token from the [developer portal](https://discord.com/developers) I suggest watching [this video.](https://www.youtube.com/watch?v=b61kcgfOm_4)

Once you obtain your bot token, paste it in the script as shown below. Make sure the token is IN THE QUOTATION MARKS (the token should be a string object)
```py
token = "NzQzOTU1Mzk3NjcyNDM1NzYy.XzcMdA.cSXie4geIGekaQkk6dXPnTjoJqc"
```

After getting your bot token, set your prefix by typing your prefix as shown below. Again, make sure it's in the quotes or it won't work.
```py
prefix = "$"
```

There are a few more config options to configure how your nuke actually behaves. These are all filled in already, so editing these are optional.
```py
spam_messages = ["@everyone nuked", "@everyone get nuked"]
channel_names = ["nuked", "get nuked"]
webhook_usernames = ["nuked", "get nuked"]
nuke_on_join = False
nuke_wait_time = 0
```
**spam_messages** : The messages your bot will spam after nuking the server. Make sure that each entry in the list is a string and separated by a comma.
 
**channel_names** : The names of the channels your bot will create when nuking. Like spam_messages, each entry should be a string and separated by a comma.
 
**webhook_usernames** : Usernames of the webhooks your bot will use to spam channels when nuking. Just like spam_messages and channel_names, this should be a list of strings separated by commas.
 
**nuke_on_join** : This will determine if your bot nukes the server as soon as it's added. This should either be True or False. By default it is set to False.
 
**nuke_wait_time** : The amout of time (in seconds) that the bot will wait before nuking the server when autonuke is enabled.

# Commands
> cmds : DMs you all of the bot's commands.
>
> kill : Nukes the server.
>
> sall : Spams all channels.
>
> ccr [amount] [name] : Creates channels.
> 
> cdel : Deletes all channels.
>
> logout : Exits the script.

# Additional Notes
This probably won't be updated frequently, if ever.

Don't be a skid, give credit if you're gonna distribute and use this.

*Happy nuking!*
