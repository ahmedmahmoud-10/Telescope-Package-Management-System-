from EP import EP

class Orthographic(EP):
    def __init__(self, ep_afov, ep_focal_length):
        super().__init__("O", ep_afov, ep_focal_length) # this is an Orthographic eyepiece
