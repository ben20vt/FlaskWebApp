import pandas as pd

def TrimIngestData(table):
    table = table.iloc[:,1]
    table = table.reset_index()
    for i in range(len(table)):
        if str(table.iloc[i,1]) == "nan":
            table.iloc[i,1] = 0
        elif "Version" in str(table.iloc[i,1]):
            table.iloc[i,1] = 0
        elif "(hX_5) hX_5.setResourceServer" in str(table.iloc[i,1]):
            table.iloc[i,1] = 0
        else:
            table.iloc[i,1] = 1

    for i in range(len(table)):
        if i == len(table):
            Output = 1
        elif i == len(table) - 1:
            table.iloc[i,1] = 0
        else:
            table.iloc[i,1] = table.iloc[i + 1,1] - table.iloc[i,1]
    index = []
    for i in range(len(table)):        
        if table.iloc[i,1] == -1:
            index.append(i)
        else:
            Donothing = 1

    EndofData = min(index)
    EndofData = table.iloc[EndofData,0]   
    return EndofData     