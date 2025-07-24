from readData import readDataFromExcel
from cleandata import clean_employee_data
from writeData import writeData
from employeeController import save_employee_data_to_db


source_file = "EmployeeData.xlsx"
destination_file = "cleaned_data.xlsx"

def main():
    print("Reading Row data")
    raw_data = readDataFromExcel(source_file)

    print("Cleaning data")
    cleaned_data, employee_list = clean_employee_data(raw_data)

    print("Writing data")
    writeData(destination_file, employee_list)

    print("Saving data to Database")
    save_employee_data_to_db(employee_list)

    print("Employee data cleaned Excel and inserted to database successfully")

if __name__ == '__main__':
    main()