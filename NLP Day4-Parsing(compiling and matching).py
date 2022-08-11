#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re

#knowledge in today's course:
#re.compile()
#re.match()
#re.group(0)

# characters are defined
character_1 = "Dorothy"
character_2 = "Henry"

# .compile() a regular expression object named regular_expression that will match any 7 character string of word characters.
regular_expression=re.compile("[A-Za-z]{7}")

# Use regular_expression‘s .match() method to check if the regex matches the string stored in character_1. Save the result to result_1 and print it.
result_1=regular_expression.match(character_1)
#or .match("Dorothy")
print("result_1 is ==> ",result_1)



# store and print the matched text here:Access the match in result_1 using its .group() method with an argument of 0. Save the result to match_1 and print it.
match_1=result_1.group(0)
print("match_1 is ==> ",match_1)


# compile a regular expression to match a 7 character string of word characters and check for a match to character_2 here:In one line, use re‘s .match() method to compile a regular expression that will match any string of characters of length 7 and check if the regex matches the string stored in character_2. Save the result to result_2 and print it. Was a match found?
#Answer:No
#not compile(["A-Za-z{7}"])
result_2=(re.compile("[A-Za-z]{7}")).match(character_2)
print("result_2 is ==> ",result_2)

