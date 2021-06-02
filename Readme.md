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