from OpticalToolbox import OpticalToolbox


class OTA:
    """
    Optical Tube Assembly model.
    """

    __ota_types = {
        "G": "Galilean (Refractor)",
        "N": "Newtonian (Reflector)",
        "S": "Schmidt-Cassegrain (Catadioptric)",
        "M": "Maksutov-Cassegrain (Catadioptric)",
    }

    def __init__(self, ota_type, ota_aperture, ota_focal_length, mount_plate_type, weight):
        self.__ota_type = ota_type
        self.__ota_aperture = ota_aperture
        self.__ota_focal_length = ota_focal_length
        self.__mount_plate_type = mount_plate_type
        self.__weight = weight

    def set_type(self, ota_type):
        self.__ota_type = ota_type

    def set_aperture(self, ota_aperture):
        self.__ota_aperture = ota_aperture

    def set_focal_length(self, ota_focal_length):
        self.__ota_focal_length = ota_focal_length

    def get_type(self):
        return self.__ota_type

    def get_aperture(self):
        return self.__ota_aperture

    def get_focal_length(self):
        return self.__ota_focal_length

    def get_mount_plate_type(self):
        return self.__mount_plate_type

    def get_weight(self):
        return self.__weight

    def __str__(self):
        ota_type_text = OTA.__ota_types.get(self.__ota_type, "Unknown")
        mount_plate_text = OpticalToolbox.mount_plate_type_to_text(self.__mount_plate_type)
        return (
            f"Type: {ota_type_text}\n"
            f"Aperture: {self.__ota_aperture}mm\n"
            f"Focal Length: {self.__ota_focal_length}mm\n"
            f"Mount Plate Type: {mount_plate_text}\n"
            f"OTA Weight: {self.__weight}kg"
        )
