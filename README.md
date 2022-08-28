# numerical_algorithm
This repo contains a few numerical algorithms I wrote during one of my engineering classes. The files names and associated information is summarised below.

### numerical_integration

1. Pick a function to integrate and define in integral().
2. Pick bounds of integration and specify the exact answer in true_value.
3. Select a range of increments for discrete calculations, specify in delta_x.
4. Modify x_coordinates if needed, to match the delta_x.

Example plot shown below:

![image](https://user-images.githubusercontent.com/89020809/187082172-442e24db-4331-4eba-9e43-c7494a64f655.png)



### cholesky_dcomp
A method to factorise a squre matrix in Lower and Upper triangle matrices (LU decomposition). This only works for Hermitian, positive definite matrix. 
Refer https://byjus.com/maths/cholesky-factorization/ for more information.


### matrix_solver
This file contains 2 main functions: 
1. calculate the determinant of any matrix
2. solve sparse tri-diagonal matrix (refer: https://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm)
