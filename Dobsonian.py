from Mount import Mount

class Dobsonian(Mount):
    def __init__(self,weight_rating,goto):
        super().__init__("D","AA","NA",weight_rating,goto)
