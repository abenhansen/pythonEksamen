værdier={'to':2, 'tre':3, 'fire':4, 'fem':5,'seks':6, 'syv':7, 'otte':8, 'ni':9, 'ti':10, 'bonde':10, 'dronning':10, 'konge':10, 'es':1}
class Hånd:

    def __init__(self):
        self.korthånd = []
        self.værdi = 0
        self.skjultVærdi = 0



    def tilføj_kort(self,kort):
        self.korthånd.append(kort)
        self.værdi += værdier[kort.nummer]
        for k in self.korthånd[1:]:
            self.skjultVærdi+=værdier[kort.nummer]
    def tjekes(self):
        har_es=False
        for kort in self.korthånd:
            if kort.nummer =='es':
                har_es=True
        if har_es and self.værdi <= 11:
            self.værdi+=10
        return self.værdi


