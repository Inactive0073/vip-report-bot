from enum import Enum

class UserRole(Enum):
    ADMIN = (1, "Админ")
    EMPLOYEE = (2, "Сотрудник")

    def __init__(self, role_id: int, label: str):
        self.role_id = role_id
        self.label = label

    @classmethod
    def get_role_by_id(cls, id_: int):
        for role in cls:
            if role.role_id == id_:
                return role

class StoreMode(Enum):
    EDIT = "edit"
    ADD = "add"