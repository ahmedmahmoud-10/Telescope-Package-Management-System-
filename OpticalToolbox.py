class OpticalToolbox:
    """
    Static helper functions for optical calculations.
    """

    __mount_plate_types = {
        "V": 'Vixen 1.75"',
        "L": 'Losmandy 3"',
        "NA": "Not Applicable - Dobsonian",
    }

    @staticmethod
    def effective_magnification(ota, ep):
        return OpticalToolbox.__formatted_return(
            ota.get_focal_length() / ep.get_focal_length()
        )

    @staticmethod
    def f_ratio(ota):
        return OpticalToolbox.__formatted_return(
            ota.get_focal_length() / ota.get_aperture()
        )

    @staticmethod
    def eyepiece_usability(ota, ep):
        # Typical practical bounds: ~3.5mm to 30mm exit pupil.
        magnification = ota.get_focal_length() / ep.get_focal_length()
        if magnification <= 0:
            return False
        exit_pupil = ota.get_aperture() / magnification
        return 3.5 <= exit_pupil <= 30.0

    @staticmethod
    def true_fov(ota, ep):
        magnification = ota.get_focal_length() / ep.get_focal_length()
        return OpticalToolbox.__formatted_return(ep.get_afov() / magnification)

    @staticmethod
    def __formatted_return(value):
        rounded = round(float(value), 2)
        return int(rounded) if rounded.is_integer() else rounded

    @staticmethod
    def mount_plate_type_to_text(mount_code):
        return OpticalToolbox.__mount_plate_types.get(mount_code, "Unknown")
