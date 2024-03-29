import os
import sys

from fastapi import FastAPI

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    print("Hi")
    print(os.environ["PYTHONPATH"])
