//
// Created by cheyulin on 11/2/16.
//

#ifndef CPP_MODULO_MODULOSOLVER_H
#define CPP_MODULO_MODULOSOLVER_H

#include <iostream>
#include <sstream>
#include <vector>
#include <list>
#include <string>
#include <unordered_map>

using namespace std;

using MatrixType = vector<vector<unsigned char>>;
using LookupMapType=unordered_map<MatrixType, vector<pair<unsigned char, unsigned char>>>;
constexpr long MAX_SIZE = 300 * 1024 * 1024;
extern hash<string> yche_hash_func_obj;

namespace std {
    template<>
    struct hash<vector<vector<unsigned char>>> {
        size_t operator()(const vector<vector<unsigned char>> &my_arr) const {
            stringstream ss;
            for (auto &row:my_arr) {
                for (auto &col:row) {
                    ss << col;
                }
            }
            return yche_hash_func_obj(ss.str());
        }
    };
}


class ModuloSolver {
public:
    void GetAnswer();

    ModuloSolver(int modulo_num, string &grid_str, vector<string> &piece_strs);

private:
    int modulo_num_;
    int grid_row_;
    int grid_col_;
    int bottom_depth_;

    MatrixType modulo_grid_;
    vector<MatrixType> pieces_;
    vector<int> pieces_sum_;
    int check_depth_;
    int max_possible_cell_num_;
    int min_possible_cell_num_;

    LookupMapType look_up_grids_;

    vector<string> Split(const string &s, char delim);

    MatrixType ExtractMatrix(string &matrix_str);

    int GetMatrixSum(const MatrixType &matrix);

    int GetPieceStateSize(const MatrixType &matrix);

    int GetStartCheckDepth();

    void PrintMatrix(const MatrixType &matrix, string msg = string(""));

    void PrintInitInfo();

    void DFSBuildMap(int depth, MatrixType &tmp_grid,
                     vector<pair<unsigned char, unsigned char>> &path_list);

    int GetLeftNumsCount(const MatrixType &my_map_arr);

    bool DFSLookup(int depth, int left_cells, vector<pair<unsigned char, unsigned char>> &path_list, MatrixType &my_map_arr);


};


#endif //CPP_MODULO_MODULOSOLVER_H
