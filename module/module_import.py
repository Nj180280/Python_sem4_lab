import module_create 
import imp
module_create.myfunc() 
imp.reload(module_create) 
module_create.meth2()
print(dir(module_create))