import numpy as np
from scipy.io import mmread

# 1) načtení Matrix Market souboru ze SuiteSparse
A_sparse = mmread("abb313.mtx")
B_sparse = mmread("bcspwr01.mtx")
C_sparse = mmread("ash219.mtx")
D_sparse = mmread("lp_stocfor.mtx")

# 2) převedení do CSR formátu
A_sparse = A_sparse.tocsr()
B_sparse = B_sparse.tocsr()
C_sparse = C_sparse.tocsr()
D_sparse = D_sparse.tocsr()

# 3) QR rozklad → dense matice
A = A_sparse.toarray()
B = B_sparse.toarray()
C = C_sparse.toarray()
D = D_sparse.toarray()


def classic_GS(A):
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    for j in range(n):
        z = A[:, j]
        for k in range(j):  # Ortogonalizace
            R[k, j] = np.dot(Q[:, k].T, z)
            z = z - R[k, j] * Q[:, k]
        R[j, j] = np.linalg.norm(z)
        if R[j, j] != 0:
            Q[:, j] = z / R[j, j]
        else:
            Q[:, j] = np.zeros_like(z)
    return Q, R


def mod_GS(A):
    m, n = A.shape
    V = A.copy().astype(float)  # vektory v_j
    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    for j in range(n):
        R[j, j] = np.linalg.norm(V[:, j])
        if R[j, j] != 0:
            Q[:, j] = V[:, j] / R[j, j]
        else:
            Q[:, j] = np.zeros_like(V[:, j])

        for k in range(j + 1, n):   # Ortogonalizace
            R[j, k] = np.dot(Q[:, j].T, V[:, k])
            V[:, k] = V[:, k] - R[j, k] * Q[:, j]

    return Q, R


def test(A, name):
    print(f"Matice {name}, tvar {A.shape}")

    Q, R = classic_GS(A)
    print("Classic GS:")
    print("||A - QR|| =", np.linalg.norm(A - Q @ R))
    print("||QᵀQ - I|| =", np.linalg.norm(Q.T @ Q - np.eye(Q.shape[1])))

    Q, R = mod_GS(A)
    print("Modified GS:")
    print("||A - QR|| =", np.linalg.norm(A - Q @ R))
    print("||QᵀQ - I|| =", np.linalg.norm(Q.T @ Q - np.eye(Q.shape[1])))
    print("-" * 40)


test(A, "A")
test(B, "B")
test(C, "C")
test(D, "D")
