import math
import matplotlib.pyplot as plt
import numpy as np

'''
We want to write an initial simple program where the user choose between calculate
the linear thermal expansion, the area thermal expansion or the volume thermal expansion
for an element. In this program, the user gives us the initial and final temperature, the coefficient
of thermal expansion of the element, and the initial length of the material. We then return the change
in length in the material at x temperature and total length of the material.
'''
LENGTH_METRICS = ['millimeter','mm','Centimetre', 'cm','decimeter','dm','meter','m','dekameter','dam','hectometer','hm','kilometer','km','myriameter','mym','miles', 'mi','yard','yd','feet','ft','inches','in']
TEMPERATURE_METRICS = ['Celsius', 'C', 'Fahrenheit', 'F', 'Kelvin', 'K']
VOLUME_METRICS = ['millileter','ml','centiliter','cl','deciliter','dl','liter','l','kiloliter','kl','cubic centimeter','cu cm','cc', 'decistere','ds', 'US Gallons (Liquid)', 'gal lqd', 'US Gallons (Dry)', 'gal dry','cubic feet', 'cu ft','cubic meter', 'm3', 'cubic inches', 'cu in', 'cubic yard', 'cu yd']
AREA_METRICS = ['sq centimeter','sq cm', 'centare', 'ca', 'sq metters','sq m', 'are','a', 'hectare','ha', 'sq kilometer','sq km', 'sq inches','sq in', 'sq feet','sq ft', 'sq yards','sq yd', 'acres','ac', 'sq miles','sq mi'] 

def length_metric_conversion(desire_metric,num,metric): #This function converts the value of num in a length unit metric to another unit metric
        length_metric = [] #We create an empty list for later stored the values of the conversion here
        #We are only going to work with the units in the dictionary metrics, where we stored the name and abbreviation of these units
        metrics = {'millimeter':'mm','Centimetre': 'cm','decimeter':'dm','meter':'m','dekameter':'dam','hectometer':'hm','kilometer':'km','myriameter':'mym','miles': 'mi','yard':'yd','feet':'ft','inches':'in'}
        #We are going to work with the metter unit as the standard for each unit, we assigned to each unit as key, its equivalent in metter as the pair value
        metrics_in_metters = {'millimeter':0.001,'Centimetre':0.01,'inches':0.025400,'decimeter':0.1,'feet':0.30480,'yard':0.91440,'meter':1,'dekameter':10, 'hectometer':100,'kilometer':1000,'myriameter':10000,'miles':1609.3445}
        if desire_metric.lower() not in metrics_in_metters: #Because the desire_metric or metric value could be the unit name or its abbreviation
        #And we only use one of these strings as key in the dict metrics_in_metters
        #We cannot access its pair value if the string is different to the key value, so in case this happens
        #We use if statements to verify if desire_metric or metric are in metrics_in_metters
            for key in metrics.keys(): #In case desire_metric or metric aren't in the dict with the values in metters, we use the for loop to check in metrics dict
                if metrics[key] == desire_metric.lower(): #We check if the value of the key in metrics is equal to the desire_metric or metric
                    desire_metric = key #And change the desire_metric or metric for the value that is a key in the dict metrics_in_metters
        if metric.lower() not in metrics_in_metters:
            for key in metrics.keys():
                if metrics[key] == metric.lower():
                    metric = key
        #Now we can access the pair value of the key in metrics_in_metters
        #When we want to convert from one unit metric to another, we need to check the standard values of these units and compare 
        if metrics_in_metters[desire_metric] > metrics_in_metters[metric]: #We use if and elif statements to compare if the values are greater or less
            num /= metrics_in_metters[desire_metric] #If we want to pass from a metric with an standard value that is less than the value of the metric we want to pass to
            #We divide the value of num by the standard value of the desire metric
            length_metric.append(desire_metric)
            length_metric.append(num) #We then add the new values to the empty list we created
            print('Lenght = '+str(num)+''+str(desire_metric)+'s') #Print the values for the user
        elif metrics_in_metters[desire_metric] < metrics_in_metters[metric]: #If we want to pass from a metric with an standard value that is greater than the value of the desire metric
            num *= metrics_in_metters[desire_metric] #We multiply the value of num by the standard value of the desire metric
            length_metric.append(desire_metric)
            length_metric.append(num) #We then add the new values to the empty list we created
            print('Lenght = '+str(num)+''+str(desire_metric)+'s') #Print the values for the user
        return length_metric #Return the new values to the main function

def area_metric_conversion(desire_metric,num,metric): #This function converts the value of num in a area unit metric to another unit metric
    area_metric = [] #We create an empty list for later stored the values of the conversion here
    #We are only going to work with the units in the dictionary metrics, where we stored the name and abbreviation of these units
    metrics = {'sq centimeter' : 'sq cm', 'centare' : 'ca', 'sq metters' : 'sq m', 'are' : 'a', 'hectare' : 'ha', 'sq kilometer' : 'sq km', 'sq inches' : 'sq in', 'sq feet' : 'sq ft', 'sq yards':'sq yd', 'acres' : 'ac', 'sq miles' :'sq mi'}
    #We are going to work with the square metter unit as the standard for each unit, we assigned to each unit as key, its equivalent in square metter as the pair value
    metrics_in_sqmetters = {'sq cm':0.0001, 'sq in':0.00065, 'sq ft':0.0929,'sq yd': 0.83613,'ca': 1, 'sq m': 1, 'a': 100,'ha':10000, 'sq km': 1000000, 'sq mi': 2589989.174, 'ac': 4046.863}
    if desire_metric.lower() not in metrics_in_sqmetters and desire_metric.lower() in metrics: #Because the desire_metric or metric value could be the unit name or its abbreviation
        #And we only use one of these strings as key in the dict metrics_in_sqmetters
        #We cannot access its pair value if the string is different to the key value, so in case this happens
        #We use if statements to verify if desire_metric or metric are in metrics_in_sqmetters
        for key in metrics.keys(): #In case desire_metric or metric aren't in the dict with the values in square metters, we use the for loop to check in metrics dict
            if metrics[key] == desire_metric:
                desire_metric = key #And change the desire_metric or metric for the value that is a key in the dict metrics_in_sqmetters
    if metric.lower() not in metrics_in_sqmetters and metric.lower() in metrics:
        for key in metrics.keys():
            if metrics[key] == desire_metric:
                desire_metric = key
    #When we want to convert from one unit metric to another, we need to check the standard values of these units and compare 
    if metrics_in_sqmetters[desire_metric] > metrics_in_sqmetters[metric]: #We use if and elif statements to compare if the values are greater or less
        num /= metrics_in_sqmetters[desire_metric] #If we want to pass from a metric with an standard value that is less than the value of the metric we want to pass to
        #We divide the value of num by the standard value of the desire metric
        area_metric.append(desire_metric) #We then add the new values to the empty list we created
        area_metric.append(num)
        print('Area = '+str(num)+''+str(desire_metric)+'s') #Print the values for the user
    elif metrics_in_sqmetters[desire_metric] < metrics_in_sqmetters[metric]: #If we want to pass from a metric with an standard value that is greater than the value of the desire metric
        num *= metrics_in_sqmetters[desire_metric] #We multiply the value of num by the standard value of the desire metric
        area_metric.append(desire_metric) 
        area_metric.append(num) #We then add the new values to the empty list we created
        print('Area = '+str(num)+''+str(desire_metric)+'s')  #Print the values for the user
    return area_metric #Return the new values to the main function

def volume_metric_conversion(desire_metric,num,metric): #This function converts the value of num in a volume unit metric to another unit metric
    volume_metric = [] #We create an empty list for later stored the values of the conversion here
    #We are only going to work with the units in the dictionary metrics, where we stored the name and abbreviation of these units
    metrics = {'millileter':'ml','centiliter':'cl','deciliter':'dl','liter':'l','kiloliter':'kl','cubic centimeter':'cu cm', 'cubic centimeter':'cc', 'decistere':'ds', 'US Gallons (Liquid)': 'gal lqd', 'US Gallons (Dry)': 'gal dry','cubic feet': 'cu ft','cubic meter': 'm3', 'cubic inches': 'cu in', 'cubic yard': 'cu yd'}
    #We are going to work with the cubic metter unit as the standard for each unit, we assigned to each unit as key, its equivalent in cubic metter as the pair value
    metrics_in_cmetters = {'ml':0.000001, 'cl':0.00001,'dl':0.0001, 'cu cm':0.000001, 'cc':0.000001,'cu ft': 0.02832, 'cu in': 0.000016387, 'cu yd':0.76456, 'm3': 1,'l': 0.001,'kl':1, 'ds':0.10, 'gal lqd':0.00379, 'gal dry': 0.0044}
    if desire_metric.lower() not in metrics_in_cmetters and desire_metric.lower() in metrics: #Because the desire_metric or metric value could be the unit name or its abbreviation
        for key in metrics.keys(): #And we only use one of these strings as key in the dict metrics_in_cmetters
            if metrics[key] == desire_metric: #We cannot access its pair value if the string is different to the key value, so in case this happens
                desire_metric = key #We use if statements to verify if desire_metric or metric are in metrics_in_cmetters
    if metric.lower() not in metrics_in_cmetters and metric.lower() in metrics: 
        for key in metrics.keys(): #In case desire_metric or metric aren't in the dict with the values in cubic metters, we use the for loop to check in metrics dict
            if metrics[key] == desire_metric: #And change the desire_metric or metric for the value that is a key in the dict metrics_in_cmetters
                desire_metric = key
    #When we want to convert from one unit metric to another, we need to check the standard values of these units and compare            
    if metrics_in_cmetters[desire_metric] > metrics_in_cmetters[metric]: #We use if and elif statements to compare if the values are greater or less
        num /= metrics_in_cmetters[desire_metric] #If we want to pass from a metric with an standard value that is less than the value of the metric we want to pass to
        #We divide the value of num by the standard value of the desire metric
        volume_metric.append(desire_metric) #We then add the new values to the empty list we created
        volume_metric.append(num)
        print('Volume = '+str(num)+''+str(desire_metric)+'s') #Print the values for the user to see
    elif metrics_in_cmetters[desire_metric] < metrics_in_cmetters[metric]: #If we want to pass from a metric with an standard value that is greater than the value of the desire metric
        num *= metrics_in_cmetters[desire_metric] #We multiply the value of num by the standard value of the desire metric
        volume_metric.append(desire_metric) #We then add the new values to the empty list we created
        volume_metric.append(num)
        print('Volume = '+str(num)+''+str(desire_metric)+'s') #Print the values for the user
    return volume_metric #Return the new values to the main function

def temperature_metric_conversion(desire_metric,num,metric): #This function converts the value of num in a temperature unit metric to another unit metric
    temperature_metric = []  #We create an empty list for later stored the values of the conversion here
    metrics = ['Celsius', 'C', 'Fahrenheit', 'F', 'Kelvin', 'K'] #We are only going to work with Celsius, Kelvin and Fahrenheit units
    #We use if statements to check the different possible cases in metrics for the desire_metric
    #And we use if elif statements to check the different possible cases in metrics for metric in each desire_metric possible case
    if desire_metric.lower() == 'celsius' or desire_metric.lower() == 'c':
        if metric == 'Fahrenheit' or metric == 'F': #If it is from Fahrenheit to Celsius
            num -= 32 #We use the equation (Fahrenheit - 32) / 1.8
            temperature_metric.append(desire_metric) #We add the values to the list temperature_metric 
            temperature_metric.append(num/1.8)
            print('Temperature =' + str(temperature_metric[1]) +str(temperature_metric[0])) #Print the new values for the user to see
        elif metric == 'Kelvin' or metric == 'K': #If it is from Kelvin to Celsius
            num -=273.15 #We use the equation Kelvin (num value) - 273.15
            temperature_metric.append(desire_metric) #We add the new values to the list temperature_metric
            temperature_metric.append(num)
            print('Temperature =' + str(temperature_metric[1]) +str(temperature_metric[0])) #Print the new values for the user to see
    if desire_metric == 'Fahrenheit' or desire_metric == 'F': #If we want to transform a value to its Fahrenheit value
        if metric == 'Celsius' or metric == 'C':#If it is from Celsius to Fahrenheit
            num *= 1.8 #We use the equation (Celsius * 1.8) + 32 
            temperature_metric.append(desire_metric)
            temperature_metric.append(num+32) #We add the new values to the list temperature_metric
            print('Temperature =' + str(temperature_metric[1]) +str(temperature_metric[0])) #Print the values for the user to see
        elif metric == 'Kelvin' or metric == 'K': #If it is from Kelvin to Fahrenheit
            num -= 273.15 #We use the equation  ((Kelvin - 273.15) * 1.8) + 32
            temperature_metric.append(desire_metric) #We add the new values to the list temperature_metric
            temperature_metric.append((num*1.8) + 32)
            print('Temperature =' + str(temperature_metric[1]) +str(temperature_metric[0])) #Print the values to the user
    if desire_metric == 'Kelvin' or desire_metric == 'K': #If we want to transform a value to its Kelvin value
        if metric == 'Celsius' or metric == 'C': #If it is from Celcius to Kelvin
            num += 273.15 #We use the equation Celsius (num value) + 273.15
            temperature_metric.append(desire_metric) #We add the new values to the list temperature_metric
            temperature_metric.append(num)
            print('Temperature =' + str(temperature_metric[1]) +str(temperature_metric[0])) #Print the values for the user to see
        elif metric == 'Fahrenheit' or metric == 'F': #If it is from Fahrenheit to Kelvin
            num -=32 #We use the equation ((Fahrenheit - 32) / 1.8) + 273.15
            temperature_metric.append(desire_metric)
            temperature_metric.append((num/1.8) + 273.15) #We add the new values to temperature_metric
            print('Temperature =' + str(temperature_metric[1]) +str(temperature_metric[0])) #Print the values for the user
    return temperature_metric #We return the value to the main function

def cte_metric_conversion(desire_metric,num,metric): #This function convert the cte value into the value with the unit metric needed
    cte_metric_conversed = []  #We create a empty list for later stored the values of the conversion here
    metrics = ['Celsius', 'C', 'Fahrenheit', 'F', 'Kelvin', 'K'] #We are only going to work with Celsius, Kelvin and Fahrenheit units
    #We use if statements to check the different possible cases in metrics for the desire_metric
    #And we use if elif statements to check the different possible cases in metrics for metric in each desire_metric possible case
    if desire_metric == 'Celsius' or desire_metric == 'C': #If we want to transform a value to its Celsius value
        if metric == 'Fahrenheit' or metric == 'F': #If it is from Fahrenheit to Celsius
            num *=1.8 #We multiply the value for an approximate value of 1.8
            cte_metric_conversed.append(desire_metric) #Then we add these values to the list cte_metric_conversed
            cte_metric_conversed.append(num)
            print('CTE =' + str(cte_metric_conversed[1]) +str(cte_metric_conversed[0])) #And print its value to the user
        elif metric == 'Kelvin' or metric == 'K': #If it is from Kelvin to Celsius
            num *=1 #We multiply the value by 1 since there's not change between these units
            cte_metric_conversed.append(desire_metric) #Then we add these values to the list cte_metric_conversed
            cte_metric_conversed.append(num)
            print('CTE =' + str(cte_metric_conversed[1]) +str(cte_metric_conversed[0]))
    if desire_metric == 'Fahrenheit' or desire_metric == 'F': #If we want to transform a value to its Fahrenheit value
        if metric == 'Celsius' or metric == 'C': #If it is from Celsius to Fahrenheit
            num /= 1.8 #We divide the value of num by 1.8
            cte_metric_conversed.append(desire_metric) #And add the new value to the list
            cte_metric_conversed.append(num)
            print('CTE =' + str(cte_metric_conversed[1]) +str(cte_metric_conversed[0])) #Print the value for the user
        elif metric == 'Kelvin' or metric == 'K': #If it is from Kelvin to Fahrenheit
            num /=1.8 #Again we divide the value of num by 1.8
            cte_metric_conversed.append(desire_metric) #add the new value to the list
            cte_metric_conversed.append(num)
            print('CTE =' + str(cte_metric_conversed[1]) +str(cte_metric_conversed[0])) #Print the value for the user
    if desire_metric == 'Kelvin' or desire_metric == 'K': #If we want to transform a value to its Kelvin value
        if metric == 'Celsius' or metric == 'C': #If it is from Celcius to Kelvin
            num *=1 #We multiply num value by 1, since there's not significant change between Celsius and Kelvin
            cte_metric_conversed.append(desire_metric) #Add the values to the list
            cte_metric_conversed.append(num)
            print('CTE =' + str(cte_metric_conversed[1]) +str(cte_metric_conversed[0])) #Print the values for the user
        elif metric == 'Fahrenheit' or metric == 'F': #If it is from Fahrenheit to Kelvin
            num *= 1.8 #We multiply num value for an approximate value of 1.8
            cte_metric_conversed.append(desire_metric) #add the new value to the list
            cte_metric_conversed.append(num)
            print('CTE =' + str(cte_metric_conversed[1]) +str(cte_metric_conversed[0])) #Print the value for the user
    return cte_metric_conversed #Return the values to the main function

print('Thermal Expansion Calculator')
print('Choose what kind of thermal expansion you wish to get between the following options: ')
print('a) Linear expansion') #We want the user to choose which operation we should do
print('b) Area expansion')
print('c) Volume expansion')
thermal_expansion = input('Enter an option: ') #The user must write the letter or the name of the thermal expansion
if thermal_expansion.lower() == 'a' or thermal_expansion.lower() == 'linear expansion' or thermal_expansion.lower() == 'linear':
    print('You have chosen linear thermal expansion')
    initial_length = float(input('Enter the initial length of the material in numbers: ')) #We ask for the initial length number
    initial_length_metric = input('Enter the unit metrics of the initial length of the material, eg. m if is meters, ft if is in feet: ')
    #We ask for the metric of that number
    if initial_length_metric.lower() not in LENGTH_METRICS:
        print('Invalid length metric. Please use one of the following: ' + ', '.join(LENGTH_METRICS))
        exit()
    desire_metric = input('Enter 1 if you wish to keep the result in the same metric, 2 if you wish another: ')
        #We ask the user if they want to keep that metric or want to transform it into another metric
    if desire_metric == '1':
        final_length_metric = initial_length_metric
    elif desire_metric == '2':
        final_length_metric = input('Enter the unit metrics you wish to have the result in, eg. m if is meters, ft if is in feet: ')
        if final_length_metric.lower() not in LENGTH_METRICS:
            print('Invalid length metric. Please use one of the following: ' + ', '.join(LENGTH_METRICS))
            exit()
        length = length_metric_conversion(final_length_metric, initial_length,initial_length_metric) #We call the length metric conversion function
        #Which will transform the initial length metric into the desired metric and return a list with the values
        initial_length = length[1] #We give the initial length its new value in the new metric, calling the value on the list stored on length
        initial_length_metric = final_length_metric #We could keep this or call the value on the index 0 of the list stored in length
    else:
        print('Invalid option. Please enter 1 or 2.')
        exit()   
    initial_temp = float(input('Enter the initial temperature: '))
    initial_temp_metric = input('Enter the unit metrics of the initial temperature, eg. C if is Celsius, F if is Fahrenheit: ')
    if initial_temp_metric.lower() not in TEMPERATURE_METRICS:
        print('Invalid temperature metric. Please use one of the following: ' + ', '.join(TEMPERATURE_METRICS))
        exit()
    final_temp = float(input('Enter the final temperature(it must be in the same metric of the initial temperature): '))
    desire_temperature_metric = input('Enter 1 if you desire to keep the result in the same metric, 2 if you wish another: ')
    #We ask the user if they want to keep the same metric or transform it into another
    if desire_temperature_metric == '1':
        final_temp_metric = initial_temp_metric
    elif desire_temperature_metric == '2':
        final_temp_metric = input('Enter the unit metrics you wish to have the result in, eg. C if is Celsius, F if is Fahrenheit: ')
        if final_temp_metric.lower() not in TEMPERATURE_METRICS:
            print('Invalid temperature metric. Please use one of the following: ' + ', '.join(TEMPERATURE_METRICS))
            exit()
        temperature = temperature_metric_conversion(final_temp_metric, initial_temp,initial_temp_metric) #We call the temperature metric conversion function
        initial_temperature = temperature[1]        #Which will transform the initial temperature metric into the desired metric and return a list with the values
        initial_temp = temperature[1] #We give the initial temperature its new value in the new metric, calling the value on the list stored on temperature
        initial_temp_metric = final_temp_metric #We could keep this or call the value on the index 0 of the list stored in temperature
        temperature_final = temperature_metric_conversion(final_temp_metric, final_temp, initial_temp_metric)
        final_temp = temperature_final[1]    
    else:
        print('Invalid option. Please enter 1 or 2.')
        exit()
    #We ask for the coefficient of linear thermal expansion
    coefficient = float(input('Enter the coefficient of linear thermal expansion: '))
    cte_metric = input('Enter the metric of the linear expansion coefficient: ') #Then we ask in what metric is the linear expansion coefficient
    if cte_metric.lower() not in TEMPERATURE_METRICS:
        print('Invalid temperature metric. Please use one of the following: ' + ', '.join(TEMPERATURE_METRICS))
        exit()
    cte = cte_metric_conversion(cte_metric, coefficient, initial_temp_metric) #We call the cte metric conversion function
    coefficient = cte[1] #We give the coefficient its new value in the new metric, calling the value on the list stored on cte  
    #We calculate the change in length and the total length
    change_in_length = coefficient * (final_temp - initial_temp) * initial_length
    total_length = initial_length + change_in_length
    
    print(f'The change in length is {change_in_length} and the total length is {total_length}')

elif thermal_expansion.lower() == 'b' or thermal_expansion.lower() == 'area expansion' or thermal_expansion.lower() == 'area':
    print('You have chosen area thermal expansion')
    initial_area = float(input('Enter the initial area of the material in numbers: ')) #We ask for the initial area number
    initial_area_metric = input('Enter the unit metrics of the initial area of the material, eg. m2 if is square meters, ft2 if is in square feet: ')
    #We ask for the metric of that number
    if initial_area_metric.lower() not in AREA_METRICS:
        print('Invalid area metric. Please use one of the following: ' + ', '.join(AREA_METRICS))
        exit()
    desire_metric = input('Enter 1 if you wish to keep the result in the same metric, 2 if you wish another: ')
    #We ask the user if they want to keep that metric or want to transform it into another metric   
    # We use if statements to check the different possible cases in metrics for the desire_metric
    if desire_metric == '1':
        final_area_metric = initial_area_metric
    elif desire_metric == '2':
        final_area_metric = input('Enter the unit metrics you wish to have the result in, eg. m2 if is square meters, ft2 if is in square feet: ')
        if final_area_metric.lower() not in AREA_METRICS:
            print('Invalid area metric. Please use one of the following: ' + ', '.join(AREA_METRICS))
            exit()
        area = area_metric_conversion(final_area_metric, initial_area,initial_area_metric) #We call the area metric conversion function
        #Which will transform the initial area metric into the desired metric and return a list with the values             
        # We give the initial area its new value in the new metric, calling the value on the list stored on area
        initial_area = area[1]
        initial_area_metric = final_area_metric
    else:
        print('Invalid option. Please enter 1 or 2.')
        exit()  
    initial_temp = float(input('Enter the initial temperature: '))
    initial_temp_metric = input('Enter the unit metrics of the initial temperature, eg. C if is Celsius, F if is Fahrenheit: ') 
    if initial_temp_metric.lower() not in TEMPERATURE_METRICS:
        print('Invalid temperature metric. Please use one of the following: ' + ', '.join(TEMPERATURE_METRICS))
        exit()
    final_temp = float(input('Enter the final temperature(it must be in the same metric of the initial temperature): '))
    desire_temperature_metric = input('Enter 1 if you desire to keep the result in the same metric, 2 if you wish another: ')       
    #We ask the user if they want to keep the same metric or transform it into another
    if desire_temperature_metric == '1':
        final_temp_metric = initial_temp_metric
    elif desire_temperature_metric == '2':
        final_temp_metric = input('Enter the unit metrics you wish to have the result in, eg. C if is Celsius, F if is Fahrenheit: ')
        if final_temp_metric.lower() not in TEMPERATURE_METRICS:
            print('Invalid temperature metric. Please use one of the following: ' + ', '.join(TEMPERATURE_METRICS))
            exit()
        temperature = temperature_metric_conversion(final_temp_metric, initial_temp,initial_temp_metric) 
        #We call the temperature metric conversion function
        #Which will transform the initial temperature metric into the desired metric and return a list with the values
        # We give the initial temperature its new value in the new metric, calling the value on the list stored on temperature
        initial_temp = temperature[1]
        initial_temp_metric = final_temp_metric
        temperature_final = temperature_metric_conversion(final_temp_metric, final_temp, initial_temp_metric)           
        final_temp = temperature_final[1]
    else:
        print('Invalid option. Please enter 1 or 2.')
        exit()  
    #We ask for the coefficient of area thermal expansion
    coefficient = float(input('Enter the coefficient of area thermal expansion: '))
    cte_metric = input('Enter the metric of the area expansion coefficient: ')
    #Then we ask in what metric is the area expansion coefficient
    if cte_metric.lower() not in TEMPERATURE_METRICS:
        print('Invalid temperature metric. Please use one of the following: ' + ', '.join(TEMPERATURE_METRICS))
        exit()
    cte = cte_metric_conversion(cte_metric, coefficient, initial_temp_metric)
    #We call the cte metric conversion function
    coefficient = cte[1]
    #We give the coefficient its new value in the new metric, calling the value on the list stored on cte
    #We calculate the change in area and the total area
    change_in_area = (coefficient*2) * (final_temp - initial_temp) * initial_area   
    total_area = initial_area + change_in_area
    print(f'The change in area is {change_in_area} and the total area is {total_area}')

elif thermal_expansion.lower() == 'c' or thermal_expansion.lower() == 'volume expansion' or thermal_expansion.lower() == 'volume':
    print('You have chosen volume thermal expansion')
    initial_volume = float(input('Enter the initial volume of the material in numbers: ')) #We ask for the initial volume number
    initial_volume_metric = input('Enter the unit metrics of the initial volume of the material, eg. m3 if is cubic meters, ft3 if is in cubic feet: ') 
    #We ask for the metric of that number
    if initial_volume_metric.lower() not in VOLUME_METRICS:
        print('Invalid volume metric. Please use one of the following: ' + ', '.join(VOLUME_METRICS))
        exit()
    desire_metric = input('Enter 1 if you wish to keep the result in the same metric, 2 if you wish another: ')
    #We ask the user if they want to keep that metric or want to transform it into another metric
    if desire_metric == '1':
        final_volume_metric = initial_volume_metric
    elif desire_metric == '2':
        final_volume_metric = input('Enter the unit metrics you wish to have the result in, eg. m3 if is cubic meters, ft3 if is in cubic feet: ')
        if final_volume_metric.lower() not in VOLUME_METRICS:
            print('Invalid volume metric. Please use one of the following: ' + ', '.join(VOLUME_METRICS))
            exit()
        volume = volume_metric_conversion(final_volume_metric, initial_volume,initial_volume_metric)
        #We call the volume metric conversion function
        #Which will transform the initial volume metric into the desired metric and return a list with the values
        #We give the initial volume its new value in the new metric, calling the value on the list stored on volume
        initial_volume = volume[1]
        initial_volume_metric = final_volume_metric
    else:
        print('Invalid option. Please enter 1 or 2.')
        exit()  
    initial_temp = float(input('Enter the initial temperature: '))
    initial_temp_metric = input('Enter the unit metrics of the initial temperature, eg. C if is Celsius, F if is Fahrenheit: ') 
    if initial_temp_metric.lower() not in TEMPERATURE_METRICS:
        print('Invalid temperature metric. Please use one of the following: ' + ', '.join(TEMPERATURE_METRICS))
        exit()
    final_temp = float(input('Enter the final temperature(it must be in the same metric of the initial temperature): '))
    desire_temperature_metric = input('Enter 1 if you desire to keep the result in the same metric, 2 if you wish another: ')
    #We ask the user if they want to keep the same metric or transform it into another
    if desire_temperature_metric == '1':
        final_temp_metric = initial_temp_metric
    elif desire_temperature_metric == '2':
        final_temp_metric = input('Enter the unit metrics you wish to have the result in, eg. C if is Celsius, F if is Fahrenheit: ')
        if final_temp_metric.lower() not in TEMPERATURE_METRICS:
            print('Invalid temperature metric. Please use one of the following: ' + ', '.join(TEMPERATURE_METRICS))
            exit()
        temperature = temperature_metric_conversion(final_temp_metric, initial_temp,initial_temp_metric)
        #We call the temperature metric conversion function
        #Which will transform the initial temperature metric into the desired metric and return a list with the values
        #We give the initial temperature its new value in the new metric, calling the value on the list stored on temperature
        initial_temp = temperature[1]
        initial_temp_metric = final_temp_metric
        temperature_final = temperature_metric_conversion(final_temp_metric, final_temp, initial_temp_metric)
        final_temp = temperature_final[1]
    else:
        print('Invalid option. Please enter 1 or 2.')
        exit()  
    #We ask for the coefficient of volume thermal expansion
    coefficient = float(input('Enter the coefficient of volume thermal expansion: '))
    cte_metric = input('Enter the metric of the volume expansion coefficient: ')
    #Then we ask in what metric is the volume expansion coefficient
    if cte_metric.lower() not in TEMPERATURE_METRICS:
        print('Invalid temperature metric. Please use one of the following: ' + ', '.join(TEMPERATURE_METRICS))
        exit()
    cte = cte_metric_conversion(cte_metric, coefficient, initial_temp_metric)
    #We call the cte metric conversion function
    coefficient = cte[1]
    #We give the coefficient its new value in the new metric, calling the value on the list stored on cte
    #We calculate the change in volume and the total volume
    change_in_volume = (coefficient*3) * (final_temp - initial_temp) * initial_volume
    total_volume = initial_volume + change_in_volume
    print(f'The change in volume is {change_in_volume} and the total volume is {total_volume}')
else:
    print('Invalid option. Please enter a, b or c.')
    exit()
# This is a thermal expansion calculator that allows the user to calculate the change in length, area, or volume of a material due to temperature changes.
# It includes functions for converting between different metric units for length, area, volume, temperature, and coefficient of thermal expansion (CTE).
# It prompts the user to input the initial and final temperatures, the initial length/area/volume, and the coefficient of thermal expansion.
# The calculator then computes the change in length, area, or volume based on the provided inputs and displays the results. 
# The code also includes error handling for invalid metric inputs and ensures that the user can convert between different units as needed.
# This is a thermal expansion calculator that allows the user to calculate the change in length, area, or volume of a material due to temperature changes.
# It includes functions for converting between different metric units for length, area, volume, temperature, and coefficient of thermal expansion (CTE).
# It prompts the user to input the initial and final temperatures, the initial length/area/volume, and the coefficient of thermal expansion.
# The calculator then computes the change in length, area, or volume based on the provided inputs and displays the results.
# The code also includes error handling for invalid metric inputs and ensures that the user can convert between different units as needed.