##Tuple

- python preprocess field result

```python
[(0, 'id'), (1, 'price'), (2, 'saleNum'), (3, 'favNum'), (4, 'color'), (5, 'size'), (6, 'itemNum'), (7, 'created_at'), (8, 'dsr'), (9, 'tag')]
```

- tuple column

```zsh
0 : id
1 : price
2 : saleNum
3 : favNum
4 : color
5 : size
6 : itemNum
7 : created_at
8 : dsr
9 : tag
```

- description

```zsh
id: 商品id long
price: 价格 int
saleNum: 销量 int
favNum: 收藏点赞数 int
color: 主要颜色 text {红橙黄绿青蓝紫等等}
size: 尺寸 1-7 分别代表{XS,S,M,L,XL,XXL,XXXL}
itemNum: 库存 int
created_at: 创建时间 long 时间戳表示
dsr: 店铺动态评分 float 范围 2.0-5.0
tag: 标签 text
```