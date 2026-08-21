# ==============================================================================
# AETHEL-Engine v1.0
# Copyright (c) 2026 FrostmoonCyber. All Rights Reserved.
# Author: FrostmoonCyber
# Repository: https://github.com/FrostmoonCyber/AETHEL-Engine
# 
# Licensed under PolyForm Noncommercial License 1.0.0.
# ==============================================================================

import argparse
import sys

from aethel.core.auditor import AethelAuditor

BANNER= """[0;37;40m ╒════════╗  ╒═════════╗ ╒══════════╗ ╒════╗╒════╗ ╒═════════╗ ╒════╗               ╒═════════╗  ╒════╗   ╒════╗ ╒════════╗  ╒══════╗  ╒════╗   ╒════╗ ╒═════════╗[0m
[0;37;40m │  ╓──┐  ║  └┐  ╓───┐ ║ │ ╓─┐  ╓─┐ ║ └┐  ╓╜└┐  ╓╜ └┐  ╓───┐ ║ └┐  ╓╜               └┐  ╓───┐ ║  │    ╚╗  └┐  ╓╜ │  ╓───┐ ║  └─┐  ╓─╜  │    ╚╗  └┐  ╓╜ └┐  ╓───┐ ║[0m
[0;37;40m │  ║  │  ║   │  ║   └─╜ └─╜ │  ║ └─╜  │  ║  │  ║   │  ║   └─╜  │  ║                 │  ║   └─╜  │  ╟┐ ╚╗  │  ║  │  ║   └─╜    │  ║    │  ╟┐ ╚╗  │  ║   │  ║   └─╜[0m
[0;37;40m │  ╚══╛  ║   │  ╚══╗        │  ║      │  ╚══╛  ║   │  ╚══╗     │  ║       ╒══════╗  │  ╚══╗     │  ║└┐ ╚╗ │  ║  │  ║          │  ║    │  ║└┐ ╚╗ │  ║   │  ╚══╗   [0m
[0;37;40m │  ╓──┐  ║   │  ╓──╜        │  ║      │  ╓──┐  ║   │  ╓──╜     │  ║       └──────╜  │  ╓──╜     │  ║ └┐ ╚╗│  ║  │  ║ ╒════╗   │  ║    │  ║ └┐ ╚╗│  ║   │  ╓──╜   [0m
[0;37;40m │  ║  │  ║   │  ║   ╒═╗     │  ║      │  ║  │  ║   │  ║   ╒═╗  │  ║   ╒═╗           │  ║   ╒═╗  │  ║  └┐ ╚╡  ║  │  ║ └┐  ╓╜   │  ║    │  ║  └┐ ╚╡  ║   │  ║   ╒═╗[0m
[0;37;40m╒╛  ╚╗╒╛  ╚╗ ╒╛  ╚═══╛ ║    ╒╛  ╚╗    ╒╛  ╚╗╒╛  ╚╗ ╒╛  ╚═══╛ ║ ╒╛  ╚═══╛ ║          ╒╛  ╚═══╛ ║ ╒╛  ╚╗  └┐    ║  │  ╚══╛  ║  ╒═╛  ╚═╗ ╒╛  ╚╗  └┐    ║  ╒╛  ╚═══╛ ║[0m
[0;37;40m└────╜└────╜ └─────────╜    └────╜    └────╜└────╜ └─────────╜ └─────────╜          └─────────╜ └────╜   └────╜  └────────╜  └──────╜ └────╜   └────╜  └─────────╜[0m"""

def main():
    parser = argparse.ArgumentParser(
                    prog='AETHEL-Engine | VIP Digital Footprint Audit Framework',
                    description= ('Modular security scanner designed to audit digital footprints, '
                                  'evaluate HTTP headers, and detect infrastructure risks for VIP entities.'),
                    epilog=(
        'Driven by the discipline of a musician and the precision of a telecommunications technician.\n'
        'Developed by FrostmoonCyber | https://github.com/FrostmoonCyber/AETHEL-Engine')
    )                               
    parser.add_argument("-t","--target", help = "Domain or audit IP", type= str)
    parser.add_argument("--version", "-v", action= "version", help = "Show version", version='%(prog)s 1.0.0' )
    args = parser.parse_args()

    print(BANNER)
    if args.target:
      auditor = AethelAuditor(args.target) #Instantiate the class, passing the console target
      report = auditor.execute_analysis()  # Run the analysis and save/print the response
      print(report)
    else:
      parser.print_help()

if __name__ == '__main__':
    main()

                                    


