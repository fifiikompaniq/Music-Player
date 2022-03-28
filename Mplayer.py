import json

LOW_BITRATE = 96


class Song: 
    def __init__(self, title, artist, album, length, bitrate): 
        self.title = title 
        self.artist = artist
        self.album  = album 
        self.rating = -1
        self.length = length
        self.bitrate = bitrate
        
    def rate(self,new_rating): 
        self.rating = new_rating

class Playlist(): 
    def __init__(self, title): 
        self.songs = []
        self.title = title
    
    def add_song(self, song): 
        self.songs.append(song)
    
    def remove_song(self, song_name):
        for i in len(self.songs):
            if self.songs[i].title == song_name:   
                self.songs.remove(self.songs[i])
    
    def total_length(self):
        total_length = 0
        for i in len(self.songs): 
            total_length+=self.songs[i].length
        return total_length
    
    def remove_disrated(self):
        for i in len(self.songs):
            if self.songs[i].rating == -1:   
                self.songs.remove(self.songs[i])
    
    def remove_bad_quality(self): 
        for i in len(self.songs):
            if self.songs[i].bitrate < 100:   
                self.songs.remove(self.songs[i])
    
    def show_artists(self):
        artists = []
        for i in len(self.songs): 
            if self.songs[i].artist in artists:
                pass
            else:
                artists.append(self.songs[i].artist)
    
    def __str__(self):
        song_docs = []
        for i in self.songs:
            song_docs.append("{} - {}: {}".format(self.songs[i].artist, self.songs[i].title, self.songs[i].length))
        return '\n'.join(song_docs) 

    def save(self, playlist_title): 
        playlist = open(f"{playlist_title}.json", "w")
        s = f'{playlist_title} [ \n'
        for i in len(self.songs): 
            pass
            


    def load(self, playlist_title): 
        playlist = open(f"{playlist_title}.json", "r") 
         