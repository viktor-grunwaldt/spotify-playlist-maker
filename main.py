from getpass import getpass
import requests
import json
# Things to do:
# 1. read in links
# 2. split albums from songs
# 3. fetch songs
# 4. make playlist
# 5. add songs to pl

class spt():
    def __init__(self):
        self.client_id = getpass("client_id: ")
        self.client_pass = getpass("client_pass: ")
        self.headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.client_pass}"
        }


def create_playlist(spt:spt, name, description):
    request_body = json.dumps({
        "name": name,
        "description": description,
        "public": True
    })

    query = f"https://api.spotify.com/v1/users/{spt.client_id}/playlists"
    response = requests.post(
        query,
        data=request_body,
        headers=spt.headers
    )
    response_json = response.json()

    # playlist id
    return response_json["id"]

# parses the read data into two lists of id's - songs and albums
def parse_text(data):
    songs, albums = [], []
    # example link:
    # https://open.spotify.com/album/5l5m1hnH4punS1GQXgEi3T?si=gZH_1PCoSBirFUg728jrzA
    # the si part is a fingerprint of user + time
    for link in data:
        id_type, tail = link.replace("https://open.spotify.com/", "").split("/")
        link_id = tail.split("?")[0]
        if id_type == "album":
            albums.append(link_id)
        elif id_type == "track":
            songs.append(link_id)
        else:
            raise Exception("My parser is bad!")
        
    return (songs, albums)

# using get album tracks instead of get several albums, 
# since I have more than 20 anyways
def get_album_tracks(album_id):
    pass


def main():
    pass

if __name__ == "__main__":
    main()