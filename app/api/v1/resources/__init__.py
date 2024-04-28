# resources/__init__.py

from .chats import api as chats
from .documents import api as documents
from .users import api as users
from .agents import api as agents

__all__ = ["chats", "documents", "users", "agents"]