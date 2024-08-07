class Television2:
    objectCnt=0
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on
        self.objectCnt +=1
        
    def show(self):
        print(self.channel, self.volume, self.on, self.objectCnt)
        
    
    
    