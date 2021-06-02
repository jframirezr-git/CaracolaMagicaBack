from starlette.responses import JSONResponse
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request

from App.controller import MathController

# initialize project
app = Starlette()
# add CORDS politics
app.add_middleware(CORSMiddleware, allow_methods=['POST', 'GET'], allow_origins=['*'], allow_headers=['*'])


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
