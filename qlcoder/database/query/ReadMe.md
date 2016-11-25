##item & query

- item attributes

```python
names = ["id", "price", "saleNum", "favNum", "color", "size", "itemNum", "created_at", "dsr", "tag"]
```

- query format

```python
for i in range(queryLimit):
    a, b = random.sample(tag, 2)
    Q = "(tag:*" + a + "* OR tag:*" + b + "*)"
    rd = random.sample(ls, 3)
    for j in rd:
        da = datas[j]
        m, n = random.sample(da, 2)
        if m > n:
            m, n = swap(m, n)
        if names[j] == "color":
            Q += " AND " + names[j] + ":" + str(m)
        else:
            Q += " AND " + names[j] + ":[" + str(m) + " TO " + str(n) + "]"
    out.write(Q + "\n")
```
