#def outer():
#    def inner():
#        res = 4 * 5
#        return res
#    return inner()


#f = outer()
#print(f)

#def outer():
 #   def inner(x):
  #      res = 4 * x
   #     return res
    #return inner

#f = outer()
#func = f(5)
#print(func)

#def outer():     # this is closure
 #   x = 5
  #  def inner():
   #     res = 4 * x
    #    return res
   # return inner()

#f = outer()
#print(f)

def outer(x):
    def inner():
        res = 4 * x
        return res
    return inner()

f = outer(5)
print(f)