from EP import EP


class Plossl(EP):
    def __init__(self, ep_afov, ep_focal_length):
        super().__init__("P", ep_afov, ep_focal_length)
