def add_job():

    job = input('Enter job: ')
    file = open('jobs.txt', 'a+') 
    try:  
        if file:
            file.write(job +'\n')
    finally:
        file.close()

def view_file():
    with open('jobs.txt', 'r+') as file:
         lines = file.readlines()
         print("Jobs in the file: \n")
         for i in range(len(lines)):
             print(lines[i])
    return lines

def delete_file():
    array = []
    print('Choose job to delete: \n' )
    lines = view_file()
    # print(lines)
    delete_job = input('Enter job to delete: ')
    for i in range(len(lines)):
        if delete_job + '\n' != lines[i]:
            array.append(lines[i])
    with open('jobs.txt', 'w+') as file:
        file.writelines(array)




while (True):
    print('1 - Add in file\n2 - Delete from file\n3 - View file\n0 - Exit')
    operation = int(input('Enter operation: '))
    match operation:
        case 0:
            break

        case 1:
            add_job()

        case 2:
            delete_file()


        case 3:
            view_file()


            
        case _:
            print('Invalid symbols')
