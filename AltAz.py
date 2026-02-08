from Tripod import Tripod

class AltAz(Tripod):
    def __init__(self,mp_code,weight_rating,goto):
        super().__init__("T","AA",mp_code,weight_rating,goto)
