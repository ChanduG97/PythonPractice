l=['x',20,"y",10,"z",30]
cnt = 0
st = ""
inc=0
for c in range (1,6,2):
    cnt += c
    st = st+l[c-1]+"@"
    inc +=l[c]
print(cnt,inc,st)