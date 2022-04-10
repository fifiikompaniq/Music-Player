import json
import audio_metadata
import os

LOW_BITRATE = 96


class Song: 
    def __init__(self, title, artist, album, length, bitrate): 
        self.title = title 
        self.artist = artist
        self.album  = album 
        self.rating = -1
        self.length = length
        self.bitrate = bitrate
        self.playlist = ""
        
    def rate(self,new_rating): 
        self.rating = new_rating

class Playlist(): 
    def __init__(self, title, songs=None): 
        self.songs = songs if songs is not None else []
        self.title = title
    
    def add_song(self, song): 
        self.songs.append(song)
        song.playlist = self.title
    
    def remove_song(self, song_name):
        for song in self.songs:
            if song.title == song_name:
                song.playlist = ""
                self.songs.remove(song)
                 
    def total_length(self):
        total_length = 0
        for song in self.songs: 
            total_length+=song.length
        return total_length
    
    def remove_disrated(self):
        for song in self.songs:
            if song.rating == -1: 
                song.playlist = ""  
                self.songs.remove(song)
    
    def remove_bad_quality(self): 
        for song in self.songs:
            if song.bitrate < 100:   
                self.songs.remove(song)
    
    def show_artists(self):
        artists = []
        for song in self.songs: 
            if song.artist in artists:
                pass
            else:
                artists.append(song.artist)
        print(artists)
    
    def __str__(self):
        song_docs = []
        if len(self.songs) != 0:
            for song in self.songs:
                song_docs.append("{} - {}: {} seconds\n".format(song.artist, song.title, song.length))
        else: 
            print("There are no songs in this playlist!")
        return '\n'.join(song_docs) 

    def save(self): 
        filePathNameWExt = self.title + '.json'
        data = {}
        with open(filePathNameWExt, 'w') as fp:
            for song in self.songs: 
                data['title'] = str(song.title)
                data['artist'] = str(song.artist)
                data['album'] = str(song.album)
                data['rating'] = str(song.rating)
                data['length'] = str(song.length)
                data['bitrate'] = str(song.bitrate)
                json.dump(data, fp)
                fp.write('\n')
                data = {}
            
            


    def load(self, playlist_title): 
        playlist = open(f"{playlist_title}.json", "r")
        data = []
        i = 0
        for line in playlist:     
                data.append(json.loads(line))
                song = Song(title = data[i]["title"], artist = data[i]["artist"], album = data[i]["album"], length = data[i]["length"], bitrate = data[i]["bitrate"])
                self.songs.append(song)
                i+=1

class MusicCrawler(): 
    def generate_playlist(self, directory, title): 
        playlist = []
        for filename in os.listdir(directory):
            file = os.path.join(directory, filename)
            metadata = audio_metadata.load(file)
            playlist.append(Song(title=metadata.tags.title, artist=metadata.tags.artist, album=metadata.tags.album, length=metadata.streaminfo["duration"], bitrate=metadata.streaminfo["bitrate"]))
        return Playlist(title=title, songs=playlist)
            
         
        


         