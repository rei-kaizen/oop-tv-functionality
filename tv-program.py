#TV requirements:
# ON and Off
# channel switcher
# volume control

#define a class named TV
class TV:
    #create function to initialize channel, volumeLevel, and on as TV default object
    def __init__(self) -> None:
        """Initialize a default TV object"""
        self.channel = 1
        self.volumeLevel = 1
        self.on = True
        
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
        """Sets the new channel for this TV"""
        self.channel = channel
        
    #function to get the volume
    def getVolume(self):
        """Gets the volume level of the TV and returns an int representing the current volume for this TV"""
        return self.volumeLevel
        
    #function to set the volume
    def setVolumE(self, volumeLevel) -> None:
        """Sets the new volume level for this TV"""
        self.volumeLevel = volumeLevel
        
    #function to increase the channel
    #function to decrease the channel
    #function to increase the volume
    #function to decrease the volume
    
#define a class named TestTV for test driver program
    #create two objects from class TV
 
TV()   