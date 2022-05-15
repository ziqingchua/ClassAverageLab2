"""
input: the test scores
initiate a iterator (counter) and accumulator (sum) and set it to zero 
loop through the list scores 
add all the test scores
increment the counter by one 
once the loop ends, there are no more scores to add
divide the accumulator (sum) by counter 
display the output to the user
output: print the average of the class score
"""

"""
scores
iterator, accumulator = 0 
loop through scores
  accumulator = accumulator + scores
  iterator = iterator + 1 
average = accumulator / total score
print average
"""

def calculate_average (scores):
    iterator = 0 
    accumulator = 0 
    student_count = len(scores)
    while iterator < len(scores):
        accumulator = accumulator + scores[iterator]
        iterator = iterator + 1
    average = accumulator / student_count
    return average 

output = calculate_average(
    [50, 0, 100, 80, 90, 70, 50, 95, 60, 90, 50, 100, 70, 90])
print ("The average of total scores in  the class is: ", output)