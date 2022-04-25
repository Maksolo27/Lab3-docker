from fastapi import APIRouter
import numpy as np

router = APIRouter()

@router.get('')
def matrix() -> dict:
    mat1 = np.random.randint(100, size=[10, 10])
    mat2 = np.random.randint(100, size=[10, 10])
    resMat = np.matmul(mat1, mat2)
    mat1 = np.array2string(mat1)
    mat2 = np.array2string(mat2)
    resMat = np.array2string(resMat)
    return {'msg': { 'matrix_a': mat1, 'matrix_b': mat2, 'product': resMat }}