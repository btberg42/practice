import sys

def fizzbuzz(max):
    print "FizzBuzz 1 to %d" % max
    for x in range (1,max):
        str = ""
        if x % 3 == 0:
            str = "%s%s" % (str,"Fizz")
        if x % 5 == 0:
            str = "%s%s" % (str,"Buzz")
        
        if str != "":
            print str
        else:
            print x

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for x in range (1, len(sys.argv)):
            max = int(sys.argv[x])
            if max > 1:
                fizzbuzz(max)
    else:
        fizzbuzz(100)
