//
// Created by cheyulin on 11/2/16.
//

#ifndef CPP_MODULO_MODULOSOLVER_H
#define CPP_MODULO_MODULOSOLVER_H

#include <vector>
#include <list>

using namespace std;

using PieceMatrixType=vector<vector<unsigned char>>;
using ModuloGridType = vector<vector<unsigned char>>;


struct PieceInfo {
    PieceMatrixType piece_matrix_;
    int piece_counts_;

    PieceInfo(const PieceMatrixType &piece_matrix,
              int piece_counts) : piece_matrix_(piece_matrix), piece_counts_(piece_counts) {}
};


struct GridInfo {

};


struct TmpGridInfo : public GridInfo {

};

class ModuloSolver {
public:

private:
    int row_num_;
    int col_num_;
    int init_marked_num_;
    ModuloSolver modulo_grid_;

    bool DepthFirstSearch(int depth, ModuloGridType &my_map_arr);
};


#endif //CPP_MODULO_MODULOSOLVER_H
