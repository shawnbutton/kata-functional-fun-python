from dataclasses import dataclass


@dataclass
class Reading:
    type: str
    inactive: bool
    data: any
    temperature: float
