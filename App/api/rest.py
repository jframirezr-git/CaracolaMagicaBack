from starlette.responses import JSONResponse
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware

from App.controller import MathController

# initialize project
app = Starlette()
# add CORDS politics
app.add_middleware(CORSMiddleware, allow_methods=['POST', 'GET'], allow_origins=['*'], allow_headers=['*'])
app.add_middleware(ProxyHeadersMiddleware)


# Here are the rest methods.
@app.route(path='/absolut_mistake', methods=['POST'])
async def absolut_mistake(request: Request):
    data: dict = await request.json()
    response = await MathController.absolut_mistake(data=data)
    return JSONResponse(response)


@app.route(path='/relative_mistake', methods=['POST'])
async def relative_mistake(request: Request):
    data: dict = await request.json()
    response = await MathController.relative_mistake(data=data)
    return JSONResponse(response)


@app.route(path='/correct_decimals', methods=['POST'])
async def correct_decimals(request: Request):
    data: dict = await request.json()
    response = await MathController.correct_decimals(data=data)
    return JSONResponse(response)


@app.route(path='/bisection', methods=['POST'])
async def bisection(request: Request):
    data: dict = await request.json()
    response = await MathController.bisection(data=data)
    return JSONResponse(response)


@app.route(path='/newton', methods=['POST'])
async def newton(request: Request):
    data: dict = await request.json()
    response = await MathController.newton(data=data)
    return JSONResponse(response)


@app.route(path='/secant', methods=['POST'])
async def newton(request: Request):
    data: dict = await request.json()
    response = await MathController.secant(data=data)
    return JSONResponse(response)


@app.route(path='/jacobi', methods=['POST'])
async def newton(request: Request):
    data: dict = await request.json()
    response = await MathController.jacobi(data=data)
    return JSONResponse(response)


@app.route(path='/gauss', methods=['POST'])
async def newton(request: Request):
    data: dict = await request.json()
    response = await MathController.gauss(data=data)
    return JSONResponse(response)


@app.route(path='/gausspi', methods=['POST'])
async def newton(request: Request):
    data: dict = await request.json()
    response = await MathController.gausspi(data=data)
    return JSONResponse(response)


@app.route(path='/gaussto', methods=['POST'])
async def newton(request: Request):
    data: dict = await request.json()
    response = await MathController.gaussto(data=data)
    return JSONResponse(response)


@app.route(path='/gausslu', methods=['POST'])
async def newton(request: Request):
    data: dict = await request.json()
    response = await MathController.gausslu(data=data)
    return JSONResponse(response)
