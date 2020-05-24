''' note serializer '''
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict, List

from .base_activity import ActivityObject, Image

@dataclass(init=False)
class Note(ActivityObject):
    ''' Note activity '''
    url: str
    inReplyTo: str
    published: str
    attributedTo: str
    to: List[str]
    cc: List[str]
    content: str
    replies: Dict
    # TODO: this is wrong???
    attachment: List[Image] = field(default=lambda: [])
    sensitive: bool = False
