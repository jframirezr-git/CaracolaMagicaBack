How use it:

    steps:

        install requirements: pip install -r requirements.txt
        run  virtual environment
        run: uvicorn main:app 

This is the documentation for the endpoints:

        Absolute Mistake:
            end point: /absolut_mistake
            request: {
                        'x1': number,
                        'x2': number
                        }
        Relative Mistake:
            end point: /relative_mistake
            request: {
                        'error': number,
                        'x': number
                        }