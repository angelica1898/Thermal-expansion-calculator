import math

'''
We want to write an initial simple program where the user choose between calculate
the linear thermal expansion, the area thermal expansion or the volume thermal expansion
for an element. In this program, the user gives us the initial and final temperature, the coefficient
of thermal expansion of the element, and the initial length of the material. We then return the change
in length in the material at x temperature and total length of the material.
'''
LENGTH_METRICS = ['millimeter','mm','centimetre', 'cm','decimeter','dm','meter','m','dekameter','dam','hectometer','hm','kilometer','km','myriameter','mym','miles', 'mi','yard','yd','feet','ft','inches','in']
TEMPERATURE_METRICS = ['Celsius', 'C', 'Fahrenheit', 'F', 'Kelvin', 'K','celsius','fahrenheit','kelvin']
VOLUME_METRICS = ['millileter','ml','centiliter','cl','deciliter','dl','liter','l','kiloliter','kl','cubic centimeter','cu cm','cc', 'decistere','ds', 'US Gallons (Liquid)', 'gal lqd', 'US Gallons (Dry)', 'gal dry','cubic feet', 'cu ft','cubic meter', 'm3', 'cubic inches', 'cu in', 'cubic yard', 'cu yd']
AREA_METRICS = ['sq centimeter','sq cm', 'centare', 'ca', 'sq metters','sq m', 'are','a', 'hectare','ha', 'sq kilometer','sq km', 'sq inches','sq in', 'sq feet','sq ft', 'sq yards','sq yd', 'acres','ac', 'sq miles','sq mi'] 

def main():
    print('Thermal Expansion Calculator')
    print('Choose what kind of thermal expansion you wish to get between the following options: ')
    print('a) Linear expansion') #We want the user to choose which operation we should do
    print('b) Area expansion')
    print('c) Volume expansion')
    thermal_expansion = input('Enter an option: ') #The user must write the letter or the name of the thermal expansion
    if thermal_expansion.lower() == 'a' or thermal_expansion.lower() == 'linear expansion' or thermal_expansion.lower() == 'linear' :
        print('You have chosen linear thermal expansion')
        initial_length = float(input('Enter the initial length of the material in numbers: ')) 
        #We ask for the initial length number
        initial_length_metric = input('Enter the unit metrics of the initial length of the material, eg. m if is meters, ft if is in feet: ')
        #We ask for the metric of that number
        if initial_length_metric.lower() not in LENGTH_METRICS: #To avoid errors or make the program too broad
            print('') #We use only an amount of all the unit metrics possible stored on the list LENGTH_METRICS
            print('Value not valid') #If the value of the input initial_length_metric isn't valid
            print('Try again between the following length metrics: ') #We ask the user to input a metric between the ones contained on the list
            print(LENGTH_METRICS)
            initial_length_metric = input('Enter the metrics of the initial length: ')
        desire_metric = input('Enter 1 if you wish to keep the result in the same metric, 2 if you wish another: ')
        #We ask the user if they want to keep that metric or want to transform it into another metric
        if desire_metric == '2':
            desire_il_metric = input('Enter the unit metrics you wish to have the result in: ') #If the user wants another metric, we ask them which one they want
            if desire_il_metric.lower() not in LENGTH_METRICS: #Again, in case the metric isn't in the list LENGTH_METRICS
                print('') #We ask the user to input one that is on the list
                print('Value not valid')
                print('Try again between the following values: ')
                print(LENGTH_METRICS)
                desire_il_metric = input('Which metric do you desire? ')
            length = length_metric_conversion(desire_il_metric, initial_length,initial_length_metric) #We call the length metric conversion function
            #Which will transform the initial length metric into the desired metric and return a list with the values
            initial_length = length[1] #We give the initial length its new value in the new metric, calling the value on the list stored on length
            initial_length_metric = desire_il_metric #We could keep this or call the value on the index 0 of the list stored in length
        elif desire_metric != '1' or desire_metric != '2':
            print('Invalid option. Please enter 1 or 2.')
            desire_metric = input('')
            if desire_metric == '2':
                desire_il_metric = input('Enter the unit metrics you wish to have the result in: ') #If the user wants another metric, we ask them which one they want
                if desire_il_metric.lower() not in LENGTH_METRICS: #Again, in case the metric isn't in the list LENGTH_METRICS
                    print('') #We ask the user to input one that is on the list
                    print('Value not valid')
                    print('Try again between the following values: ')
                    print(LENGTH_METRICS)
                    desire_il_metric = input('Which metric do you desire? ')
                length = length_metric_conversion(desire_il_metric, initial_length,initial_length_metric) #We call the length metric conversion function
                #Which will transform the initial length metric into the desired metric and return a list with the values
                initial_length = length[1] #We give the initial length its new value in the new metric, calling the value on the list stored on length
                initial_length_metric = desire_il_metric #We could keep this or call the value on the index 0 of the list stored in length
        initial_temperature = float(input('Enter the initial temperature in numbers: ')) #We ask for the numeric value of temperature
        initial_temperature_metric = input('Enter the metrics of the initial temperature, eg. C if is Celsius, F if is Fahrenheit: ')
        #We ask for the metric of that value, if it is celcius, Fahrenheit or Kelvin
        if initial_temperature_metric not in TEMPERATURE_METRICS: #There's more unit metrics for temperature, but we only use the three more used
            print('') #In case the user inputs one that isn't one of these three, stored on TEMPERATURE_METRICS list
            print('Value not valid') #We ask the user to input a metric between Celsius, Fahrenheit and Kelvin
            print('Try again between the following values: ')
            print(TEMPERATURE_METRICS)
            initial_temperature_metric = input('Enter the metrics of the initial temperature: ')
        final_temperature = float(input('Enter the final temperature in numbers (it must be in the same metric of the initial temperature): '))
        #We ask for the numeric value of the final temperature, and the user must be sure the value correspond to the same metric of the initial temperature
        desire_temperature_metric = input('Enter 1 if you desire to keep the result in the same metric, 2 if you wish another: ')
        #We ask the user if they want to keep the same metric or transform it into another
        if desire_temperature_metric == '2':
            desire_it_metric = input('Enter the unit metrics you wish to have the result in: ') #We ask the user which metric desires
            if desire_it_metric not in TEMPERATURE_METRICS: #Again, in case the user input a value that isn't in TEMPERATURE_METRICS
                print('') #We ask them to input a value between Celsius, Kelvin or Fahrenheit
                print('Value not valid')
                print('Try again between the following values: ')
                print(TEMPERATURE_METRICS)
                desire_it_metric = input('Which metric do you desire? ')
            temperature = temperature_metric_conversion(desire_it_metric, initial_temperature,initial_temperature_metric)
            #We call the temperature metric conversion function
            initial_temperature = temperature[1] #Which will transform the initial temperature metric into the desired metric and return a list with the values
            #We give the initial temperature its new value in the new metric, calling the value on the list stored on temperature
            temperature_final = temperature_metric_conversion(desire_it_metric, final_temperature, initial_temperature_metric)
            final_temperature = temperature_final[1]
        linear_expansion_coefficient = float(input('Enter the number of the linear expansion coefficient of the element: '))
        #We ask for the numeric value of the linear expansion coefficient
        cte_metric = input('Enter the metric of the linear expansion coefficient: ') #Then we ask in what metric is the linear expansion coefficient
        if cte_metric not in TEMPERATURE_METRICS: #Like we did with the temperature metric, if isn't on TEMPERATURE_METRICS list
            print('') #We ask the user to input one between Celsius, Kelvin or Fahrenheit
            print('Value not valid') #The value of the coefficient must be on one of these three units or the calculation won't be accurate
            print('Try again between the following values: ')
            print(TEMPERATURE_METRICS)
            cte_metric = input('Enter the metric of the linear expansion coefficient: ')
        #We ask if that value is in celsius, Fahrenheit or Kelvin
        #The coefficient of thermal expansion, or linear expansion coefficient, must be on the same metric than the temperature of the element
        #In case that metric differs from the temperature metric, we call the temperature metric conversion function to equal the metrics
        if cte_metric != initial_temperature_metric and desire_temperature_metric == '1': #If the user wants to keep the same unit metrics for temperature
            cte = cte_metric_conversion(initial_temperature_metric,linear_expansion_coefficient,cte_metric) #But it differs from the CTE metrics
            #We convert the cte value into the same unit metric of the temperature of the element
            linear_expansion_coefficient = cte[1] #We give the new value to the linear_expansion_coefficient
        elif desire_temperature_metric =='2' and cte_metric != desire_it_metric: #Again, if the user changes the metrics of the initial and final temperature
            cte = cte_metric_conversion(desire_it_metric,linear_expansion_coefficient,cte_metric) #And it differs from the CTE metrics
            linear_expansion_coefficient = cte[1] #We convert the cte value to the new metric and give a new value to the linear expansion coefficient
        value = linear_expansion(initial_length,initial_temperature,final_temperature,linear_expansion_coefficient)
        #Finally we call the linear expansion function to calculate the thermal expansion
        print('Length change is', value[0], initial_length_metric) #We give the user the value of the change in length
        print('Final length is', value[1], initial_length_metric) #And the final length value

    elif thermal_expansion == 'b' or thermal_expansion == 'Area expansion':
        initial_area = float(input('Enter the initial area in numbers: '))#We ask for the initial area number
        initial_area_metric = input('Enter the metrics of the initial area, eg. sq m if it is square meters, sq ft if it is square feet: ')
        #We ask for the metric of that value
        if initial_area_metric not in AREA_METRICS: #To avoid errors or make the program too broad
            print('') #We use only an amount of all the unit metrics possible stored on the list AREA_METRICS
            print('Value not valid') #If the value of the input initial_area_metrics isn't valid
            print('Try again between the following values: ')  #We ask the user to input a metric between the ones contained on the list
            print(AREA_METRICS)
            initial_area_metric = input('Enter the metrics of the initial area: ')
        desire_metric = input('Enter 1 if you desire to keep the result in the same metric, 2 if you wish another: ')
        #If the user wants another metric, we ask them which one they want.
        if desire_metric == '2':
            desire_ia_metric = input('Which metric do you desire: ')
            if desire_ia_metric not in AREA_METRICS:#Again, in case the metric isn't in the list LENGTH_METRICS
                print('') #We ask the user to input one that is on the list.
                print('Value not valid')
                print('Try again between the following values: ')
                print(AREA_METRICS)
                desire_ia_metric = input('Which metric do you desire? ')
            area = area_metric_conversion(desire_ia_metric, initial_area,initial_area_metric) #We call the conversion function that returns a list
            initial_area = area[1] #We give initial_area the new value according to its new unit metrics
            initial_area_metric = desire_ia_metric
        elif desire_metric != '1' or desire_metric != '2':
            print('Invalid option. Please enter 1 or 2.')
            desire_metric = input('')
            if desire_metric == '2':
                desire_ia_metric = input('Enter the unit metrics you wish to have the result in: ') #If the user wants another metric, we ask them which one they want
                if desire_ia_metric.lower() not in AREA_METRICS: #Again, in case the metric isn't in the list AREA_METRICS
                    print('') #We ask the user to input one that is on the list
                    print('Value not valid')
                    print('Try again between the following values: ')
                    print(AREA_METRICS)
                    desire_ia_metric = input('Which metric do you desire? ')
                area = area_metric_conversion(desire_ia_metric,initial_area,initial_area_metric) #We call the area metric conversion function
                #Which will transform the initial area metric into the desired metric and return a list with the values
                initial_area = area[1] #We give the initial area its new value in the new metric, calling the value on the list stored on area
                initial_area_metric = desire_ia_metric #We could keep this or call the value on the index 0 of the list stored in area
        initial_temperature = float(input('Enter the initial temperature in numbers: ')) 
        initial_temperature_metric = input('Enter the metrics of the initial temperature, eg. C if is Celsius, F if is Fahrenheit: ')
        #We ask for the initial and final temperature and their metric
        if initial_temperature_metric not in TEMPERATURE_METRICS:
            print('') #We make sure if the given metric is correct or not
            print('Value not valid')
            print('Try again between the following values: ')
            print(TEMPERATURE_METRICS)
            initial_temperature_metric = input('Enter the metrics of the initial temperature: ')
        final_temperature = float(input('Enter the final temperature in numbers (it must be in the same metric of the initial temperature)'))
        #We ask the user if they want to keep the same metric or transform it into another
        desire_temperature_metric = input('Enter 1 if you desire to keep the result in the same metric, 2 if you wish another: ')
        if desire_temperature_metric == '2':
            desire_it_metric= input('Which metric do you desire: ')
            if desire_it_metric not in TEMPERATURE_METRICS:
                print('')
                print('Value not valid')
                print('Try again between the following values: ')
                print(TEMPERATURE_METRICS)
                desire_it_metric = input('Which metric do you desire? ')
            #We call the temperature metric conversion function
            #Which will transform the initial temperature metric into the desired metric and return a list with the values
            #We give the initial temperature its new value in the new metric, calling the value on the list stored on temperature
            temperature = temperature_metric_conversion(desire_it_metric, initial_temperature,initial_temperature_metric)
            initial_temperature = temperature[1]
            temperature_final = temperature_metric_conversion(desire_it_metric, final_temperature, initial_temperature_metric)
            final_temperature = temperature_final[1]
        #We ask for the coefficient of linear thermal expansion
        linear_expansion_coefficient = float(input('Enter the number of the linear expansion coefficient of the element: '))
        #Then we ask in what metric is the linear expansion coefficient
        cte_metric = input('Enter the metric of the linear expansion coefficient: ')
        if cte_metric not in TEMPERATURE_METRICS:#If cte_metric doesn't correspond to a value in TEMPERATURE_METRICS
            print('') #We ask the user to input a value that is on the list
            print('Value not valid')
            print('Try again between the following values: ')
            print(TEMPERATURE_METRICS)
            cte_metric = input('Enter the metric of the linear expansion coefficient: ')
        #The CTE must be on the same metric of the initial and final temperatures, in case it isn't:
        if cte_metric != initial_temperature_metric and desire_temperature_metric == '1':
            cte = cte_metric_conversion(initial_temperature_metric,linear_expansion_coefficient,cte_metric)
            #We call the cte metric conversion function
            linear_expansion_coefficient = cte[1] 
            #We give the coefficient its new value in the new metric, calling the value on the list stored on cte
        elif desire_temperature_metric =='2' and cte_metric != desire_it_metric:
            cte = cte_metric_conversion(desire_it_metric,linear_expansion_coefficient,cte_metric)
            linear_expansion_coefficient = cte[1]
        value = area_expansion(initial_area,initial_temperature,final_temperature,linear_expansion_coefficient)
        #We call the area_expansion function to calculate the area thermal expansion that returns a value stored on a list
        print('Area change is', value[0], initial_area_metric) #We print those values
        print('Final area is',value[1],initial_area_metric)

    elif thermal_expansion == 'c' or thermal_expansion == 'Volume expansion':
        initial_volume = float(input('Enter the initial volume in numbers: ')) #We ask for the initial volume number
        initial_volume_metric = input('Enter the metrics of the initial volume, eg. m if is meters, ft if is in feet: ')
        #We ask for the metric of that number
        if initial_volume_metric not in VOLUME_METRICS:
            print('')
            print('Value not valid')
            print('Try again between the following values: ')
            print(VOLUME_METRICS)
            initial_volume_metric= input('Enter the metrics of the initial length: ')
        desire_metric = input('Enter 1 if you desire to keep the result in the same metric, 2 if you wish another: ')
        #We ask the user if they want to keep that metric or want to transform it into another metric
        if desire_metric == '2':
            desire_iv_metric = input('Which metric do you desire? ')
            if desire_iv_metric not in VOLUME_METRICS: #If the value isn't valid because it isn't contained on VOLUME METRICS
                print('') #We ask the user again to input a value from the list
                print('Value not valid')
                print('Try again between the following values: ')
                print(VOLUME_METRICS)
                desire_iv_metric = input('Which metric do you desire? ')
            #We call the volume metric conversion function
            #Which will transform the initial volume metric into the desired metric and return a list with the values
            #We give the initial volume its new value in the new metric, calling the value on the list stored on volume
            volume = volume_metric_conversion(desire_iv_metric, initial_volume, initial_volume_metric)
            initial_volume = volume[1]
            initial_volume_metric = desire_iv_metric
        elif desire_metric != '1' or desire_metric != '2':
            print('Invalid option. Please enter 1 or 2.')
            desire_metric = input('')
            if desire_metric == '2':
                desire_iv_metric = input('Enter the unit metrics you wish to have the result in: ') #If the user wants another metric, we ask them which one they want
                if desire_iv_metric.lower() not in VOLUME_METRICS: #Again, in case the metric isn't in the list VOLUME METRICS
                    print('') #We ask the user to input one that is on the list
                    print('Value not valid')
                    print('Try again between the following values: ')
                    print(VOLUME_METRICS)
                    desire_il_metric = input('Which metric do you desire? ')
                volume = volume_metric_conversion(desire_iv_metric,initial_volume,initial_volume_metric) #We call the volume metric conversion function
                #Which will transform the initial volume metric into the desired metric and return a list with the values
                initial_volume = volume[1] #We give the initial volume its new value in the new metric, calling the value on the list stored on volume
                initial_volume_metric = desire_iv_metric #We could keep this or call the value on the index 0 of the list stored in volume
        #We ask for the initial and final temperature, and their metric
        initial_temperature = float(input('Enter the initial temperature in numbers: '))
        initial_temperature_metric = input('Enter the metrics of the initial temperature, eg. C if is Celsius, F if is Fahrenheit: ')
        final_temperature = float(input('Enter the final temperature in numbers (it must be in the same metric of the initial temperature)'))
        desire_temperature_metric = input('Enter 1 if you desire to keep the result in the same metric, 2 if you wish another: ')
        #We ask the user if they want to keep the same metric or transform it into another
        if desire_temperature_metric == '2':
            desire_it_metric= input('Which metric do you desire? ')
            if desire_it_metric not in TEMPERATURE_METRICS:
                print('')
                print('Value not valid')
                print('Try again between the following values: ')
                print(TEMPERATURE_METRICS)
                desire_it_metric = input('Which metric do you desire? ')
            #We call the temperature metric conversion function
            #Which will transform the initial temperature metric into the desired metric and return a list with the values
            #We give the initial temperature its new value in the new metric, calling the value on the list stored on temperature
            temperature = temperature_metric_conversion(desire_it_metric, initial_temperature, initial_temperature_metric)
            initial_temperature = temperature[1]
            temperature_final = temperature_metric_conversion(desire_it_metric, final_temperature,initial_temperature_metric)
            final_temperature = temperature_final[1]
        #We ask for the coefficient of linear thermal expansion
        linear_expansion_coefficient = float(input('Enter the number of the linear expansion coefficient of the element: '))
        cte_metric = input('Enter the metric of the linear expansion coefficient: ')
        #Then we ask in what metric is the linear expansion coefficient
        if cte_metric not in TEMPERATURE_METRICS:  #If cte_metric doesn't correspond to a value in TEMPERATURE_METRICS
            print('') #We ask the user to input a value that is on the list
            print('Value not valid')
            print('Try again between the following values: ')
            print(TEMPERATURE_METRICS)
            cte_metric = input('Enter the metric of the linear expansion coefficient: ')
        if cte_metric != initial_temperature_metric and desire_temperature_metric == '1': 
            #The CTE must be on the same metric of the initial and final temperatures, in case it isn't:
            cte = cte_metric_conversion(initial_temperature_metric,linear_expansion_coefficient,cte_metric) #We call the cte metric conversion function
            linear_expansion_coefficient = cte[1] #We give the coefficient its new value in the new metric, calling the value on the list stored on cte
        elif desire_temperature_metric =='2' and cte_metric != desire_it_metric:
            cte = cte_metric_conversion(desire_it_metric,linear_expansion_coefficient,cte_metric) #We call the cte metric conversion function
            linear_expansion_coefficient = cte[1] #We give the coefficient its new value in the new metric, calling the value on the list stored on cte
        value = volume_expansion(initial_volume,initial_temperature,final_temperature,linear_expansion_coefficient)
        print('Volume change is ', value[0], initial_volume_metric)
        print('Final volume is', value[1], initial_volume_metric)
    else:
        print('')
        print("˙◠˙")
        print('Sorry for not being able to help you.')
    print('')
    print('See you soon!') 

def length_metric_conversion(desire_metric,num,metric): #This function converts the value of num in a length unit metric to another unit metric
    length_metric = [] #We create an empty list for later stored the values of the conversion here
    #We are only going to work with the units in the dictionary metrics, where we stored the name and abbreviation of these units
    metrics = {'millimeter':'mm','centimetre': 'cm','decimeter':'dm','meter':'m','dekameter':'dam','hectometer':'hm','kilometer':'km','myriameter':'mym','miles': 'mi','yard':'yd','feet':'ft','inches':'in'}
    #We are going to work with the metter unit as the standard for each unit, we assigned to each unit as key, its equivalent in metter as the pair value
    metrics_in_metters = {'millimeter':0.001,'Centimetre':0.01,'inches':0.025400,'decimeter':0.1,'feet':0.30480,'yard':0.91440,'meter':1,'dekameter':10, 'hectometer':100,'kilometer':1000,'myriameter':10000,'miles':1609.3445}
    if desire_metric.lower() not in metrics_in_metters: #Because the desire_metric or metric value could be the unit name or its abbreviation
        #And we only use one of these strings as key in the dict metrics_in_metters
        #We cannot access its pair value if the string is different to the key value, so in case this happens
        #We use if statements to verify if desire_metric or metric are in metrics_in_metters
        for key in metrics.keys(): #In case desire_metric or metric aren't in the dict with the values in metters, we use the for loop to check in metrics dict
            if metrics[key] == desire_metric.lower():
                desire_metric = key #And change the desire_metric or metric for the value that is a key in the dict metrics_in_metters
    if metric.lower() not in metrics_in_metters:
        for key in metrics.keys():
            if metrics[key] == metric.lower():
                metric = key
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
    if desire_metric == 'Celsius' or desire_metric == 'C': #If we want to transform a value to its Celsius value
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


def linear_expansion(length,temperature1, temperature2, linear_expansion_coefficient): #This function calculates the linear thermal expansion
    linear_te = [] #We create a list to later return the results to the main function
    longitude_change = linear_expansion_coefficient * length * (temperature2 - temperature1) #we use the area thermal expansion equation
    #And calculate the change in length at x temperature
    final_longitude = length + longitude_change #Finally we add the change in length to the element's longitude to know its final length
    linear_te.append(longitude_change) #We add these values to the list linear_te
    linear_te.append(final_longitude) 
    return linear_te #Return to the main function the values stored on the list

def area_expansion(area, temperature1, temperature2, linear_expansion_coefficient): #This function calculates the area thermal expansion
    area_te = [] #We create a list to later return the results to the main function
    area_expansion_coefficient = linear_expansion_coefficient * 2 #The area expansion coefficient is two times the linear expansion coefficient
    area_change = area * area_expansion_coefficient * (temperature2 - temperature1) #Then we use the area thermal expansion equation
    #And calculate the change in area at x temperature
    total_area = area + area_change #Finally we add the change in area to the element's area, to know its final area
    area_te.append(area_change) #We add these values to the list area_te
    area_te.append(total_area)
    return area_te #Return to the main function the values stored on the list

def volume_expansion(volume, temperature1, temperature2, linear_expansion_coefficient): #This function calculates the volume thermal expansion
    volume_te = [] #We create a list to return the results to the main function
    volume_expansion_coefficient = linear_expansion_coefficient * 3 #Some elements like liquids or gases have their volume expansion coefficient
    #But because we want to make an extandard code, we'll use the linear coefficient for the volume expansion, multiplying its value by 3
    volume_change = volume_expansion_coefficient * volume * (temperature2 - temperature1) #Then we use the volume thermal expansion equation
    #And calculate the change in volume at x temperature
    final_volume = volume + volume_change #Finally we add the change in volume to the volume of the element, to know its final volume
    volume_te.append(volume_change) #We add these values to the list volume_te
    volume_te.append(final_volume) 
    return volume_te #Return to the main function the values stored on the list
    

if __name__ == "__main__":
    main()