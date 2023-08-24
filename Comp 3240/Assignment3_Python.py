# Jack Bianca
# Comp 3240 - Programming Assignment 3
# 4/3/23
# 
class PA3_Python(object):
   
   '''
   # Multiplies matrix 1 by matrix 2
   '''
   def matrix_mult(mat1, mat2):
      mat3 = [[0,0],[0,0]]
      for i in range(len(mat1)):
         for j in range(len(mat2[0])):
            for k in range(len(mat2)):
               mat3[i][j] += mat1[i][k] * mat2[k][j]
      return mat3
   '''
   # Create the transition matrix from the given observation points
   '''
   def calc_transition_matrix(observation_string):
      observeLength = len(observation_string)
      DD = 0
      RR = 0
      DR = 0
      RD = 0
      RTotal = 0
      DTotal = 0
      #for every char in string, checks which counter to increment
      for i in range(observeLength-1):
         if observation_string[i] == 'R':
            if observation_string[i+1] == 'R':
               RR += 1
               RTotal += 1
            else:
               RD += 1
               RTotal += 1
         else:
            if observation_string[i+1] == 'D':
               DD += 1
               DTotal += 1
            else:
               DR += 1
               DTotal += 1
      #creates transition matrix using counters
      transMatrix = [[DD/DTotal, RD/RTotal], [DR/DTotal, RR/RTotal]]
      #curr_weather = []
      #if observation_string[0] == 'D':
         #curr_weather = [[1],[0]]
      #else:
         #curr_weather = [[0],[1]]
      return transMatrix
   '''
   # Generates the forecast for the next 7 days given the transition matrix and
   the current weather
   # The forecast should be a 2x7 matrix where each row is a forecast for a day
   '''
   def generate_forecast(transition_matrix, curr_weather):
      #creates next transition matrix
      newMatrix = transition_matrix
      forecast = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
      print(curr_weather)
      #for every exponent, updates forecast with result
      for i in range(7):
         forecast[i] = PA3_Python.matrix_mult(newMatrix, curr_weather)
         #square transition matrix
         newMatrix = PA3_Python.matrix_mult(transition_matrix, newMatrix)
         print(newMatrix)
      #return forecast
      print(forecast)
      #throw invalid observations string for forecast
      return forecast
   '''
   # Generates the climate prediction (i.e., steady state vector) given the
   transition matrix, current
   # weather, and precision
   '''
   def generate_climate_prediction(transition_matrix, curr_weather, precision):
   #climate prediction with desired precision
   #take delta from day 1 and day 2, until its less than precision
   #newMatrix = transition_matrix
   #prevDay = forecast[i-1]
   #currDay = forecast[i]
   #delta = currDay - prevDay
   #throw an invalid precision exception
   #for i in range(forecast):
   #   if delta <= precision
   #     return i
      pass
   '''
   # Print the forecasted weather predictions
   '''
   def print_predictions(forecast):
      # Print first line
      print(f'[{forecast[0]},')
      # Print middle 5 lines
      for i in range(1, len(forecast) - 1):
         print(f' {forecast[i]},')
      # Print the last line
      print(f' {forecast[6]}]')
   '''
   # Print the steady state vector containing the climate prediction
   '''
   def print_steady_state(steady_state):
      print(steady_state[0])
      print(steady_state[1])
      
observation_string = input("input an observation string: ")
precision = input("enter a precision: ")

transition_matrix = PA3_Python.calc_transition_matrix(observation_string)
print("Transition Matrix: ")
print(transition_matrix)

curr_weather = [[1],[0]]
print("Weather Forecast: ")
forecast = PA3_Python.generate_forecast(transition_matrix, curr_weather)
#print(PA3_Python.print_predicitons(forecast))

#steady_state = PA3_Python.generate_climate_prediction(transition_matrix,
#   curr_weather, precision)
#print("Steady State Vector: ")
#PA3_Python.print_steady_state(steady_state)
#observation = 'RRRRDDDDDRDRD'
#precision = 0.01