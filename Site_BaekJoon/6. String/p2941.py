A = input()
B = 0
if "dz=" in A:
    B = B + A.count("dz=")
if "c=" in A:
    B = B + A.count("c=")
if "c-" in A:
    B = B + A.count("c-")
if "z=" in A:
    B = B + A.count("z=")
if "d-" in A:
    B = B + A.count("d-")
if "lj" in A:
    B = B + A.count("lj")
if "nj" in A:
    B = B + A.count("nj")
if "s=" in A:
    B = B + A.count("s=")


C = len(A) - B
print(C)