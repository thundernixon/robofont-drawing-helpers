f= CurrentFont()
selection = f.selection

for g in selection:
    # print(f[g].unicodes)
    f[g].unicode = None
    # print(f[g].unicodes)