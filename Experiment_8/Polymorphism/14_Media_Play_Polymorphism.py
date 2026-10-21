class Media:
    def play(self):
        pass


class Audio(Media):
    def play(self):
        print("Playing audio.")


class Video(Media):
    def play(self):
        print("Playing video.")


class Podcast(Media):
    def play(self):
        print("Playing podcast.")


for media in [Audio(), Video(), Podcast()]:
    media.play()
