from enum import Enum


class TaskType(Enum):
    BUG = "Bug"
    FEATURE = "Feature"
    IMPROVEMENT = "Improvement"


class TaskPriority(Enum):
    BLOCKER = "Blocker"
    CRITICAL = "Critical"
    MAJOR = "Major"
    MINOR = "Minor"
    TRIVIAL = "Trivial"


class TaskStatus(Enum):
    BACKLOG = "Backlog"
    TODO = "Todo"
    IN_PROGRESS = "In_progress"
    DONE = "Done"