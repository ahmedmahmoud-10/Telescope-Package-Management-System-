from EP import EP

class Nagler(EP):
    def __init__(self, ep_afov, ep_focal_length):
        super().__init__("N", ep_afov, ep_focal_length) # this is a Nagler eyepiece
