class Room:
    def __init__(self, name):
        self.name = name
        self.songs = []
        self.patron = []
        

    def new_guest(self, guest):
        return self.patron.append(guest)
       

    def remove_guest(self, guest):
        return self.patron.remove(guest)

    def has_guest(self):
        return len(self.patron)

    def add_song(self, song):
        return self.songs.append(song)

    def has_song(self):
        return len(self.songs)

    def check_capacity(self):
        if len(self.patron) > 2:
            return self.patron.pop()