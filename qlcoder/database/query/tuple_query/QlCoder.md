##注意
- 需要注意的是： 同一个tag可能会在一条商品记录中出现多次， [拉链  xxx  拉链]
- 并且注意ik说的这个点


> 然而对Tag的搜索并不是直接相等的搜索，而是查找包含关系。换句话说，如果product的Tag是“聚酯纤维”，那么将会匹配“*聚酯*”这个Tag的查询。

- 自己写了一个小程序，没仔细看生成数据的python脚本，一开始被这一点坑了。

##思路
- 我只对tag进行了index，不同tag or操作的时候使用`set_union`
- 对于三个属性的过滤在对`set_union`出来结果遍历时候进行
- 使用C++写，开启`-O3`编译选项，然后单核大概需要60个小时
- 并行部分用openmp，编译选项加上 `-fopenmp`， 对独立的quey进行简单并行，对临界区保护`total`这个计数的变量

```cpp
#pragma omp parallel for
    for (auto i = 0; i < query_list.size(); i++) {
        auto tmp = CheckMatchNumber(tuple_list, tag_indices, query_list[i]);
//        cout << tmp << endl;
#pragma omp critical
        total += tmp;
    }
    cout << "Total:" << total << endl;
```


- 我用了学校的服务器， 40个逻辑CPU核， 1个半小时到2个小时出结果