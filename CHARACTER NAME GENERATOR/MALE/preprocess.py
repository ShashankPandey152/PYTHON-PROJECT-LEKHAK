# Import the libraries
import re

# Load a doc
def load_doc(filename):
    file = open(filename, "r", encoding="ISO-8859-1")
    doc = file.read()
    lines = doc.split("\n")
    for i in range(len(lines)):
        lines[i] = re.sub('[^a-zA-Z]', '', lines[i])   
    return lines

# Loop through all the name files
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
             'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

names = []
for alphabet in alphabets:
    names.append(load_doc(alphabet + "-boy.txt"))
    print(alphabet + " done!")
    
# Write to csv file
file = open('boy-data.csv', 'w')
i = 1
for name_list in names:
    for name in name_list:
        file.write(name + "\n")
    print(str(i) + " done!")
    i += 1
file.close()

# Randomize names in boy-data
import pandas as pd

df = pd.read_csv('boy-data.csv', header=None)

ds = df.sample(frac=1)

ds.to_csv('boy-data-new.csv')