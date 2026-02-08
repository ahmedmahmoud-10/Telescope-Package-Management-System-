from OpticalToolbox import OpticalToolbox


class Package:
    __count = 0
    __sort_by = 3  # 1=OTA type, 2=physical mount type, 3=package number

    def __init__(self, ota, mount, eps):
        self.__ota = ota
        self.__mount = mount
        self.__eps = list(eps)
        Package.__count += 1
        self.__package_number = Package.__count

    @staticmethod
    def sort_by_ota():
        Package.__sort_by = 1

    @staticmethod
    def sort_by_mount():
        Package.__sort_by = 2

    @staticmethod
    def sort_by_number():
        Package.__sort_by = 3

    @staticmethod
    def get_sort_key():
        return Package.__sort_by

    def __lt__(self, other):
        if not isinstance(other, Package):
            return NotImplemented
        if Package.__sort_by == 1:
            return self.get_ota().get_type() < other.get_ota().get_type()
        if Package.__sort_by == 2:
            return (
                self.get_mount().get_physical_mount_type()
                < other.get_mount().get_physical_mount_type()
            )
        return self.get_package_number() < other.get_package_number()

    def get_package_number(self):
        return self.__package_number

    def set_ota(self, ota):
        self.__ota = ota

    def get_ota(self):
        return self.__ota

    def set_mount(self, mount):
        self.__mount = mount

    def get_mount(self):
        return self.__mount

    def add_ep(self, ep):
        self.__eps.append(ep)

    def drop_ep(self, index):
        return self.__eps.pop(index)

    def get_eps(self):
        return self.__eps

    def __str__(self):
        retval = f"***** PACKAGE {self.__package_number} *****\n"
        retval += f"{self.__ota}\n"
        retval += f"{self.__mount}\n"
        if len(self.__eps) == 0:
            retval += "Package has no eyepieces."
        else:
            for ep in self.__eps:
                retval += f"{ep}\n"
        return retval

    def validate_package(self):
        if self.__ota is None:
            return "Package missing OTA."
        if self.__mount is None:
            return "Package missing mount."
        if len(self.__eps) == 0:
            return "Package has no eyepieces."

        if self.__ota.get_mount_plate_type() != self.__mount.get_mount_plate_type():
            return "OTA and mount plate types are incompatible."

        differential = self.__ota.get_weight() - self.__mount.get_weight_rating()
        if differential > 0:
            return f"OTA is {differential}kg too heavy for mount."

        ep_keep_list = []
        for ep_index in range(len(self.__eps)):
            if OpticalToolbox.eyepiece_usability(self.__ota, self.__eps[ep_index]):
                ep_keep_list.append(self.__eps[ep_index])

        if len(ep_keep_list) == 0:
            return "No supplied eyepieces were compatible."

        self.__eps = ep_keep_list
        return "OK"
