from OpticalToolbox import OpticalToolbox


class Mount:
    """
    Represents a telescope mount.
    """

    __physical_types = {
        "T": "Tripod",
        "D": "Dobsonian Base",
    }

    __motion_types = {
        "AA": "Altitude-Azimuth",
        "EQ": "Equatorial",
    }

    def __init__(self, p_code, m_code, mp_code, weight_rating, goto):
        self.__p_code = p_code
        self.__m_code = m_code
        self.__mp_code = mp_code
        self.__weight_rating = weight_rating
        self.__goto = goto

    def get_physical_mount_type(self):
        return self.__p_code

    def get_motion_mount_type(self):
        return self.__m_code

    def get_mount_plate_type(self):
        return self.__mp_code

    def get_weight_rating(self):
        return self.__weight_rating

    def get_goto(self):
        return self.__goto

    def __str__(self):
        physical = Mount.__physical_types.get(self.__p_code, "Unknown")
        motion = Mount.__motion_types.get(self.__m_code, "Unknown")
        plate = OpticalToolbox.mount_plate_type_to_text(self.__mp_code)
        goto_text = "Yes" if str(self.__goto).strip().upper().startswith("Y") else "No"
        return (
            "Mount:\n"
            f"Physical Type: {physical}\n"
            f"Motion Type: {motion}\n"
            f"Mount Plate Type: {plate}\n"
            f"Mount Weight Rating: {self.__weight_rating}kg maximum\n"
            f"Mount is GOTO: {goto_text}"
        )
