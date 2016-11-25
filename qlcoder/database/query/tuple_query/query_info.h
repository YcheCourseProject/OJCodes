//
// Created by cheyulin on 11/25/16.
//

#ifndef TUPLE_QUERY_QUERY_INFO_H
#define TUPLE_QUERY_QUERY_INFO_H

#include "util.h"

struct QueryInfo {
    vector<string> tags_;
    vector<string> first_constraint_;
    vector<string> second_constraint_;
    vector<string> third_constraint_;

    QueryInfo(string &query_str) {
        vector<string> query_cond_list = SplitReg(query_str, " AND ");

        // only three constraints
        tags_.resize(2);
        auto &tag_str = query_cond_list[0];
        auto tags = SplitReg(tag_str, " OR ");
        tags_[0] = SplitReg(tags[0], "\\*")[1];
        tags_[1] = SplitReg(tags[1], "\\*")[1];

        first_constraint_ = move(SplitConstraint(query_cond_list[1]));
        second_constraint_ = move(SplitConstraint(query_cond_list[2]));
        third_constraint_ = move(SplitConstraint(query_cond_list[3]));
    }

    QueryInfo(QueryInfo &&query_info) {
        tags_ = move(query_info.tags_);
        first_constraint_ = move(query_info.first_constraint_);
        second_constraint_ = move(query_info.second_constraint_);
        third_constraint_ = move(query_info.third_constraint_);
    }

};

#endif //TUPLE_QUERY_QUERY_INFO_H
