from OTA import OTA

class Galilean(OTA):
    def __init__(self, ota_aperture, ota_focal_length, mount_plate_type, weight):
        super().__init__("G", ota_aperture, ota_focal_length, mount_plate_type, weight)
