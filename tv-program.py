import random
import pyfiglet

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
    def channelUp(self) -> None:
        """Increases the channel number by 1"""
        if self.on  and self.channel < 120:
            self.channel += 1    

    #function to decrease the channel
    def channelDown(self) -> None:
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
               
#define a function named TestTV for test driver program
def TestTV():
    """Test the methods for each TV object""" 
    #create two objects from class TV
    #for TV1 objects
    TV1 = TV()
    TV1.turnOn()
    TV1.setChannel(30)
    TV1.setVolume(3)
    
    #for TV2 objects
    TV2 = TV()
    TV2.turnOn()
    TV2.setChannel(3)
    TV2.setVolume(2)
    
    #display the output
    #add design similar to tv with ascii art string
    #add color to the output string
    
    #TV1
    print(" "*19 +"\   /" + " "*19)
    print(" "*20 +"\ /" + " "*20)
    print("+" + "="*45 + "+")
    print("|" + "\033[31m" +" .  '"*9 + "\033[0m" + "|")
    print("|" + "\033[33m" + " .  '"*9 + "\033[0m" + "|")
    print("|" + "\033[32m" + " .  '"*9 + "\033[0m" + "|")
    #📺 TV1's channel is 30 and volume level is 3
    print("\033[93m" + f"\U0001F4FA TV1's channel is {TV1.getChannel()} and volume level is {TV1.getVolume()}\U0001F4FA" + "\033[0m")
    print("|" + "\033[35m" +" .  '"*9 + "\033[0m" + "|")
    print("|" + "\033[36m" + " .  '"*9 + "\033[0m" + "|")
    print("|" + "\033[31m" + " .  '"*9 + "\033[0m" + "|")
    print("|" + "-"*45 + "|")
    print("|" + " "*19 + "\033[90mTV #1\033[0m" + " "*16 + "\U0001F535   |")
    print("+" + "="*45 + "+")
    print("O-O" + " "*41 + "O-O")
    
#                    \   /
#                     \ /                        
# +=============================================+
# | .  ' .  ' .  ' .  ' .  ' .  ' .  ' .  ' .  '|
# | .  ' .  ' .  ' .  ' .  ' .  ' .  ' .  ' .  '|
# | .  ' .  ' .  ' .  ' .  ' .  ' .  ' .  ' .  '|
# 📺 TV1's channel is 30 and volume level is 3📺 
# | .  ' .  ' .  ' .  ' .  ' .  ' .  ' .  ' .  '|
# | .  ' .  ' .  ' .  ' .  ' .  ' .  ' .  ' .  '|
# | .  ' .  ' .  ' .  ' .  ' .  ' .  ' .  ' .  '|
# |---------------------------------------------|
# |                   TV #1                🔵   |
# +=============================================+
# O-O                                         O-O
    print()
    
    #TV2
    print(" "*19 +"\   /" + " "*19)
    print(" "*20 +"\ /" + " "*20)
    print("+" + "="*45 + "+")
    print("|" + "\033[31m" +" .  '"*9 + "\033[0m" + "|")
    print("|" + "\033[33m" + " .  '"*9 + "\033[0m" + "|")
    print("|" + "\033[32m" + " .  '"*9 + "\033[0m" + "|")
    print("\033[91m" + f"\U0001F4FA TV2's channel is {TV2.getChannel()} and volume level is {TV2.getVolume()} \U0001F4FA" + "\033[0m")
    #📺 TV2's channel is 3 and volume level is 2
    print("|" + "\033[35m" +" .  '"*9 + "\033[0m" + "|")
    print("|" + "\033[36m" + " .  '"*9 + "\033[0m" + "|")
    print("|" + "\033[31m" + " .  '"*9 + "\033[0m" + "|")
    print("|" + "-"*45 + "|")
    print("|" + " "*19 + "\033[90mTV #2\033[0m" + " "*16 + "\U0001F535   |")
    print("+" + "="*45 + "+")
    print("O-O" + " "*41 + "O-O")
    
#                    \   /
#                     \ /
# +=============================================+
# | .  ' .  ' .  ' .  ' .  ' .  ' .  ' .  ' .  '|
# | .  ' .  ' .  ' .  ' .  ' .  ' .  ' .  ' .  '|
# | .  ' .  ' .  ' .  ' .  ' .  ' .  ' .  ' .  '|
# 📺 TV2's channel is 3 and volume level is 2 📺
# | .  ' .  ' .  ' .  ' .  ' .  ' .  ' .  ' .  '|
# | .  ' .  ' .  ' .  ' .  ' .  ' .  ' .  ' .  '|
# | .  ' .  ' .  ' .  ' .  ' .  ' .  ' .  ' .  '|
# |---------------------------------------------|
# |                   TV #2                 🔵  |
# +=============================================+
# O-O                                         O-O

TestTV()   
