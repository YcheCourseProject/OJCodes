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

using namespace std;

using MatrixType = vector<vector<unsigned char>>;

class ModuloSolver {
public:

private:
    int modulo_num_;
    int grid_row_;
    int grid_col_;
    MatrixType modulo_grid_;
    vector<MatrixType> pieces_;
    vector<int> pieces_sum_;

    int marked_num_;

    vector<string> Split(const string &s, char delim);

    MatrixType ExtractMatrix(string &matrix_str);

    void PrintMatrix(const MatrixType &matrix, string msg = string(""));

    int GetMatrixSum(const MatrixType &matrix);

    int GetPieceStateSize(const MatrixType &matrix);

public:
    ModuloSolver(int modulo_num, string &grid_str, vector<string> &piece_strs);

private:
    bool DepthFirstSearch(int depth, MatrixType &my_map_arr);
};


#endif //CPP_MODULO_MODULOSOLVER_H
