from dataclasses import dataclass


@dataclass
class Reading:
    name: str
    type: str
    inactive: bool
    data: any
    temperature: float
