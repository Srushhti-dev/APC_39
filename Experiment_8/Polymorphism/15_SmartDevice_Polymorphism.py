class SmartDevice:
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class Light(SmartDevice):
    def turn_on(self):
        print("Light turned ON.")

    def turn_off(self):
        print("Light turned OFF.")


class Fan(SmartDevice):
    def turn_on(self):
        print("Fan turned ON.")

    def turn_off(self):
        print("Fan turned OFF.")


class AC(SmartDevice):
    def turn_on(self):
        print("AC turned ON.")

    def turn_off(self):
        print("AC turned OFF.")


class TV(SmartDevice):
    def turn_on(self):
        print("TV turned ON.")

    def turn_off(self):
        print("TV turned OFF.")


devices = [Light(), Fan(), AC(), TV()]

for device in devices:
    device.turn_on()
    device.turn_off()
