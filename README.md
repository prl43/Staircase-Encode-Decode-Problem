# Staircase-Encode-Decode-Problem
The task involves creating a function named decode(message_file) that can process a text file containing encoded messages. Each line of the file has a number followed by a word. The function decodes a hidden message by constructing a "pyramid" structure from the numbers, where the numbers increase consecutively by line, starting from 1 at the top. The message is revealed by concatenating the words that correspond to the last number in each line of the pyramid. The function is expected to ignore all other words that do not align with the pyramid structure. The result should be a decoded message returned as a string.

For example, given an input file with the following content:
3 love
6 computers
2 dogs
4 cats
1 I
5 you

The pyramid structure would be:
1
2 3
4 5 6

The words at the end of each pyramid line (I, love, computers) form the hidden message. The function should return the string "I love computers".
