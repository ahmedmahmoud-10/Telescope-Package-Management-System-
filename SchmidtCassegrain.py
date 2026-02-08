from Catadioptric import Catadioptric

class SchmidtCassegrain(Catadioptric):
    def __init__(self, ota_aperture, ota_focal_length, mount_plate_type, weight):
        super().__init__("S", ota_aperture, ota_focal_length, mount_plate_type, weight)
