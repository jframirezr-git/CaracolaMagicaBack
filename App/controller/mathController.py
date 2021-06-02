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
               The number of iterations to implement."""
        f = lambda x: eval(data['function'])
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
