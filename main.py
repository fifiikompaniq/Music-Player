from Mplayer import Song, Playlist
import json

def main(): 
    song_1 = Song(title="My Funny Valentine", artist="Frank Sinatra", album="None", length=145, bitrate=90) # Length is in secnds
    song_2 = Song(title="My Not Funny Valentine", artist="Frank Sinatra", album="None", length=145, bitrate=125)
    playlist = Playlist("My_Playlist")
    playlist.add_song(song_1)
    playlist.add_song(song_2)
    print(playlist)
    playlist.save()
    playlist.load("My_Playlist")
    print(playlist)
    
    


main()