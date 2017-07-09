from functools import *

ponctuation = set("，　。\"：\n. -《》、,；'？")
un2345 = "一二三四五"

filenames = ["第" + n + "章.txt" for n in un2345]
files = [open(fn, "r", encoding = "utf-8") for fn in filenames]


ss = [f.read() for f in files]
for f in files:
    f.close()
    
tout = "".join(ss)
toutl = sorted([(i, tout.count(i)) for i in set(tout)], key = lambda t: -t[1])
print(len(tout), len(toutl))

sets = [set(s) - ponctuation for s in ss]
lens = [len(t) for t in sets]
print(lens)

ls = [[(i, s.count(i)) for i in set(s) - ponctuation] for s in ss]
ls = [sorted(l, key = lambda t: -t[1]) for l in ls]

filenames = ["caractères" + c + ".txt" for c in un2345]

gs = [open(fn, "w", encoding = "utf-8") for fn in filenames]
outs = [[("\n" if i%10==0 else " ") + l[i][0]+ str(l[i][1]).rjust(4) for i in range(len(l))] for l in ls]
strs = ["".join(l) for l in outs]

zs = zip(gs, strs)       
for z in zs:
        z[0].write(z[1])
        z[0].close()

def fait(filename):
    f = open(filename, "r", encoding = "utf-8")
    s = f.read()
    f.close()
    
    e = set(s) - ponctuation
    l = [(car, s.count(car)) for car in e]
    l = sorted(l, key = lambda x: -x[1])
    
    out = ""
    for i in range(len(l)):
        out = out + ("\n" if i%10==0 else " ") + l[i][0] + str(l[i][1]).rjust(4)

    f= open(filename[0:-4] + "字" + ".txt", "w", encoding = "utf-8")
    f.write("nombre de caractères: " + str(len(s)) + "\n")
    f.write("caractères différents: " + str(len(e)) + "\n")
    f.write(out)
    f.close

def faitsans(filename):
    f = open(filename, "r", encoding = "utf-8")
    s = f.read()
    f.close()
    
    e = set(s) - ponctuation
    
    out = ""
    for car in e:
        out = out + car + " "

    f= open(filename[0:-4] + "字sans" + ".txt", "w", encoding = "utf-8")
    f.write("caractères différents: " + str(len(e)) + "\n")
    f.write(out)
    f.close
