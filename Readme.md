How use it:

    steps:

        install requirements: pip install -r requirements.txt
        run  virtual environment
        run: uvicorn main:app 

This is the documentation for the endpoints:

        Absolute Mistake:
            end point: /absolut_mistake
            method: POST
            request: {
                        'x1': number,
                        'x2': number
                        }
            response: {"error": number}

        Relative Mistake:
            end point: /relative_mistake
            method: POST
            request: {
                        'error': number,
                        'x': number
                        }
            response: {"error": number}

        Correct Decimals:
            end point: /correct_decimals
            method: POST
            request: {
                        'x1': number,
                        'x2': number,
                        'decimal': number
                        }
            responde: {"correct": boolean}

        Bisection:
            Parameters
           ----------
           f : function
               The function for which we are trying to approximate a solution f(x)=0.
           a,b : numbers
               The interval in which to search for a solution. The function returns
               None if f(a)*f(b) >= 0 since a solution is not guaranteed.
           N : (positive) integer
               The number of iterations to implement.

            end point: /bisection
            method: POST
            request: {
                        'f': string,
                        'a': number,
                        'b': number,
                        'N': number
                        }
            responde: {"correct": boolean} | {"correct":boolean, "result": number"}

        Newton:
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

             end point: /newton
            method: POST
            request: {
                        'f': string,
                        'df': number,
                        'x0': number,
                        'epsilon': number,
                        'max_iter': number
                        }
            responde: {"correct": boolean} | {"correct":boolean, "result": number"}

        Secant:
             Parameters
            ----------
            f : function
                The function for which we are trying to approximate a solution f(x)=0.
            a,b : numbers
                The interval in which to search for a solution. The function returns
                None if f(a)*f(b) >= 0 since a solution is not guaranteed.
            N : (positive) integer
                The number of iterations to implement.

            end point: /secant
            method: POST
            request: {
                        'f': string,
                        'a': number,
                        'b': number,
                        'N': number
                        }
            responde: {"correct": boolean} | {"correct":boolean, "result": number"}

        Jacobi:
            Solves the equation Ax=b via the Jacobi iterative method.
            Parameters
            ----------
            A,b,N,x
            

            Example
            ----------
            {
                "A": [[2.0,1.0],[5.0,7.0]],
                "b": [11.0,13.0],
                "N": 5,
                "x": [1.0,1.0]  #x can be string but void "".
            }
            end point: /jacobi
            method: POST
            request: {
                        'A': array,
                        'b': array,
                        'N': number,
                        'x': array
                        }
            responde: {"result": "string"}

            