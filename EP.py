class EP:
    """
    Eyepiece model.
    """

    __ep_types = {
        "K": "Kellner",
        "O": "Orthographic",
        "P": "Plossl",
        "N": "Nagler",
    }

    def __init__(self, ep_type, ep_afov, ep_focal_length):
        self.__ep_type = ep_type
        self.__ep_afov = ep_afov
        self.__ep_focal_length = ep_focal_length

    def set_type(self, ep_type):
        self.__ep_type = ep_type

    def set_afov(self, ep_afov):
        self.__ep_afov = ep_afov

    def set_focal_length(self, ep_focal_length):
        self.__ep_focal_length = ep_focal_length

    def get_type(self):
        return self.__ep_type

    def get_afov(self):
        return self.__ep_afov

    def get_focal_length(self):
        return self.__ep_focal_length

    def __str__(self):
        ep_type_text = EP.__ep_types.get(self.__ep_type, "Unknown")
        return (
            f"Type:{ep_type_text:>18}\n"
            f"afov:{str(self.__ep_afov) + 'deg':>15}\n"
            f"Focal Length:{str(self.__ep_focal_length) + 'mm':>8}"
        )
