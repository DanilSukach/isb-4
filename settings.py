import json

SETTINGS = {
    "card_number_file": "files/card_number.txt",
    "statistics_file": "files/statistics.txt",
    "visual_directory": "files",
    "hash": "70ba6e37c3be80134c2fd8563043c0cb9278a43116b3bc2dfad03e2e455ed473",
    "bins": [446674],
    "last_numbers": "1378",
}


if __name__ == "__main__":
    with open("settings.json", "w") as fp:
        json.dump(SETTINGS, fp)