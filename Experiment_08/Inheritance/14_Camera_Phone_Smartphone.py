class Camera:
    def take_photo(self):
        print("Photo taken.")


class Phone:
    def make_call(self, number):
        print("Calling", number)


class Smartphone(Camera, Phone):
    def use_smartphone(self):
        self.take_photo()
        self.make_call("9876543210")


phone = Smartphone()
phone.take_photo()
phone.make_call("9876543210")
phone.use_smartphone()
