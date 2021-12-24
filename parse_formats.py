#!/usr/bin/env python3
"""parse_formats.py
Description of parse_formats.py.
"""
import csv
import re
from pprint import pprint

REGEX = r'([\w ]+)\((.+)\)([\w() -]+):[\D .]+(\d+)'
FORMATS = """CRM:
8k (29.97p/25.00p/24.00p/23.98p) Raw: Approx. 2600 Mbps
8k (29.97p/25.00p) Raw (Light): Approx. 1700 Mbps
8k (24.00p/23.98p) Raw (Light): Approx. 1350 Mbps
MOV: MP4 H.264 Canon Log off
8K (29.97p/25.00p/24.00p*/23.98p) ALL-I: Approx. 1300 Mbps
8K (29.97p/25.00p/24.00p*/23.98p) IPB: Approx. 470 Mbps
8K (29.97p/25.00p/24.00p*/23.98p) IPB (Light): Approx. 230 Mbps
4K (119.9p / 100p) ALL-I: Approx. 1880 Mbps
4K (59.94p/50.00p) ALL-I: Approx. 940 Mbps
4K (59.94p/50.00p) IPB: Approx. 230 Mbps
4K (59.94p/50.00p) IPB (Light): Approx. 120 Mbps
4K (29.97p/25.00p/24.00p/23.98p) ALL-I: Approx. 470 Mbps
4K (29.97p/25.00p/24.00p/23.98p) IPB: Approx. 120 Mbps
4K (29.97p/25.00p/24.00p/23.98p) IPB (Light): Approx. 60 Mbps
Full HD (119.9p/100p) ALL-I: Approx. 360 Mbps
Full HD (59.94p/50.00p) ALL-I: Approx. 180 Mbps
Full HD ( 59.94p/50.00p) IPB : Approx. 60 Mbps
Full HD ( 59.94p/50.00p) IPB (Light): Approx.35 Mbps
Full HD (29.97p/25.00p/24.00p/23.98p) ALL-I: Approx. 90 Mbps
Full HD (29.97p/25.00p/24.00p/23.98p) IPB: Approx. 30 Mbps
Full HD (29.97p/25.00p) IPB (Light) : Approx. 12 Mbps
8K Time Lapse (29.97p/25.00p) ALL-I: Approx. 1300 Mbps
4K Time Lapse (29.97p/25.00p)ALL-I : Approx. 470 Mbps
Full HD Time Lapse (29.97p/25.00p) ALL-I: Approx. 90 Mbps
MOV: MP4 H.265 Canon Log on
8K (29.97p/25.00p/24.00p*/23.98p) ALL-I: Approx. 1300 Mbps
8K (29.97p/25.00p/24.00p*/23.98p) IPB: Approx. 680 Mbps
8K (29.97p/25.00p/24.00p*/23.98p) IPB (Light): Approx.340 Mbps
4K (119.9p / 100p) ALL-I : Approx. 1880 Mbps
4K (59.94p/50.00p) ALL-I : Approx. 1000 Mbps
4K (59.94p/50.00p) IPB: Approx. 340 Mbps
4K (59.94p/50.00p) IPB (Light): Approx. 170 Mbps
4K (29.97p/25.00p/24.00p/23.98p) ALL-I: Approx. 470 Mbps
4K (29.97p/25.00p/24.00p/23.98p) IPB: Approx. 170 Mbps
4K (29.97p/25.00p/24.00p/23.98p) IPB (Light): Approx. 85 Mbps
Full HD (119.9p/100p) ALL-I: Approx. 470 Mbps
Full HD (59.94p/50.00p) ALL-I: Approx. 230 Mbps
Full HD (59.94p/50.00p) IPB: Approx. 90 Mbps
Full HD (59.94p/50.00p) IPB (Light): Approx. 50 Mbps
Full HD (29.97p/25.00p/24.00p/23.98p) ALL-I: Approx. 135 Mbps
Full HD (29.97p/25.00p/24.00p/23.98p) IPB: Approx. 45 Mbps
Full HD (29.97p/25.00p) IPB (Light): Approx. 28 Mbps
8K Time Lapse (29.97p/25.00p) ALL-I: Approx. 1300 Mbps
4K Time Lapse (29.97p/25.00p) ALL-I : Approx. 470 Mbps
Full HD Time Lapse (29.97p/25.00p) ALL-I: Approx. 135 Mbps"""


def write_csv(path, formats):
    with open(path, mode='w') as csv_file:
        fieldnames = list(formats[0])
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for f in formats:
            writer.writerow(f)


def main():
    """docstring for main"""
    output = []
    for f in FORMATS.splitlines():
        match = re.findall(REGEX, f)
        if match:
            frame_rates = [x.strip('p*') for x in match[0][1].split('/')]
            for fps in frame_rates:
                item = {'resolution': match[0][0].strip(),
                        'fps': fps,
                        'format': match[0][2].strip(),
                        'bitrate': match[0][3].strip()}
                output.append(item)

    write_csv('formats.csv', output)
    pprint(output)


if __name__ == '__main__':
    main()
