# this is a project that takes in the users current vertical jump, and the weight they intend to looses then it
# calculates their future vertical jump.

jump = int(input("current vertical jump (in inches):")) # this prints a statement that asks for the user for their
# current vertical jump and stores it as "jump".
lb_lost = int(input("weight lost (in lbs):")) # this prints a statement that asks for the user for their current
# weight and stores it as "lb_lost".
answer = (jump * lb_lost * 0.005) # this creates the calculations for the answer of the inches gained.
print("you will be able to jump", answer, "inches higher after you lose", lb_lost,
      "lbs, you then will have a vertical jump of", (jump + answer), "inches")
