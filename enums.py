
from enum import Enum


class RoleEnum(str, Enum):
    DEMO = 'Демо-режим'
    BASIC = 'Обычная подписка'
    PRO = 'Расширенная подписка'