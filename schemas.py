from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship
from enum import Enum as Enum_


class TeamBase(SQLModel):
    name: str = Field(index=True)
    headquarters: str


class Team(TeamBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    heroes: List["Hero"] = Relationship(back_populates="team")


class TeamCreate(TeamBase):
    pass


class TeamRead(TeamBase):
    id: int


class TeamUpdate(SQLModel):
    name: Optional[str] = None
    headquarters: Optional[str] = None


class Enum(Enum_):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class Status(str, Enum):
    CLIENT = "CLIENT"
    TRAINER = "TRAINER"


class HeroBase(SQLModel):
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)
    status: Status = Status.CLIENT

    team_id: Optional[int] = Field(default=None, foreign_key="team.id")


class Hero(HeroBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    team: Optional[Team] = Relationship(back_populates="heroes")


class HeroCreate(HeroBase):
    status: Status = Status.CLIENT


class HeroRead(HeroBase):
    id: int


class HeroUpdate(SQLModel):
    name: Optional[str] = None
    secret_name: Optional[str] = None
    age: Optional[int] = None
    status: Status = Status.CLIENT
    team_id: Optional[int] = None


class TeamReadWithHeroes(TeamRead):
    heroes: List[HeroRead] = []


class HeroReadWithTeam(HeroRead):
    team: Optional[TeamRead] = None
