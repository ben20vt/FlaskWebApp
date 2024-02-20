import pandas as pd

def TrimIngestData(table):
    table = table.iloc[:,2]
    for i in range(len(table)):
        if str(table[i]) == "nan":
            table[i] = 0
        elif "Version" in str(table[i]):
            table[i] = 0
        else:
            table[i] = 1

    for i in range(len(table)):
        if i == len(table):
            Output = 1
        elif i == len(table) - 1:
            table[i] = 0
        else:
            table[i] = table[i + 1] - table[i]
    index = []
    for i in range(len(table)):        
        if table[i] == -1:
            index.append(i)
        else:
            Donothing = 1

    EndofData = max(index)   
    return EndofData     