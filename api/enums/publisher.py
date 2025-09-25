from enum import Enum


class PublisherStatus(Enum):
    """Publisher status"""
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'
    DRAFT = 'DRAFT'
    NEED_TO_APPROVE = 'NEED_TO_APPROVE'
