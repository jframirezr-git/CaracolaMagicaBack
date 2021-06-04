import json
import copy

from numpy import array, zeros, diag, diagflat, dot
import numpy as np


# Here we implements the differents math methods.
class MathController:

    @classmethod
    async def absolut_mistake(cls, data: dict):
        error = data['x1'] - data['x2']
        return {"error": error}

    @classmethod
    async def relative_mistake(cls, data: dict):
        error = data['error'] / data['x']
        return {"error": error}

    @classmethod
    async def correct_decimals(cls, data: dict):
        minor_result = data['x2'] - 0.5 ** (- data['decimal'])
        mayor_result = data['x2'] + 0.5 ** (- data['decimal'])
        if minor_result <= data['x1'] < mayor_result:
            return {"correct": True}
        else:
            return {"correct": False}

    # implement busquedas

    @classmethod
    async def bisection(cls, data: dict):
        """Approximate solution of f(x)=0 on interval [a,b] by bisection method.

           Parameters
           ----------
           f : function
               The function for which we are trying to approximate a solution f(x)=0.
           a,b : numbers
               The interval in which to search for a solution. The function returns
               None if f(a)*f(b) >= 0 since a solution is not guaranteed.
           N : (positive) integer
               The number of iterations to implement.

             Returns
            -------
            x_N : number
            The midpoint of the Nth interval computed by the bisection method. The
            initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0 for some
            midpoint m_n = (a_n + b_n)/2, then the function returns this solution.
            If all signs of values f(a_n), f(b_n) and f(m_n) are the same at any
            iteration, the bisection method fails and return None"""

        f = lambda x: eval(data['f'])
        if f(data['a']) * f(data['b']) >= 0:
            return {'correct': False}
        a_n = data['a']
        b_n = data['b']
        for n in range(1, data['N'] + 1):
            m_n = (a_n + b_n) / 2
            f_m_n = f(m_n)
            if f(a_n) * f_m_n < 0:
                a_n = a_n
                b_n = m_n
            elif f(b_n) * f_m_n < 0:
                a_n = m_n
                b_n = b_n
            elif f_m_n == 0:
                return {'correct': True, 'result': m_n}
            else:
                return {'correct': False}
        result = (a_n + b_n) / 2
        return {'correct': True, 'result': result}

    @classmethod
    async def newton(cls, data: dict):
        """Approximate solution of f(x)=0 by Newton's method.

            Parameters
            ----------
            f : function
                Function for which we are searching for a solution f(x)=0.
            df : function
                Derivative of f(x).
            x0 : number
                Initial guess for a solution f(x)=0.
            epsilon : number
                Stopping criteria is abs(f(x)) < epsilon.
            max_iter : integer
                Maximum number of iterations of Newton's method.

            Returns
            -------
            xn : number
                Implement Newton's method: compute the linear approximation
                of f(x) at xn and find x intercept by the formula
                    x = xn - f(xn)/Df(xn)
                Continue until abs(f(xn)) < epsilon and return xn.
                If Df(xn) == 0, return None. If the number of iterations
                exceeds max_iter, then return None. """

        f = lambda x: eval(data['f'])
        Df = lambda x: eval(data['df'])
        xn = data['x0']
        for n in range(0, data['max_iter']):
            fxn = f(xn)
            if abs(fxn) < data['epsilon']:
                return {'correct': True, 'result': xn}
            Dfxn = Df(xn)
            if Dfxn == 0:
                return {'correct': False}
            xn = xn - fxn / Dfxn
        return {'correct': False}

    @classmethod
    async def secant(cls, data: dict):
        """Approximate solution of f(x)=0 on interval [a,b] by the secant method.

            Parameters
            ----------
            f : function
                The function for which we are trying to approximate a solution f(x)=0.
            a,b : numbers
                The interval in which to search for a solution. The function returns
                None if f(a)*f(b) >= 0 since a solution is not guaranteed.
            N : (positive) integer
                The number of iterations to implement.

            Returns
            -------
            m_N : number
                The x intercept of the secant line on the the Nth interval
                    m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
                The initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0
                for some intercept m_n then the function returns this solution.
                If all signs of values f(a_n), f(b_n) and f(m_n) are the same at any
                iterations, the secant method fails and return None. """

        f = lambda x: eval(data['f'])
        if f(data['a']) * f(data['b']) >= 0:
            print("Secant method fails.")
            return None
        a_n = data['a']
        b_n = data['b']
        for n in range(1, data['N'] + 1):
            m_n = a_n - f(a_n) * (b_n - a_n) / (f(b_n) - f(a_n))
            f_m_n = f(m_n)
            if f(a_n) * f_m_n < 0:
                a_n = a_n
                b_n = m_n
            elif f(b_n) * f_m_n < 0:
                a_n = m_n
                b_n = b_n
            elif f_m_n == 0:
                return {'correct': True, 'result': m_n}
            else:
                return {'correct': False}
        result = a_n - f(a_n) * (b_n - a_n) / (f(b_n) - f(a_n))
        return {'correct': True, 'result': result}

    @classmethod
    async def jacobi(cls, data: dict):
        """Solves the equation Ax=b via the Jacobi iterative method.
        Parameters
        ----------
        A,b,N,x
        """
        # Create an initial guess if needed
        x = data['x']
        if x == "":
            x = zeros(len(data['A'][0]))

        # Create a vector of the diagonal elements of A
        # and subtract them from A
        D = diag(data['A'])
        R = data['A'] - diagflat(D)

        # Iterate for N times
        for i in range(data['N']):
            x = (data['b'] - dot(R, x)) / D
        lists = x.tolist()
        result = json.dumps(lists)
        return {'result': result}

    @classmethod
    async def gauss(cls, data: dict):
        M = array(data['M'])
        n = len(M)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if M[j, i] != 0:
                    M[j, i:n + 1] = M[j, i:n + 1] - [M[j, i] / M[i, i]] * M[i, i:n + 1]

        lists = M.tolist()
        result = json.dumps(lists)
        return {'result': result}

    @classmethod
    async def gausspi(cls, data: dict):
        M = array(data['M'])
        n = len(M)
        for i in range(n - 1):
            aux0 = max(abs(M[i + 1:n, i]))
            aux = np.where(M == aux0)[0]
            if aux0 > abs(M[i, i]):
                aux2 = copy.deepcopy(M[i + aux, i:n + 1])
                M[aux + i, i:n + 1] = M[i, i:n + 1]
                M[i, i:n + 1] = aux2

            for j in range(i + 1, n):
                if M[j, i] != 0:
                    M[j, i:n + 1] = M[j, i:n + 1] - [M[j, i] / M[i, i]] * M[i, i:n + 1]

        lists = M.tolist()
        result = json.dumps(lists)
        return {'result': result}

    @classmethod
    async def gaussto(cls, data: dict):
        M = array(data['M'])
        n = len(M)
        cambi = []
        for i in range(n - 1):
            (a, b) = np.where(abs(M[i:n, i:]) == abs(M[i:n, i:n]).max(0).max(0))
            if (b[0] + i) != i:
                cambi = [i, b[0] + i]
                aux2 = copy.deepcopy(M[:, b[0] + i])
                M[:, b[0] + i] = M[:, i]
                M[:, i] = aux2

            if a[0] + i != i:
                print("entro")
                aux2 = copy.deepcopy(M[i + a[0], i:n + 1])
                M[a[0] + i, i:n + 1] = M[i, i:n + 1]
                M[i, i:n + 1] = aux2

            for j in range(i + 1, n):
                if M[j, i] != 0:
                    M[j, i:n + 1] = M[j, i:n + 1] - [M[j, i] / M[i, i]] * M[i, i:n + 1]

        lists = M.tolist()
        result = json.dumps(lists)
        return {'result': result}

    @classmethod
    async def gausslu(cls, data: dict):
        M = array(data['M'])
        n = len(M)
        L = np.identity(n)
        U = np.zeros((n, n))

        for i in range(n - 1):
            for j in range(i + 1, n):
                if M[j, i] != 0:
                    L[j, i] = M[j, i] / M[i, i]
                    M[j, i:n] = M[j, i:n] - [M[j, i] / M[i, i]] * M[i, i:n]

            U[i, i:n] = M[i, i:n]
            U[i + 1, i + 1:n] = M[i + 1, i + 1:n]
        U[n - 1, n - 1] = M[n - 1, n - 1]

        print(U)
        lists = M.tolist()
        result = json.dumps(lists)
        return {'result': result}

    @classmethod
    async def gaussseidel(cls, data: dict):
        global xact
        M = array(data['M'])
        b = data['b']
        x0 = data['x0']
        tol = data['tol']
        nmax = data['nmax']

        D = np.diag(np.diag(M))

        L = - np.tril(M) + D

        U = - np.triu(M) + D
        T = np.dot(np.linalg.inv(D - L), U)
        C = np.dot(np.linalg.inv(D - L), b)
        xant = x0
        E = 1000
        cont = 0

        while E > tol and cont < nmax:
            xact = T * xant + C
            E = np.linalg.norm(xant - xact)
            xant = xact
            cont = cont + 1

        print(xact, cont, E)
        lists = M.tolist()
        result = json.dumps(lists)
        return {'result': result}
