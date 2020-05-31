#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# Author: Joon Lee
# Date Created: May 30th, 2020
# Editor: Jexy Liew
###############################################################################
# When doing the Python modules, please do the problem on your own
#   before looking at the answer key. Feel free to use web (Stack Exchange
#   is a reliable source) or reach out to the project manager; Essentially,
#   the goal of these modules are to give you a small goal to help understand
#   Python by doing your personal research on something specific.
###############################################################################

# Swap the values of the two variables
v1 = "God is good."
v2 = "All the time."
print("\nIntially, we have the phrase:\n", v1, v2)
print("We will now swap the variables.")

# We want you to swap variables v1 and v2 such that the text
#   prints the following:
# "Now, the phrase is:
#  All the time. Good is good,"

# Write your answer below:
temp = v1 # Create a temporary variable to store v1
v1 = v2 # Change the value of v1 to that of v2
v2 = temp # Change the v2 temp, which had the original v1
print("Now, the phrase is:\n", v1, v2)
print()
