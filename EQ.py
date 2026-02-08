from Tripod import Tripod

class EQ(Tripod):
    def __init__(self,mp_code,weight_rating,goto):
        super().__init__("T","EQ",mp_code,weight_rating,goto)
