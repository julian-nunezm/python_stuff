import xlrd #pip install xlrd
from pprint import pprint

#workbook = xlrd.open_workbook("Incidents.xlsx")
#worksheet = workbook.sheet_by_name("Export")
#workbook = xlrd.open_workbook("Incidents_Jared.xlsx")
#worksheet = workbook.sheet_by_name("Incidents_Jared")
workbook = xlrd.open_workbook("D:/extract.xlsx")
worksheet = workbook.sheet_by_name("Sheet1")

num_rows = worksheet.nrows
num_cols = worksheet.ncols

print(f"Total rows: {num_rows}, and Total columns: {num_cols}")

#----------------------------Array-----------------------------------------------
#incidents_array = []
#labels = []

#for i in range(0, num_cols, 1):
#    labels.append(worksheet.cell_value(0, i))
#pprint(labels)

#for curr_row in range(1, num_rows, 1):
#    incident = dict()
#    for curr_col in range(0, num_cols, 1):
#        incident[labels[curr_col]] = worksheet.cell_value(curr_row, curr_col)
#        incidents_array.append(incident)

#pprint(incidents_array)

#-----------------------------Dict-----------------------------------------------

incidents_dict = dict()

for curr_row in range(0, num_rows, 1):
    incident = dict()
    for curr_col in range(num_cols-1, -1, -1):
        if(curr_col != 0):
            #incident[worksheet.cell_value(0, curr_col)] = worksheet.cell_value(curr_row, curr_col)
            print(f"Row[{curr_row}] Col[{curr_col}]: {worksheet.cell_value(curr_row, curr_col)})")
        else:
            incidents_dict[worksheet.cell_value(curr_row, 0)] = incident

#pprint(incidents_dict)
#incident_to_find = "INC000001861326"
#print(f"The information about the incident {incident_to_find} is:\n")
#pprint(incidents_dict.get(incident_to_find))

#incident['Incident_Number'] = worksheet.cell_value(curr_row, 0)
#incident['Summary'] = worksheet.cell_value(curr_row, 1)
#incident['Notes'] = worksheet.cell_value(curr_row, 2)
#incident['STATUS'] = worksheet.cell_value(curr_row, 3)
#incident['priority'] = worksheet.cell_value(curr_row, 4)
#incident['Contact_Company'] = worksheet.cell_value(curr_row, 5)
#incident['Organization'] = worksheet.cell_value(curr_row, 6)
#incident['Department'] = worksheet.cell_value(curr_row, 7)
#incident['Service_Type'] = worksheet.cell_value(curr_row, 8)
#incident['ServiceCI'] = worksheet.cell_value(curr_row, 9)
#incident['Reported_Source'] = worksheet.cell_value(curr_row, 10)
#incident['Reported_Date'] = worksheet.cell_value(curr_row, 11)
#incident['Categorization_Tier_1'] = worksheet.cell_value(curr_row, 12)
#incident['Categorization_Tier_2'] = worksheet.cell_value(curr_row, 13)
#incident['Categorization_Tier_3'] = worksheet.cell_value(curr_row, 14)
#incident['Product_Categorization_Tier_1'] = worksheet.cell_value(curr_row, 15)
#incident['Product_Categorization_Tier_2'] = worksheet.cell_value(curr_row, 16)
#incident['Product_Categorization_Tier_3'] = worksheet.cell_value(curr_row, 17)
#incident['Assigned_Group'] = worksheet.cell_value(curr_row, 18)
#incident['Assigned_Support_Company'] = worksheet.cell_value(curr_row, 19)
#incident['Assigned_Support_Organization'] = worksheet.cell_value(curr_row, 20)
#incident['Owner_Support_Organization'] = worksheet.cell_value(curr_row, 21)
#incident['Owner_Group'] = worksheet.cell_value(curr_row, 22)
#incident['Owner_Support_Company'] = worksheet.cell_value(curr_row, 23)
#incident['Owner'] = worksheet.cell_value(curr_row, 24)
#incident['Resolved_Date'] = worksheet.cell_value(curr_row, 25)
#incident['z1D_Template_Name'] = worksheet.cell_value(curr_row, 26)
#incident['Attributed_To'] = worksheet.cell_value(curr_row, 27)
#incident['Service_Relief_Category'] = worksheet.cell_value(curr_row, 28)
#incident['CTX_Service_Relief_Category_Ev'] = worksheet.cell_value(curr_row, 29)
#incident['Resolution'] = worksheet.cell_value(curr_row, 30)
#incident['Resolution_Method'] = worksheet.cell_value(curr_row, 31)
#incident['Generic_Categorization_Tier_1'] = worksheet.cell_value(curr_row, 32)
#incident['Resolution_Category'] = worksheet.cell_value(curr_row, 33)
#incident['Resolution_Category_Tier_2'] = worksheet.cell_value(curr_row, 34)
#incident['Resolution_Category_Tier_3'] = worksheet.cell_value(curr_row, 35)
#incident['Closure_Product_Category_Tier1'] = worksheet.cell_value(curr_row, 36)
#incident['Closure_Product_Category_Tier2'] = worksheet.cell_value(curr_row, 37)
#incident['Closure_Product_Category_Tier3'] = worksheet.cell_value(curr_row, 38)

