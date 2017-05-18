# CM3D2-autodlc
Script to ease CM3D2 DLC installation.

Installing the DLC packs are tedious, aren't they? While there is a way to make an all in one installer, it too, seemed tiring. So, I put together a script to do it for me. I am not an experienced programmer, I just brought together bits and pieces from here and there. It worked for me, and if you follow the guidelines below, I don't see why it shouldn't for you. However, I recommend you start with just one or two, to make sure it works.

NOTE- 
-Use only for DLC packs which do not need to come in order. 

-That means, install the updates manually, and the Plus Acts in order, by yourself. They aren't that many.

-Script is written wrt Python2.7.

-You need ONE other library, pyautogui.

-Install using- pip install pyautogui

-Ensure that your System Locale is set to Japan. This is important, so that we don't end up with any errors.

Now, the actual installation.

-Read the script comments to find as to where your mouse should be, and also, how to find it.

-Put the script in a folder somewhere convenient. Say ../Desktop/cmupdates/

-Unpack the archives into a folders of their own, and put it in the cmupdates folder

-Open a cmd window with admin privileges, and navigate to the cmupdates folder

-Run- python script.py

-Sit back, watch it happen. Don't touch anything until it's done.

Additional notes

-The whole concept is based on the fact that the dialog box ALWAYS appears at a certain position on the screen. If this is not the case for you, don't use the script.

-REMOVE the DLC folders from the cmupdates folder, or you'll end up in a stupid situation, where the process is stalled, because there would be no second click.

-In case something DOES go wrong, the time.sleep() instances should give you enough time to go to the cmd window and press Ctrl+C. Alternatively, Ctrl+Alt+Del.

Credits to the various people on stackexchange.com who already had issues/requests relevant to the functions used in the script.

If I may, the best part, I felt, was that, even though the file structure of some DLCs were different (nested folders), the script remains unchanged.

Any suggestions to optimise code are welcome.

Obligatory Disclaimer - I'm not responsible for any or all losses you may face. Backup before doing anything.
