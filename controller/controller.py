import sys
import os, time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.attack import *
from model.scanner import *
from model.networkmap import *
from model.tester import *

# Call the function

def call_scan():
    print("\n--------------------------------")
    print("\nStarting Network traffic Sniffer")
    print("\n--------------------------------")

    startsniff()
    main_menu()

def call_mitm():
    print("\n------------------")
    print("\nStarting MiTM Tool")
    print("\n------------------")

    attack_start()
    main_menu()

def call_networkmap():
    print("\n-----------------------")
    print("\nStarting Network Mapper")
    print("\n-----------------------")

    plot_map()
    main_menu

def main_menu():
    print("\n################################################################")
    print("\n# EECS 4480 Project - Network Intrustion Toolkit               #")
    print("\n# By: Jacob Medeiros 217248824                                 #")
    print("\n#                                                              #")
    print("\n# (1) Capture Network Traffic                                  #")
    print("\n# (2) Run a MiTM Attack                                        #")
    print("\n# (3) Map a Network Topology with a given pcap file            #")
    print("\n# (4) Exit                                                     #")
    print("\n################################################################")
    #display()
    choice = input()

    match choice:
        case '1':
            call_scan()
        case '2':
            call_mitm()
        case '3':
            call_networkmap()
        case '4':
            print("Goodbye")
            exit

main_menu()