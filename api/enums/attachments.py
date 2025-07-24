from enum import Enum


class AttachmentUploadStatus(Enum):
    PENDING = 'PENDING'
    UPLOADED = 'UPLOADED'
    ERROR = 'ERROR'