from pydantic import BaseModel

class InputData(BaseModel):
    Sex: str
    Length: int
    Diameter: int
    Height: int
    Whole_weight: int
    Shucked_weight: int
    Viscera_weight: int
    Shell_weight: int
    
class PredictionOut(BaseModel):
    Age: float
