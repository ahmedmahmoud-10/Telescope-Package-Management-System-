from Reflector import Reflector

class Newtonian(Reflector):
    def __init__(self, ota_aperture, ota_focal_length, mount_plate_type, weight):
        super().__init__("N", ota_aperture, ota_focal_length, mount_plate_type, weight)
