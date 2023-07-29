

class Song:
    count = 0
    genres = []  
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre        
        Song.add_song_to_count()
        Song.add_to_genres(self)        
        Song.add_to_artists(self)
        Song.add_to_genre_count(self)
        Song.add_to_artist_count(self)
        
    def add_song_to_count():
        Song.count += 1        
        
    def add_to_genres(self):        
        Song.genres.append(self.genre)
        
    def add_to_genre_count(self):
        Song.genre_count.update({f"{self.genre}": 0})
        for genre in Song.genres:            
            if genre == self.genre:                        
                Song.genre_count[self.genre] += 1
                print(f"Adding Genres {genre} : {Song.genre_count[self.genre]}")               
                                            
    def add_to_artists(self):
        Song.artists.append(self.artist)
        
    def add_to_artist_count(self):
        Song.artist_count.update({f"{self.artist}": 0})
        for artist in Song.artists:            
            if artist == self.artist:                        
                Song.artist_count[self.artist] += 1
                print(f"Adding Genres {artist} : {Song.artist_count[self.artist]}") 
           
    #def artist_count(self):
        
                          
            
       
