class Room:
    def __init__(self, name, price, till):
        self.name = name
        self.price = price
        self.songs = []
        self.patron = []
        self.till = till
        

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
        room_capacity = 2
        if room_capacity >= len(self.patron):
            return True
        return False

    def customer_fee(self, price):
        self.till += price