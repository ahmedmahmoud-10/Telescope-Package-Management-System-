import argparse

from AltAz import AltAz
from Dobsonian import Dobsonian
from EQ import EQ
from Galilean import Galilean
from Kellner import Kellner
from MaksutovCassegrain import MaksutovCassegrain
from Nagler import Nagler
from Newtonian import Newtonian
from Orthographic import Orthographic
from Package import Package
from Plossl import Plossl
from SchmidtCassegrain import SchmidtCassegrain


PACKAGE_TUPLES = [
    (8, 4, (17, 6)),
    (9, 4, (19, 4, 7)),
    (3, 2, (0, 16)),
    (4, 11, (12, 4, 15)),
    (1, 3, (16, 7)),
    (7, 8, (5,)),
    (14, 7, (11, 12, 7)),
    (14, 10, (17,)),
    (8, 8, (17, 5, 6)),
    (5, 11, (2, 4)),
    (12, 4, (0, 19, 13)),
    (11, 1, (10, 5)),
    (2, 16, (12, 5, 15)),
    (9, 6, (12, 6)),
    (11, 5, (5,)),
    (14, 1, (9, 18, 19)),
    (15, 8, (10, 13)),
    (7, 15, (4, 14)),
    (1, 17, (15,)),
    (8, 7, (18, 19, 5)),
    (3, 9, (12, 14)),
    (13, 7, (9, 4)),
    (13, 14, (5,)),
    (3, 0, (19, 15)),
    (7, 2, (0, 8)),
    (10, 19, (5,)),
    (13, 2, (8, 10, 6)),
    (3, 11, (19, 11, 4)),
    (15, 19, (8, 15)),
    (8, 13, (2, 15)),
    (0, 13, (19, 4, 7)),
    (7, 8, (18, 3, 14)),
]


def selection_sort_packages(package_list):
    for base in range(len(package_list) - 1):
        smallest = base
        for scan in range(base + 1, len(package_list)):
            if package_list[scan] < package_list[smallest]:
                smallest = scan
        package_list[base], package_list[smallest] = package_list[smallest], package_list[base]


def binary_search_packages(package_list, target, start, end):
    if start > end:
        return None

    key = Package.get_sort_key()
    mid = (start + end) // 2
    if key == 1:
        current = package_list[mid].get_ota().get_type()
    else:
        current = package_list[mid].get_mount().get_physical_mount_type()

    if current == target:
        return package_list[mid]
    if current < target:
        return binary_search_packages(package_list, target, mid + 1, end)
    return binary_search_packages(package_list, target, start, mid - 1)


def print_packages(packages):
    print(f"IDX {'Package #':10s}{'OTA Type':10s}Physical Mount")
    print(f"=== {'=========':10s}{'========':10s}==============")
    for idx, package in enumerate(packages, start=1):
        print(
            f"{idx:<4d}"
            f"{package.get_package_number():<10d}"
            f"{package.get_ota().get_type():10s}"
            f"{package.get_mount().get_physical_mount_type():10s}"
        )


def load_otas(path):
    otas = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            if not line.strip() or line.startswith("#"):
                continue
            data = [value.strip() for value in line.split(",")]
            if data[0] == "G":
                ota = Galilean(int(data[1]), int(data[2]), data[3], int(data[4]))
            elif data[0] == "N":
                ota = Newtonian(int(data[1]), int(data[2]), data[3], int(data[4]))
            elif data[0] == "S":
                ota = SchmidtCassegrain(int(data[1]), int(data[2]), data[3], int(data[4]))
            else:
                ota = MaksutovCassegrain(int(data[1]), int(data[2]), data[3], int(data[4]))
            otas.append(ota)
    return otas


def load_eps(path):
    eps = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            if not line.strip() or line.startswith("#"):
                continue
            data = [value.strip() for value in line.split(",")]
            if data[0] == "K":
                ep = Kellner(int(data[1]), int(data[2]))
            elif data[0] == "O":
                ep = Orthographic(int(data[1]), int(data[2]))
            elif data[0] == "P":
                ep = Plossl(int(data[1]), int(data[2]))
            else:
                ep = Nagler(int(data[1]), int(data[2]))
            eps.append(ep)
    return eps


def load_mounts(path):
    mounts = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            if not line.strip() or line.startswith("#"):
                continue
            data = [value.strip() for value in line.split(",")]
            if data[0] == "D":
                mount = Dobsonian(int(data[3]), data[4])
            elif data[1] == "AZ":
                mount = AltAz(data[2], int(data[3]), data[4])
            else:
                mount = EQ(data[2], int(data[3]), data[4])
            mounts.append(mount)
    return mounts


def build_packages(otas, mounts, eps):
    packages = []
    for ota_idx, mount_idx, ep_indexes in PACKAGE_TUPLES:
        package_eps = [eps[ep_idx] for ep_idx in ep_indexes]
        packages.append(Package(otas[ota_idx], mounts[mount_idx], package_eps))
    return packages


def command_report(packages):
    print("Sorting by Physical Mount Type\n")
    Package.sort_by_mount()
    selection_sort_packages(packages)
    print_packages(packages)
    print("\nSorting by OTA Type\n")
    Package.sort_by_ota()
    selection_sort_packages(packages)
    print_packages(packages)
    print("\nSorting by Package Number\n")
    Package.sort_by_number()
    selection_sort_packages(packages)
    print_packages(packages)


def command_search(packages, ota_type, mount_type):
    if ota_type:
        Package.sort_by_ota()
        selection_sort_packages(packages)
        result = binary_search_packages(packages, ota_type, 0, len(packages) - 1)
        print(result if result else "No package found for that OTA type.")

    if mount_type:
        Package.sort_by_mount()
        selection_sort_packages(packages)
        result = binary_search_packages(packages, mount_type, 0, len(packages) - 1)
        print(result if result else "No package found for that mount type.")


def command_validate(packages):
    failed = 0
    for package in packages:
        result = package.validate_package()
        if result != "OK":
            failed += 1
            print(f"Package {package.get_package_number()}: {result}")
    if failed == 0:
        print("All packages validated successfully.")
    else:
        print(f"{failed} package(s) need attention.")


def _prompt_choice(prompt, valid_choices):
    while True:
        value = input(prompt).strip().upper()
        if value in valid_choices:
            return value
        print(f"Invalid choice. Expected one of: {', '.join(valid_choices)}")


def run_menu(packages):
    while True:
        print("\n=== Telescope Catalog Menu ===")
        print("1) Show report")
        print("2) Search by OTA type")
        print("3) Search by mount type")
        print("4) Validate packages")
        print("5) Exit")
        choice = _prompt_choice("Select an option (1-5): ", {"1", "2", "3", "4", "5"})

        if choice == "1":
            command_report(packages)
        elif choice == "2":
            ota_type = _prompt_choice("Enter OTA type [G/N/S/M]: ", {"G", "N", "S", "M"})
            command_search(packages, ota_type, None)
        elif choice == "3":
            mount_type = _prompt_choice("Enter mount type [T/D]: ", {"T", "D"})
            command_search(packages, None, mount_type)
        elif choice == "4":
            command_validate(packages)
        else:
            print("Goodbye.")
            break


def parse_args():
    parser = argparse.ArgumentParser(description="Telescope package catalog and validator.")
    parser.add_argument("--otas", default="otas.txt", help="Path to OTA dataset.")
    parser.add_argument("--eps", default="eps.txt", help="Path to eyepiece dataset.")
    parser.add_argument("--mounts", default="mounts.txt", help="Path to mount dataset.")

    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("report", help="Show sorted package reports.")

    search_parser = subparsers.add_parser("search", help="Find first matching package.")
    search_parser.add_argument("--ota-type", choices=["G", "N", "S", "M"])
    search_parser.add_argument("--mount-type", choices=["T", "D"])

    subparsers.add_parser("validate", help="Validate package compatibility.")
    subparsers.add_parser("menu", help="Run interactive menu mode.")

    return parser.parse_args()


def main():
    args = parse_args()
    otas = load_otas(args.otas)
    eps = load_eps(args.eps)
    mounts = load_mounts(args.mounts)
    packages = build_packages(otas, mounts, eps)

    if not args.command or args.command == "report":
        command_report(packages)
    elif args.command == "search":
        if not args.ota_type and not args.mount_type:
            raise SystemExit("Use --ota-type and/or --mount-type with the search command.")
        command_search(packages, args.ota_type, args.mount_type)
    elif args.command == "validate":
        command_validate(packages)
    elif args.command == "menu":
        run_menu(packages)


if __name__ == "__main__":
    main()
