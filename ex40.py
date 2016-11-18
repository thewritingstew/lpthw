class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def sing_song_backward(self):
        # this doesn't copy, just points lyrics2 to the address of lyrics
        #           lyrics2 = self.lyrics
        # so we want to do something else instead if we want to protect lyrics
        #           lyrics2 = self.lyrics[:]
        # which assigns lyrics2 by slicing lyrics
        lyrics2 = self.lyrics[:]
        while lyrics2:
            print(lyrics2.pop(-1))

        print("lyrics2 is: %r" % lyrics2)
        print("lyrics is: ")
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

happy_bday.sing_song_backward()
