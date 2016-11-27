##注意
- 需要注意的是： 同一个tag可能会在一条商品记录中出现多次， [拉链  xxx  拉链]
- 并且注意ik说的这个点


> 然而对Tag的搜索并不是直接相等的搜索，而是查找包含关系。换句话说，如果product的Tag是“聚酯纤维”，那么将会匹配“*聚酯*”这个Tag的查询。

- 自己写了一个小程序，没仔细看生成数据的python脚本，一开始被这一点坑了。

- 读文件，建立index, 注意以上两个比较坑的地方

```cpp
const string special_tag = string("聚酯纤维");
const string special_tag_sub_str = string("聚酯");

void InitTupleList(vector<TupleInfo> &tuple_list, unordered_map<string, vector<long>> &tag_indices) {
    ifstream input_stream(data_path);
    string tmp_str;
    getline(input_stream, tmp_str);
    while (getline(input_stream, tmp_str)) {
        tuple_list.emplace_back(tmp_str);
        auto &cur_tuple = tuple_list.back();
        for (auto &tag_str:cur_tuple.tag_list_) {
            if (tag_indices[tag_str].size() > 0 && tag_indices[tag_str].back() == cur_tuple.good_id_) {
                continue;
            }
            tag_indices[tag_str].push_back(cur_tuple.good_id_);
            if (tag_str == special_tag) {
                if (tag_indices[special_tag_sub_str].size() > 0 &&
                    tag_indices[special_tag_sub_str].back() == cur_tuple.good_id_) {
                    continue;
                }
                tag_indices[special_tag_sub_str].push_back(cur_tuple.good_id_);
            }
        }
    }

    PrintTupleListInfo(tuple_list);
    cout << "tuple size:\t" << tuple_list.size() << endl;
    cout << "tag size:\t" << tag_indices.size() << endl;
}
```

##思路
- 我只对tag进行了index，不同tag or操作的时候使用`set_union`
- 对于三个属性的过滤在对`set_union`出来结果遍历时候进行
- 过滤的判断如下，过滤的条件为了方便起见，都存在string里面了，判断的时候现场转为`long`或`int`或`float`：

```

bool CheckSingleTuple(TupleInfo &tuple, vector<vector<string>> &constraints) {
    for (auto &constraint:constraints) {
        if (constraint[0] == COLOR) {
            if (tuple.color_ != constraint[1])
                return false;
        } else if (constraint[0] == PRICE) {
            int left = stoi(constraint[1]);
            int right = stoi(constraint[2]);
            if (tuple.price_ < left || tuple.price_ > right)
                return false;
        } else if (constraint[0] == SALE_NUM) {
            int left = stoi(constraint[1]);
            int right = stoi(constraint[2]);
            if (tuple.sale_num_ < left || tuple.sale_num_ > right)
                return false;
        } else if (constraint[0] == FAV_NUM) {
            int left = stoi(constraint[1]);
            int right = stoi(constraint[2]);
            if (tuple.fav_num_ < left || tuple.fav_num_ > right)
                return false;
        } else if (constraint[0] == SIZE) {
            int left = stoi(constraint[1]);
            int right = stoi(constraint[2]);
            if (tuple.size_ < left || tuple.size_ > right)
                return false;
        } else if (constraint[0] == ITEM_NUM) {
            int left = stoi(constraint[1]);
            int right = stoi(constraint[2]);
            if (tuple.item_num_ < left || tuple.item_num_ > right)
                return false;
        } else if (constraint[0] == CREATE_AT) {
            long left = stol(constraint[1]);
            long right = stol(constraint[2]);
            if (tuple.create_at_ < left || tuple.create_at_ > right)
                return false;
        } else if (constraint[0] == DSR) {
            float left = stof(constraint[1]);
            float right = stof(constraint[2]);
            if (tuple.dsr_ < left || tuple.dsr_ > right)
                return false;
        } else {
            cerr << "something wrong" << endl;
            cout << "something wrong" << endl;
        }
    }
    return true;
}
```

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
