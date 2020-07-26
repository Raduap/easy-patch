import Recognise
import pandas as pd
import csv




def PrintPatchResultBefore():
    print("------------------------------------------------------")
    print("--------------------debug 0.0.1-----------------------")
    with open('PatchWebdatabin.csv', "rt", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
    print("------------------------------------------------------")
