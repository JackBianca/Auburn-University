from Evaluator import evaluate

# Notes on how to use evaluator():
# Call the evaluator with evaluate(<premise>, **<variable_dict>). "premise"
# is a single string defining the premise or conclusion to test. "variable_dict" will unpack
# named variables. The easiest way to go about this is to create a dictionary with the 
# variable as the key and True/False as the value. Remember to unpack the dictionary
# by adding '**' before the dictionary variable in the function call.

# The only valid operators for premise strings are '^' (and), 'V' (or--CAPITAL v), '~' (not),
# and '>' (implies), and you can use parentheses to override the order of operations as usual.
# All variables should be lowercase letters and each should only be one character long. Finally,
# do not include spaces in the string.

# For example, if you want to test the premise 'p implies q or not r', you should use 'p>qV~r' as
# your premise string.

class Validator(object):
    # All of the logic to complete this assignment should be written in this function
    # This method accepts two things: An array of strings called premiseList and a 
    # single string called conclusion. These strings should be formatted according to 
    # the structure definded above. Also, this needs to return a boolean variable: true if
    # the argument form is valid, and false if it is not valid.
    def validate(self, premise_list, conclusion):
        pass