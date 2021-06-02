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