import os
os.makedirs('intancias/',exist_ok =True)
arch= open("intancias/test.txt","w")
arch.write("{0} {1}".format("hello","World"))
arch.close()