winner = ["Leo", "Sam", "Frankie"]
# Loop through the list using enumerate to get both index and value
for index, person in enumerate(winner):
    # enumerate function is used to simultaneously iterate over 
    # both the index and the corresponding value of each element.
    
    # Print the index, incremented by 1 (to start from 1), and the person's name
    print("{} - {}".format(index+1, person))   
    