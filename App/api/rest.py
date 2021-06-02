from starlette.responses import JSONResponse
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware

from App.controller import MathController

app = Starlette()
app.add_middleware(CORSMiddleware, allow_methods=['POST', 'GET'], allow_origins=['*'], allow_headers=['*'])


@app.route(path='/login', methods=['GET'])
async def homepage(request):
    response = await MathController.absolut_mistake()
    return JSONResponse(response)
