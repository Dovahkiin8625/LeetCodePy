
def test_sorted_methods():
    a = [1,5,3,2,4]
    print(a,sorted(a, reverse=True))
    b = (1,5,3,2,4)
    print(b,sorted(b, reverse=True))
    c = {1,5,3,2,4}
    print(c,sorted(c, reverse=True))
    d = "15324"
    print(d,sorted(d, reverse=True))
    e = {1:6,5:8,3:7,2:9,4:0}
    print(e,sorted(e,key=e.get, reverse=True))

def test_cmp_to_key():
    from functools import cmp_to_key
    def cmp(a,b):
        return 1 if a>b else -1
    a = [1,5,3,2,4]
    print(a,sorted(a,key=cmp_to_key(cmp)))
    # print(sorted(a,))
if __name__ == '__main__':
    # test_sorted_methods()
    test_cmp_to_key()