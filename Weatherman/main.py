def pretty_print(list1,list2):
     print('Year'+ '\t' + 'Max Temperature' + '\t' + 'Min Temperature' + '\t' + 'Max Humidity' + '\t' + 'Min Humidity' )

     i=0
     while i<len(list1):
          print(str(list1[i][0]) + '\t' + str(list1[i][1]) + '\t' + str(list1[i][2]) + '\t' + str(list1[i][3]) + '\t' + str(list1[i][4]))
          i=i+1

     print('Year' + '\t' + 'Date' + '\t' + 'Temperature')
     j = 0
     while j < len(list2):
          print(str(list2[j][0]) + '\t' + str(list2[j][1]) + '\t' + str(list2[j][2]))
          j = j + 1

     return

def build_table1(dictionary):
     tyear = t1_row_dictionary['Year']

     if tyear > 0:
          t1_result_list.append([t1_row_dictionary['Year'], t1_row_dictionary['Max Temperature'], t1_row_dictionary['Min Temperature'],
                t1_row_dictionary['Max Humidity'], t1_row_dictionary['Min Humidity']])


def build_table2(dictionary):
     tyear = t2_row_dictionary['Year']

     if tyear > 0:
          t2_result_list.append([t2_row_dictionary['Year'], t2_row_dictionary['Date'], t2_row_dictionary['Temperature']])

def t1_new_row(year,dictionary):                                                   #resets dictionary
     dictionary['Year'] = year

     dictionary['Max Temperature'] = 0
     dictionary['Min Temperature'] = 1000000
     dictionary['Max Humidity'] = 0
     dictionary['Min Humidity'] = 1000000

     return dictionary


def t2_new_row(year, dictionary):  # resets dictionary

     dictionary['Year'] = year

     dictionary['Date'] = ''
     dictionary['Temperature'] = 0


     return dictionary


def t1_compare(list1, month_dictionary):

     index = 2
     readable_lines = len(list1) - 1

     while index < readable_lines:                                                   # reading lines in each file

          data_list = list1[index].split(',')

          # for Max Temperature
          try:
               max_temp = int(data_list[1])
          except ValueError as e:
               max_temp = 0

          if max_temp > month_dictionary['Max Temperature']:
               month_dictionary['Max Temperature'] = max_temp


          # for Min Temperature
          try:
               min_temp = int(data_list[3])
          except ValueError as e:
               min_temp = 0

          if min_temp < month_dictionary['Min Temperature']:
               month_dictionary['Min Temperature'] = min_temp


          # for Max Humidity
          try:
               max_hum = int(data_list[7])
          except ValueError as e:
               max_hum = 0

          if max_hum > month_dictionary['Max Humidity']:
               month_dictionary['Max Humidity'] = max_hum

          # for Min Humnidity
          try:
               min_hum = int(data_list[9])
          except ValueError as e:
               min_hum = 0

          if min_hum < month_dictionary['Min Humidity']:
               month_dictionary['Min Humidity'] = min_hum


          index=index+1

     return month_dictionary

def t2_compare(list1, month_dictionary):

     index = 2
     readable_lines = len(list1) - 1

     while index < readable_lines:                                                   # reading lines in each file

          data_list = list1[index].split(',')

          # for Mean Temperature
          try:
               mean_temp = int(data_list[2])
          except ValueError as e:
               mean_temp = 0

          #check highest mean temperature
          if mean_temp > month_dictionary['Temperature']:
               month_dictionary['Temperature'] = mean_temp
               month_dictionary['Date'] = str(data_list[0])

          index=index+1

     return month_dictionary


import os

#first table
t1_row_dictionary = {'Year' : 0 , 'Max Temperature' : 0, 'Min Temperature' : 100 , 'Max Humidity' : 0, 'Min Humidity' : 100}
t1_result_list = []

#second table
t2_row_dictionary = {'Year' : 0 , 'Date' : '', 'Temperature' : 0 }
t2_result_list = []



#user input
report_num = input("Enter report number: ")
path_name = input("Enter the path of weather data directory: ")


directory = os.path.join(path_name)                                                 #get directory

list_of_files = os.listdir(directory)                                               #list of all file names

no_of_files = len(list_of_files)                                                    #no. of files in directory


x=0
while x<no_of_files:                                                                      #this loop will read all files in the dir one by one

     filepath = directory + "/" + list_of_files[x]

     File = open(filepath)                                                                #File open and read
     lines_list = File.readlines()

     year = lines_list[2][:4]


     if year != t1_row_dictionary['Year']:                                                 #not same year

          #for table 1
          build_table1(t1_row_dictionary)
          t1_row_dictionary = t1_new_row(year,t1_row_dictionary)                   #reset
          t1_row_dictionary = t1_compare(lines_list,t1_row_dictionary)

          #for table 2
          build_table2(t2_result_list)
          t2_row_dictionary = t2_new_row(year,t2_row_dictionary)
          t2_row_dictionary = t2_compare(lines_list,t2_row_dictionary)

     else:
          t1_row_dictionary = t1_compare(lines_list,t1_row_dictionary)
          t2_row_dictionary = t2_compare(lines_list,t2_row_dictionary)


     x=x+1

build_table1(t1_row_dictionary)
build_table2(t2_row_dictionary)

pretty_print(t1_result_list,t2_result_list)

exit
