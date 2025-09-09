from pydantic import BaseModel, Field
from typing import List

class ModelConfig(BaseModel):
    model_name: str = Field(..., description="Name of the ML model")
    learning_rate: float = Field(..., ge=0, le=1)
    layers: List[int] = Field(..., description="List of hidden layer sizes")


if __name__ == "__main__":
    # Example usage
    cfg = ModelConfig(
        model_name="transformer",
        learning_rate=0.001,
        layers=[256, 128, 64]
    )

    print(cfg)
