def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count  # %r - raw data; %s - string; %d - number
    print "You have %d boxes of crackers" % boxes_of_crackers
    print "Man that's enough for the party!"
    print "Get a blanket.\n"


print "We can give the function #s directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
cheese_count = 10
amount_of_crackers = 50

cheese_and_crackers(cheese_count, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10+20, 5+6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(cheese_count + 100, amount_of_crackers + 1000)