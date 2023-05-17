from TVProgram import TV

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