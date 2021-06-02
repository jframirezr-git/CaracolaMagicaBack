
# Here we implements the differents math methods.
class MathController:

    @classmethod
    async def absolut_mistake(cls, data: dict):
        error = data['x1'] - data['x2']
        return {"error": error}
