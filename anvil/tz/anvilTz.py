from dataclasses import dataclass


@dataclass
class tzoffset():
    pass


@dataclass
class tzlocal(tzoffset):
    pass


@dataclass
class tzutc(tzoffset):
    pass
