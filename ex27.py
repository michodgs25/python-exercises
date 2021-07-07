# Logic

# TRUTH TERMS
# Python has the following - Characters and phrases for determining if something is "True" or "False".
# Logic on a computer is all about seeing if some combination of these Characters and Variables is True at some point in the program.

# and

# or

# not

# != NOT EQUAL

# == EQUAL

# >= GREATER-THAN-EQUAL

# <= LESS-THAN-EQUAL

# True

#  False

###################### TABLES

##                      NOT      | True?
##                     -------------------
#                      not False | True
#                      not True  | False


#                      OR            | True?
#                      ----------------------
#                      True or False  | True
#                      True or True   | True
#                      False or True  | True
#                      False or False | False


#                      And             | True?
#                      ------------------------
#                      False and False | False
#                      True and False  | False
#                      True and True   | True
#                      False and True  | False


#                      Not And             | True?
#                     ----------------------------
#                     not(True and False)  | True
#                     not(False and True)  | True
#                     not(True and False)  | True
#                     not(True and True)   | False


#                      Not Or              | True?
#                     -----------------------------
#                     not(True or False)   | False
#                     not(False or False)  | True
#                     not(True and True)   | False
#                     not(False and True)  | False


#                         !=            | True?
#                     -----------------------------
#                              1 != 0   | True
#                              1 != 1   | False
#                              0 != 1   | True
#                              0 != 0   | False


#                         ==            | True?
#                     -----------------------------
#                              1 == 0   | False
#                              1 == 1   | True
#                              0 == 0   | True
#                              0 == 1   | False
