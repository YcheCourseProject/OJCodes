arr = ['id', 'price', 'saleNum', 'favNum', 'color', 'size', 'itemNum', 'created_at', 'dsr', 'tag']
print len(arr)
arr2 = [(i, arr[i]) for i in range(len(arr))]
print arr2
for ele in arr2:
    print ele[0], ":", ele[1]
