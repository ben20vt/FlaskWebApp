# table0 = tables[0] # Select table of interest
# table = tables[0]
# EndofData = TrimIngestData.TrimIngestData(table0)
# #EndofData = EndofData + 1
# #table = table0.iloc[7:EndofData,0:6]
# end = len(table)
# length = end - EndofData - 1
# to_drop = [0, 1, 2, 3, 4, 5, 6]
# for i in range(length):
#     to_drop.append(i + EndofData + 1)
# table = table.drop(to_drop)


# backup_table = tables[6]
# EndofData_backup = TrimIngestData.TrimIngestData(backup_table)
# EndofData_backup = EndofData_backup + 1
# backup_table = backup_table.iloc[0:EndofData,0:6]

# maintabletype = type(backup_table.iloc[1,2])
# backuptabletype = type(table.iloc[1,2])

# if maintabletype == int and backuptabletype == int:
#     tables = pd.read_html(url) # Returns list of all tables on page
#     table0 = tables[0] # Select table of interest

#     EndofData = TrimIngestData.TrimIngestData(table0)
#     EndofData = EndofData + 1
#     table = table0.iloc[7:EndofData,0:6]
#     backup_table = tables[6]
#     EndofData_backup = TrimIngestData.TrimIngestData(backup_table)
#     EndofData_backup = EndofData_backup + 1
#     backup_table = backup_table.iloc[0:EndofData,0:6]
# else:
#     Output = "Success"

# maintabletype = type(backup_table.iloc[1,2])
# backuptabletype = type(table.iloc[1,2])

# if maintabletype == int and backuptabletype == int:
#    tables = pd.read_html(url) # Returns list of all tables on page
#    table0 = tables[0] # Select table of interest
#    EndofData = TrimIngestData.TrimIngestData(table0)
#    EndofData = EndofData + 1
#    table = table0.iloc[7:EndofData,0:6]
#    backup_table = tables[6]
#    EndofData_backup = TrimIngestData.TrimIngestData(backup_table)
#    EndofData_backup = EndofData_backup + 1
#    backup_table = backup_table.iloc[0:EndofData,0:6]
# else:
#     Output = "Success"   

# maintabletype = type(backup_table.iloc[1,2])
# backuptabletype = type(table.iloc[1,2])

# if maintabletype == int and backuptabletype == int:
#    tables = pd.read_html(url) # Returns list of all tables on page
#    table0 = tables[0] # Select table of interest
#    EndofData = TrimIngestData.TrimIngestData(table0)
#    EndofData = EndofData + 1
#    table = table0.iloc[7:EndofData,0:6]
#    backup_table = tables[6]
#    EndofData_backup = TrimIngestData.TrimIngestData(backup_table)
#    EndofData_backup = EndofData_backup + 1
#    backup_table = backup_table.iloc[0:EndofData,0:6]
# else:
#     Output = "Success"   

# maintabletype = type(backup_table.iloc[1,2])
# backuptabletype = type(table.iloc[1,2])

# if maintabletype == int and backuptabletype == int:
#    IncidentType = "Unknown"
# elif maintabletype == int and backuptabletype != int:
#     IncidentType_DB = table
# elif maintabletype != int and backuptabletype == int:
#     IncidentType_DB = backup_table
# else: 
#     IncidentType = "Unknown"