# spotify-playlist-maker

I have a list of links of songs or albums and won't add it by hand

## how-to

**steps:**\

1. grab your oauth from [here](https://developer.spotify.com/console/post-playlists/)
and user_id [here](https://developer.spotify.com/console/get-current-user/) (should be your login name or smth)
2. clone the repo
3. prepare a file of links to songs/albums (mine's named music.txt)
4. download `requests` if you haven't already (`pip install --user requests`)
5. replace file name in `main()`
6. run `python ./main.py` and fill in the secrets when prompted
7. ?
8. profit

## to-dos

* add adding playlist support(?)
* better error handling
* try different auth options
