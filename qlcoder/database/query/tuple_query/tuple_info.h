//
// Created by cheyulin on 11/25/16.
//

#ifndef TUPLE_QUERY_TUPLE_INFO_H
#define TUPLE_QUERY_TUPLE_INFO_H

#include "util.h"

struct TupleInfo {
    long good_id_;
    int price_;
    int sale_num_;
    int fav_num_;
    string color_;
    string size_;
    int item_num_;
    long create_at_;
    float dsr_;
    vector<string> tag_list_;

    TupleInfo(string &my_tuple_str) {
        auto my_cols = Split(my_tuple_str, ',');
        auto tags = Split(my_cols[my_cols.size() - 1], ' ');
        good_id_ = stol(my_cols[0]);
        price_ = stoi(my_cols[1]);
        sale_num_ = stoi(my_cols[2]);
        fav_num_ = stoi(my_cols[3]);
        color_ = move(my_cols[4]);
        size_ = move(my_cols[5]);
        item_num_ = stoi(my_cols[6]);
        create_at_ = stol(my_cols[7]);
        dsr_ = stof(my_cols[8]);
        tag_list_ = move(tags);
    }

    TupleInfo(TupleInfo &&tuple_info) {
        good_id_ = tuple_info.good_id_;
        price_ = tuple_info.price_;
        sale_num_ = tuple_info.sale_num_;
        fav_num_ = tuple_info.fav_num_;
        color_ = move(tuple_info.color_);
        size_ = move(tuple_info.size_);
        item_num_ = tuple_info.item_num_;
        create_at_ = tuple_info.create_at_;
        dsr_ = tuple_info.dsr_;
        tag_list_ = move(tuple_info.tag_list_);
    }

    void Print() {
        cout << "(" << good_id_ << ", " << price_ << ", " << sale_num_ << ", " << fav_num_ << ", " << color_ << ", "
             << size_ << ", " << item_num_ << ", " << create_at_ << ", " << dsr_ << ", " << tag_list_ << ")" << endl;
    }

};

#endif //TUPLE_QUERY_TUPLE_INFO_H
