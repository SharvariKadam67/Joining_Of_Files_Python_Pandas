import pandas as pd
import os
from datetime import date, time, datetime

file_path = r"C:\Users\SharvariKadam\Desktop\Playground\Stock_split"


HoldingFile = [
    Holding_filename
    for Holding_filename in os.listdir(file_path)
    if "holding" in Holding_filename.casefold()
    latest_holdingfile = max(os.path.gettime(HoldingFile))        
]
print(HoldingFile)

if HoldingFile:
    Latest_HoldingFile = max(
        HoldingFile,
        key=lambda filename: os.path.getctime(
            os.path.join(file_path, filename)
        )
    )
    print("Latest Holdings file:", Latest_HoldingFile)
else:
    print("No Holding File")

StockSplitFile = [
    stocksplit_filename
    for stocksplit_filename in os.listdir(file_path)
    if "stocksplit" in stocksplit_filename.casefold()
]
print(StockSplitFile)











