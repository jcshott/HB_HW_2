
def produce_summary(filename, day):
    #day = 1
    the_file = open(filename)
    print "Day %d" % day
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]
            
        print "Delivered %s %ss for total of $%s" % (count, melon, amount)
    the_file.close()
    day = day =+ 1

produce_summary("um-deliveries-20140519.txt", 1)
produce_summary("um-deliveries-20140520.txt", 2)
produce_summary("um-deliveries-20140521.txt", 3)

"""
    print "Day 2"
    the_file = open("um-deliveries-20140520.txt")
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]
            
        print "Delivered %s %ss for total of $%s" % (count, melon, amount)
    the_file.close()


    print "Day 3"
    the_file = open("um-deliveries-20140521.txt")
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]
            
        print "Delivered %s %ss for total of $%s" % (count, melon, amount)
    the_file.close()
    """
