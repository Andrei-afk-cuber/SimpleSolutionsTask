from typing import Annotated

from sqlmodel import Session
from fastapi import Depends

from ..database import engine


# Dependency for session
def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]