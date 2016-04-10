print "True and True = True [%r]" % (True and  True)
print "False and True = False [%r]" % (False and True)
print "1 == 1 and 2 == 1 False [%r]" % (1 == 1 and 2 == 1)
print "\"test\" == \"test\" = True [%r]" % ("test" == "test")
print "1 == 1 or 2 != 1 = True [%r]" % (1 == 1 or 2 != 1)
print "True and 1 == 1 = True [%r]" % (True and 1 == 1)
print "False and 0 != 0 = False [%r]" % (False and 0 != 0)
print "True or 1 == 1 = True [%r]" % (True or 1 == 1)
print "\"test\" == \"testing\" = False [%r]" % ("test" == "testing")
print "1 != 0 and 2 == 1 = False [%r]" % (1 != 0 and 2 == 1)
print "\"test\" != \"testing\" = True [%r]" % ("test" != "testing")
print "\"test\" != 1 = True [%r]" % ("test" !=  1)
print "not (True and False) = True [%r]" % (not (True and False))
print "not (1 == 1 and 0 != 1) = False [%r]" % (not (1 == 1 and 0 != 1))
print "not (10 == 1 or 1000 == 1000) = False [%r]" % (not (10 == 1 or 1000 == 1000))
print "not (1 != 10 or 3 == 4) = False [%r]" % (not (1 != 10 or 3 == 4))
print "not (\"testing\" == \"testing\" and \"Zed\" == \"Cool Guy\") = True [%r]" % (not ("testing" == "testing" and "Jesse" == "Cool Guy"))
print "1 == 1 and (not (\"testing\" == 1 or 1 == 0)) = True [%r]" % (1 == 1 and (not ("testing" == 1 or 1 == 0)))
print "\"chunk\" == \"bacon\" and (not (3 == 4 or 3 == 3)) = False [%r]" % ("chunky" == "bacon" and (not (3 == 4 or 3 == 3)))
print "3 == 3 and (not (\"testing\" == \"testing\" or \"Python\" == \"Fun\")) = False [%r]" % (3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")))




