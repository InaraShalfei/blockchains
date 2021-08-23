with open('demo.txt', mode='r') as file:
    #file.write('Hello from Python!\n')


    #user_input = input('Please enter the data: \n')
    #file.write(user_input)

    file_content = file.readlines()
    #print(file_content)

    print(file_content)

    for line in file_content:
        print(line[:-1])

    print(file.readline())
    #file.close()
print('Done!')
