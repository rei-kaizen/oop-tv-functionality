#TV requirements:
# ON and Off
# channel switcher
# volume control

#define a class named TV
class TV:
    #create function to initialize channel, volumeLevel, and on as TV default object settings
    def __init__(self) -> None:
        """Initialize a default TV object"""
        self.channel = 1
        self.volumeLevel = 1
        self.on = False
        
    #function to turn the TV on
    def turnOn(self) -> None:
        """Turns on the TV"""
        self.on = True
            
    #function to turn the TV off
    def turnOff(self) -> None:
        """Turns off te TV"""
        self.on = False
        
    #function to get the channel
    def getChannel(self):
        """Gets the channel of the TV and returns an int representing the current channel for this TV"""
        return self.channel
        
    #function to set the channel
    def setChannel(self, channel) -> None:
        """Sets the new channel for this TV
        
        Parameters:
            channel(int): channel to be set up"""
        if self.on and 1 <= channel  <= 120:
            self.channel = channel
        
    #function to get the volume
    def getVolume(self):
        """Gets the volume level of the TV and returns an int representing the current volume for this TV"""
        return self.volumeLevel
        
    #function to set the volume
    def setVolume(self, volumeLevel) -> None:
        """Sets the new volume level for this TV
        
        Parameters:
            volumeLevel(int): volumeLevel to be set up"""
        if self.on and 1 <= volumeLevel <= 7:
            self.volumeLevel = volumeLevel
        
    #function to increase the channel
    def channeUp(self) -> None:
        """Increases the channel number by 1"""
        if self.on  and self.channel < 120:
            self.channel += 1    

    #function to decrease the channel
    def channeDown(self) -> None:
        """Decreases the channel number by 1"""
        if self.on  and self.channel > 1:
            self.channel -= 1
            
    #function to increase the volume
    def volumeUp(self) -> None:
        """Increases the volume level by 1"""
        if self.on and self.volumeLevel  < 7:
            self.volumeLevel +=1
        
    #function to decrease the volume
    def volumeDown(self) -> None:
        """Decreases the volume level  by 1"""
        if self.on and self.volumeLevel > 1:
            self.volumeLevel -=1
               
