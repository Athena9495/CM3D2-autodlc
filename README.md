# CM3D2-autodlc
Script to ease CM3D2 DLC installation.

Installing the DLC packs are tedious, aren't they? While there is a way to make an all in one installer, it too, seemed tiring. So, I put together a script to do it for me. I am not an experienced programmer, I just brought together bits and pieces from here and there. It worked for me, and if you follow the guidelines below, I don't see why it shouldn't for you. However, I recommend you start with just one or two, to make sure it works.

__NOTES-__ 
<ul>
<li>Use only for DLC packs which do not need to come in order. 
<li>That means, install the updates manually, and the Plus Acts in order, by yourself. They aren't that many.
<li>Script is written w.r.t Python2.7.
<li>You need ONE other library, pyautogui.
<li>Install using- `pip install pyautogui`
<li>Ensure that your System Locale is set to Japan. This is important, so that we don't end up with any errors.
</ul>

**Now, the actual installation.**
<ul>
<li>Read the script comments to find as to where your mouse should be, and also, how to find it.
<li>Put the script in a folder somewhere convenient. Say ../Desktop/cmupdates/
<li>Unpack the archives into a folders of their own, and put it in the cmupdates folder
<li>Open a cmd window with admin privileges, and navigate to the cmupdates folder
<li>Run- `python script.py`
<li>Sit back, watch it happen. Don't touch anything until it's done.
</ul>

**Additional notes-**
<ul>
<li>The whole concept is based on the fact that the dialog box ALWAYS appears at a certain position on the screen. If this is not the case for you, don't use the script.
<li>REMOVE the DLC folders from the cmupdates folder, or you'll end up in a stupid situation, where the process is stalled, because there would be no second click.
<li>In case something DOES go wrong, the time.sleep() instances should give you enough time to go to the cmd window and press Ctrl+C. Alternatively, Ctrl+Alt+Del.
<li>Credits to the various people on stackexchange.com who already had issues/requests relevant to the functions used in the script.
<li>If I may, the best part, I felt, was that, even though the file structure of some DLCs were different (nested folders), the script remains unchanged.
</ul>

_Any suggestions to optimise code are welcome._

**Obligatory Disclaimer** - I'm not responsible for any or all losses you may face. Backup before doing anything.
