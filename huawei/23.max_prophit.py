n_ = int(input().strip())
d_ = int(input().strip())
it_ =[int(i) for i in input().strip().split()]
itp_ = []
for i in range(n_):
    itp_.append([int(j) for j in input().strip().split()])
    
rst = 0
for i in range(n_):
    m_ = 0
    for j in range(d_-1):
        m_ += max(0,itp_[i][j+1]-itp_[i][j])
    rst += m_*it_[i]
print(rst)