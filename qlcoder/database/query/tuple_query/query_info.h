//
// Created by cheyulin on 11/25/16.
//

#ifndef TUPLE_QUERY_QUERY_INFO_H
#define TUPLE_QUERY_QUERY_INFO_H

#include "util.h"

const string PRICE = string("price");
const string SALE_NUM = string("saleNum");
const string FAV_NUM = string("favNum");
const string COLOR = string("color");
const string SIZE = string("size");
const string ITEM_NUM = string("itemNum");
const string CREATE_AT = string("created_at");
const string DSR = string("dsr");


struct QueryInfo {
    vector<string> tags_;
    vector<vector<string>> constraints_;

    QueryInfo(string &query_str) {
        vector<string> query_cond_list = SplitReg(query_str, " AND ");
        constraints_.resize(3);
        // only three constraints
        tags_.resize(2);
        auto &tag_str = query_cond_list[0];
        auto tags = SplitReg(tag_str, " OR ");
        tags_[0] = SplitReg(tags[0], "\\*")[1];
        tags_[1] = SplitReg(tags[1], "\\*")[1];

        constraints_[0] = move(SplitConstraint(query_cond_list[1]));
        constraints_[1] = move(SplitConstraint(query_cond_list[2]));
        constraints_[2] = move(SplitConstraint(query_cond_list[3]));
    }

    QueryInfo(QueryInfo &&query_info) {
        tags_ = move(query_info.tags_);
        constraints_ = move(query_info.constraints_);
    }

};

#endif //TUPLE_QUERY_QUERY_INFO_H
