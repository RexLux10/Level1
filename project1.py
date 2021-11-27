# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 18:02:58 2021
@author: RexLux10

project01: 
1st option - code to det. what you have made if you know all grades
           - "what will I get in class, A, B, C, etc." 
2nd option - code to det. what you have to get in final exam to get get final grade
           - "what do I need to make in the final to get an A, B, C, etc."
           
Example of option 1:
how many graded assignments are there?: 2   #homeword, final exam
what is percent weight for assignment 1: 40 #homework is worht 40 percent
what is percent weight for assignment 2: 60 #final exam is worth 60 percent
what is your grade for assignment 1: 80     #average on all homeworks
what is your grade for assignment 1: 75     #average on all homeworks

output: you got a C =  77.0 

"""

#%% imports needed
import numpy as np #needed for matrix manipulation

#%% user input     - final grade or what to make on final exam?
response = int(input("do you want to know final grade (1) or what you have to make for final grade (2) "))

#%% the 1st option - det. what you have made if you know all grades
if response == 1:  
    
    #inputing how many assignments and weight of each.
    gradeAssignments = int(input("how many grade assignments are there? ")) 
    
    gradeWeights = [0] * gradeAssignments       
    x1 = range(0,gradeAssignments)

    for n in x1:
        gradeWeights[n] = float(input("what is percent weight for assignment %d: " % (n + 1)))
    
    if sum(gradeWeights) == 100:
        #inputing the grade of each assignment
        gradeWeightLength = len(gradeWeights)
        x2 = range(0,gradeWeightLength)

        gradeReceived = [0] * gradeAssignments

        for n in x2:
           gradeReceived[n] = float(input("what is your grade for assignment %d: " % (n + 1)))
       
        #determining the final grade
        gradeReceived= np.transpose(gradeReceived) / 100
        summation = np.average(gradeWeights*gradeReceived) * gradeAssignments

        if summation < 60:
            print("you got an F = ",summation,".")
        elif summation < 70:
            print("you got a D = ",summation,".")
        elif summation < 80:
            print("you got a C = ",summation,".")
        elif summation < 90:
            print("you got a B = ",summation,".")
        elif summation <= 100:
            print("you got an A = ",summation,".")
        else:
            print("you got above a 100?? - how is this possible??")
            
    else:
        print("warning: the amounts has to add up to 100")        
   
#%% the 2nd option - det. what you have to get in final exam to get get final grade
elif response == 2:
    print("second option")
    gradeAssignments = int(input("how many grade assignments are there? (put final exam last) "))
        
    gradeWeights = [0] * gradeAssignments       
    x1 = range(0,gradeAssignments)

    for n in x1:
        gradeWeights[n] = float(input("what is percent weight for assignment %d: " % (n + 1)))
                
    if sum(gradeWeights) == 100:
        #inputing the grade of each assignment
        gradeWeightLength = len(gradeWeights)
        x2 = range(0,gradeWeightLength)

        gradeReceived = [0] * gradeAssignments

        for n in x2:
           gradeReceived[n] = float(input("what is your grade for assignment %d: " % (n + 1)))
           if (n + 1) == gradeWeightLength - 1:
                break
            
        gradeNeeded = float(input("what grade would you like on course? "))    
        gradeReceived= np.transpose(gradeReceived) / 100
        sumOut100 = np.average(gradeWeights*gradeReceived) * gradeAssignments    
        
        gradeOnFinal = (gradeNeeded - (sumOut100)) / gradeWeights[-1] * 100
        print("")
        print("need to make this on final exam: ", gradeOnFinal)
        print("to get the final grade desired of: ", gradeNeeded)
    
    else:
        print("warning: the amounts has to add up to 100")      
    

#%% the 3rd option - give "error" option
else:
    print("error")