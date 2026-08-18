# ==============================================================================
# AETHEL-Engine v1.0
# Copyright (c) 2026 FrostmoonCyber. All Rights Reserved.
# Author: FrostmoonCyber
# Repository: https://github.com/FrostmoonCyber/AETHEL-Engine
# 
# Licensed under PolyForm Noncommercial License 1.0.0.
# ==============================================================================

import sys
import argparse

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
                    description='Trying out argparser library and its funtionality',
                    epilog='Having fun')                               
    parser.add_argument("-t","--target", help = "Domain or audit IP", type= str)
    parser.add_argument("--version", "-v", action= "version", help = "Show version", version='%(prog)s 1.0.0' )
    args = parser.parse_args()

    print(BANNER)
    if args.target:
      print(f"[+] Starting audit in: {args.target}")
    else:
      parser.print_help()

if __name__ == '__main__':
    main()

                                    


