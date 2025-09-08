from aiogram.fsm.state import State, StatesGroup


class EmployeeSG(StatesGroup):
    start = State()