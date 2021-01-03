from tkinter import * 
  
  
root = Tk() 

# defining the callback function (observer) 
def my_callback(var, indx, mode): 
    print ("Traced variable {}".format(my_var.get())) 
  
my_var = StringVar() 
  
  
# registering the observer 
my_var.trace_add('write', print) 
  
Label(root, textvariable = my_var).pack(padx = 5, pady = 5) 
  
Entry(root, textvariable = my_var).pack(padx = 5, pady = 5) 
  
root.mainloop() 
