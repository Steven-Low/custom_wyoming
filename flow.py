"""STT-INTENT-TTS FLOW"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional
from wyoming.event import Event, Eventable
 
DOMAIN = "flow"
_FLOW_TYPE = "flow"

@dataclass
class Flow(Eventable):
    """Request to synthesize a chain of audio segments in a single request."""
    audio: bytearray
    """Audio bytes in stream"""

    language: str | None = None
    """Language of the chain."""
    
    @staticmethod
    def is_type(event_type: str) -> bool:
        return event_type == _FLOW_TYPE
    
    def event(self) -> Event:
        data: Dict[str, Any] = {"audio": self.audio}
        if self.language is not None:
            data["language"] = self.language
 
        return Event(type=_FLOW_TYPE, data=data)
    
    @staticmethod
    def from_event(event: Event) -> "Flow":
        assert event.data is not None
        return Flow(
            audio=event.data["audio"],
            language=event.data.get("language")
        )