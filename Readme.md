How use it:
    steps:
        install requirements: pip install -r requirements.txt
        run  virtual environment
        run: uvicorn main:app 

This is the documentation for the endpoints:

        Absolute Mistate:
            end_point: /absolut_mistake
            request: {
                        'x1': X absoluto: number,
                        'x2': X relative: number
                        }