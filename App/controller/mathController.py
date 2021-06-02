
# Here we implements the differents math methods.
class MathController:

    @classmethod
    async def absolut_mistake(cls, data: dict):
        error = data['x1'] - data['x2']
        return {"error": error}

    @classmethod
    async def relative_mistake(cls, data: dict):
        error = data['error']/data['x']
        return {"error": error}

    @classmethod
    async def correct_decimals(cls, data: dict):
        minor_result = data['x2'] - 0.5 ** (- data['decimal'])
        mayor_result = data['x2'] + 0.5 ** (- data['decimal'])
        if minor_result <= data['x1'] < mayor_result:
            return {"correct": True}
        else:
            return {"correct": False}
