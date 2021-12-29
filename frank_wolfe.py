from scipy import optimize
import scipy.integrate as integrate
from scipy.optimize import minimize_scalar
import numpy as np
import scipy.linalg as la
import numpy.linalg as la2
import matplotlib.pyplot as plt


def estimatetime(t_0, x_a, c_a):
    ta = t_0 * (1 + 0.15 * (x_a / c_a) ** 4)
    return ta


def estimateZ(alpha, t_0, x_a, c_a, y_a):
    Z = 0
    for i in range(len(x_a)):
        Z += integrate.quad(
            lambda x: estimatetime(t_0[i], x, c_a[i]),
            0,
            x_a[i] + alpha * (y_a[i] - x_a[i]),
        )[0]
    return Z


def linesearch(t_0, x_a, c_a, y_a):
    alpha = minimize_scalar(
        estimateZ, args=(t_0, x_a, c_a, y_a), bounds=(0, 1), method="Bounded"
    )
    return alpha.x


def findEquilibrium(
    LinkNodeMatrix, LinkInfoMatrix, ODDemandMatrix, graph=False, verbose=False
):
    n_links, n_nodes = LinkNodeMatrix.shape

    t_0 = LinkInfoMatrix[:, 0]
    c_a = LinkInfoMatrix[:, 1]

    flow_from_origins = -np.sum(ODDemandMatrix, axis=1)
    np.fill_diagonal(ODDemandMatrix, flow_from_origins)

    c = np.tile(t_0, n_nodes)[:, np.newaxis]  # (n * k, 1)

    LinkNodeMatrix_T = np.transpose(LinkNodeMatrix)
    A = la.block_diag(*([LinkNodeMatrix_T] * n_nodes))  # (k * k, n * k)

    b = np.ravel(np.transpose(ODDemandMatrix), order="F")[:, np.newaxis]  # (k * k, 1)

    ybounds = (0, None)

    result = optimize.linprog(
        c,
        A_eq=A,
        b_eq=b,
        bounds=ybounds,
        options={"disp": verbose, "maxiter": 2000},
    )

    result = np.reshape(result["x"], (n_nodes, n_links))

    x_a = np.sum(result, axis=0)
    t_a = estimatetime(t_0, x_a, c_a)

    step = 0
    tanorm = 1000000

    iteration = []
    Z = []

    while (tanorm) > 0.001 * n_links:
        iteration.append(step)
        ta_old = t_a
        c = np.tile(t_a, n_nodes)[:, np.newaxis]

        result = optimize.linprog(
            c,
            A_eq=A,
            b_eq=b,
            bounds=ybounds,
            options={"disp": True, "maxiter": 2000},
        )

        result = np.reshape(result["x"], (n_nodes, n_links))
        y_a = np.sum(result, axis=0)

        alpha = linesearch(t_0, x_a, c_a, y_a)

        x_a = x_a + alpha * (y_a - x_a)

        t_a = estimatetime(t_0, x_a, c_a)
        tanorm = la2.norm(t_a - ta_old)

        z = np.dot(np.transpose(x_a), t_a)
        Z.append(z)

        step += 1

        if verbose:
            print("step ", step)
            print("x_a is ", x_a)
            print("ta is ", t_a)
            print("norm of ta is ", tanorm)

    if graph:
        plt.xlabel("iteration number")
        plt.ylabel("Z(x)")
        plt.plot(iteration, Z, "ro")
        plt.show()

    return x_a, t_a
