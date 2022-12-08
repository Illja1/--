#Task-1
class Person:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname =  surname
        self.age = age

    def talk(self):
        print(f"Hello,my name is {self.name} {self.surname} and i'm {self.age} years old ")

Person.talk('Carl','Jonshon',20)
Person.talk('Illja','Homenko',18)
Person.talk('DIma','Jonshon',22)

#Task-2
class Dog:
    def __init__(self,age):
        self.age = age

    def human_age(age,age_factor= 7):

        print(age * age_factor)


Dog.human_age(12)

#Task-3
class VoiceCommand:
    def __init__(self, channels):
        self._channels = channels
        self._current_channel = 0

    def first_channel(self):
        return self.turn_channel(1)

    def last_channel(self):
        return self.turn_channel(len(self._channels))

    def turn_channel(self, channel_number):
        self._current_channel = channel_number - 1
        return self.current_channel()

    def _previous_next(self, delta):
        self._current_channel = (self._current_channel + delta) % len(self._channels)
        return self.current_channel()

    def next_channel(self):
        return self._previous_next(1)

    def previous_channel(self):
        return self._previous_next(-1)

    def current_channel(self):
        return self._channels[self._current_channel]

    def is_exist(self, channel):
        if isinstance(channel, int):
            c = 0 <= channel < len(self._channels)
        else:
            c = channel in self._channels
        return ('No', 'Yes')[c]




CHANNELS = ["BBC", "Discovery", "TV1000"]

controller = VoiceCommand(CHANNELS)
    
controller.first_channel()
controller.last_channel() 
controller.turn_channel(1) 
controller.next_channel()
controller.previous_channel() 
controller.current_channel() 
controller.is_exist(4) 
controller.is_exist("TV1000") 
