from input_gen_dftb import *

num1 = dftb_geom()
num2 = dftb_driver_cg()
print (num1.geom())
print (num2.cg())
