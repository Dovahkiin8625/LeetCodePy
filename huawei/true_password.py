import sys
passwds = input().strip().split()

rst = ''
for p in passwds:
  if all([p[:j] in passwds for j in range(1,len(p))]) and (len(p)>len(rst) or (len(p)==len(rst) and p>rst)):
    rst = p
print(rst)
    