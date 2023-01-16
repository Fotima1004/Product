my_File = input("Enter file name: ")
print("Available operation: ")
file_Opp = (['Add', 'Remove', 'Change', "Sum"])
print(file_Opp)
operation = input("Input operation: ")

with open(my_File, "r") as f:
    f.read()
    f.close()
    if operation == 'Add':
        with open(my_File, 'a') as f:
            newItem = input("New Item: ")
            f.write("\n" + newItem)
            f.close
    elif operation == 'Change':
        with open(my_File, 'r') as f:
            old_data = f.read()
            itemOld = input("Old item: ")
            itemNew = input("New item: ")
            new_data = old_data.replace(itemOld, itemNew)
            with open(my_File, 'w') as f:
                f.write(new_data)
                f.close()
    elif operation == 'Remove': 
        with open(my_File, 'w') as f:
            f.write('')
            f.close()
    elif operation == 'Sum':
        f = open(my_File, 'r')
        total_count = sum(int(x) for x in f if x.strip().isdigit()) 
        print(total_count)

new_File = open(my_File, 'r')
result = new_File.read()
new_File.close()
print(result)
