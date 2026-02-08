from Catadioptric import Catadioptric

class MaksutovCassegrain(Catadioptric):
    def __init__(self, ota_aperture, ota_focal_length, mount_plate_type, weight):
        super().__init__("M", ota_aperture, ota_focal_length, mount_plate_type, weight)
