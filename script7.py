import string
import pathlib
import datetime

alphabet = string.ascii_uppercase
filenames = [chr for chr in alphabet] + [f"{chr}{chr}.txt" for chr in alphabet] + [f"{chr}{chr}{chr}.csv" for chr in alphabet]

for filename in filenames:
    with open(filename, "w") as f:
        f.write("こんにちは")

for path in pathlib.Path(".").glob("*.csv"):
    now = datetime.datetime.now()
    path_new = f'{path.stem}_test_{now:%Y%m%d_%H%M}.csv'
    path.rename(path_new)
