import os
import pandas as pd


list6 = [files for files in os.listdir("../data") if files.endswith(".csv")]
print(list6)



