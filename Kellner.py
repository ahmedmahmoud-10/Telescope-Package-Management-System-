from EP import EP

class Kellner(EP):
    def __init__(self, ep_afov, ep_focal_length):
        super().__init__("K", ep_afov, ep_focal_length) # this is a Kellner eyepiece
