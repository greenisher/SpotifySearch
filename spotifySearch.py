#! python3
#spotifySearch.py - launches a search in spotify for a term put in command line or in clipboard

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    song = ''.join(sys.argv[1:])
else:
    song = pyperclip.paste()

webbrowser.open('https://play.spotify.com/search/' + song)
