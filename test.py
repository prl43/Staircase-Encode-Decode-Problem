# Plugging in each letter individually is unnecessary. 
# If only needing the numbers from the end of each line in the staircase,
# I won't use the overly expansive testing of searching for each number,
# putting it in the right order of the staircase, and then decoding.
# for memory constraints, I won't store every value as well.


# The last number in the series for each line can be represented as number = step(step+1)/2
# using this, solved for number, only caring about the positive side, 
# step = (sqrt(8*number+1)-1)/2 if evenly divided out, it's at the end.

# import libraries
from math import sqrt

# initialize variables
file_path  = 'coding_qual_input.txt'
max_number_segment = 0
word_pair = {}
word_pair[-1] = '[Word Not Found]'

# loop over text file
with open(file_path, 'r') as file:
    for line in file:
        # split the line into number and word
        number_str, word = line.strip().split()
        
        # convert number part to an integer
        number = int(number_str)

        # assign value:word in dictionary if an end of segment number
        is_end_of_segment = False
        is_end_of_segment = ( ( sqrt(8 * number + 1) - 1 ) % 2 == 0 )

        if is_end_of_segment:
            # store max number segment
            number_segment = int(( sqrt(8 * number + 1) - 1 ) / 2)
            if max_number_segment < number_segment:
                max_number_segment = number_segment
        
            word_pair[number_segment] = word

## for loop from 1 to max number's segment 
for number_segment in range(1, max_number_segment):
    if number_segment in word_pair:
        print( word_pair[number_segment], end=' ' )
    else:
        # print word pair not found
        print( word_pair[-1], end=' ' )



