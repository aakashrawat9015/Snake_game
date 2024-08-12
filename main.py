
class sol:
    def __init__(self):
        self.arr = [11,2,3,4,5,6,7,8]
        self.s=11
        self.start = 0
        self.ans()
        
    def ans(self):
        for i in range(0, 8):
            self.sum = 0
            for j in range(i,8):
                self.sum = self.sum + self.arr[j]
                if self.sum == self.s:
                    print(i+1 , j+1)
                break
s1 = sol()
