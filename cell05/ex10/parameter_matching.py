#!/usr/bin/env python3
import sys #ต้องrunในbashผลถึงจะออกตามโจทย์

if len(sys.argv) == 2:
    parameter = sys.argv[1]
    user_input = input("What was the parmeter? ")

    if user_input == parameter:
        print("Good jod!")
    else:
        print("Nope, sorry...")
else:
    print("none")