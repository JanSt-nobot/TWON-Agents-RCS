from typing import Literal

from src.schemas import platform
from .base import BaseRequest


class ReplyRequest(BaseRequest):
    thread: platform.Thread
    length: Literal['50', '100', '200', '280'] = '100'

    model_config = {
        "json_schema_extra": {
            "examples": [
                BaseRequest.model_config["json_schema_extra"]["examples"][0]
                | {"thread": platform.Thread.model_config["json_schema_extra"]["examples"][0], "length": "few-word"}
            ]
        }
    }
