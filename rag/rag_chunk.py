import os

target = "rawdata.txt" if os.path.exists("rawdata.txt") else os.path.join(os.path.dirname(__file__), "rawdata.txt")
with open(target, "r", encoding="utf-8") as f:
    x=f.read().split()

z=350
q=1
for i in range(0,len(x),350):
    filename=f"chunk_{q}.txt"
    with open(filename,"w",encoding="utf-8") as f_out:
        f_out.write(" ".join(x[i:z]))
    z+=350
    q+=1
  


