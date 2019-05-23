import multiprocessing.dummy as mp 

items = [0]*10

def do_print(i):
    print(i)
    items[i] = i*2+1

p=mp.Pool(4)
p.map(do_print, range(0,10)) # range(0,1000) if you want to replicate your example
p.close()
p.join()
print(items)