class Connected:
    def __init__(self,size):
        self.size = size
        self.lindex = [0 for x in range(self.size)]
        self.ticker = 1

    def connect(self,var1,var2):
        if self.lindex[var1] == 0 and self.lindex[var2] == 0:
            self.lindex[var1] = self.ticker
            self.lindex[var2] = self.ticker
            self.ticker = self.ticker + 1

        elif self.lindex[var1] != 0 and self.lindex[var2] == 0:
            self.lindex[var2] = self.lindex[var1]
        
        elif self.lindex[var2] != 0 and self.lindex[var1] == 0:
            self.lindex[var1] = self.lindex[var2]
        
        elif self.lindex[var1] != 0 and self.lindex[var2] != 0 and self.lindex[var1] != self.lindex[var2]:
            temp = self.lindex[var1]
            for n in range(self.size):
                if self.lindex[n -1] == temp:
                    self.lindex[n-1] = self.lindex[var2]
        
            
    def isConnected(self,var1,var2):
        if self.lindex[var1] == self.lindex[var2]:
            return True
        else:
            return False

    def display(self):
        print(self.lindex)
