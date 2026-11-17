from enum import Enum


class Choice(str, Enum):
    """
    String enum that also accepts loosely written values,
    e.g. "On Hold", "on-hold" and "ON_HOLD" all become "on_hold".
    Handy for hand-written / LLM-generated JSON.
    """

    @classmethod
    def _missing_(cls, value):
        if isinstance(value, str):
            normalized = value.strip().lower().replace("-", "_").replace(" ", "_")
            for member in cls:
                if member.value == normalized:
                    return member
        return None


class ApplicationStatus(Choice):
    DISCOVERED = "discovered"
    INTERESTED = "interested"
    APPLIED = "applied"
    ASSESSMENT = "assessment"
    INTERVIEWING = "interviewing"
    OFFER = "offer"
    ON_HOLD = "on_hold"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    WITHDRAWN = "withdrawn"
    EXPIRED = "expired"


class StatusGroup(Choice):
    NOT_APPLIED = "not_applied"
    ACTIVE = "active"  # "ongoing" applications
    CLOSED = "closed"


STATUS_GROUPS: dict[StatusGroup, set[str]] = {
    StatusGroup.NOT_APPLIED: {"discovered", "interested"},
    StatusGroup.ACTIVE: {"applied", "assessment", "interviewing", "offer", "on_hold"},
    StatusGroup.CLOSED: {"accepted", "rejected", "withdrawn", "expired"},
}


class Priority(Choice):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class JobType(Choice):
    INTERNSHIP = "internship"
    FULL_TIME = "full_time"
    PART_TIME = "part_time"
    CONTRACT = "contract"
    OTHER = "other"


class ProgressResult(Choice):
    PENDING = "pending"
    PASSED = "passed"
    FAILED = "failed"
    CANCELLED = "cancelled"


# Progress stage is free text; these are just suggestions for the UI dropdown.
SUGGESTED_STAGES = [
    "Online Assessment",
    "Phone Screen",
    "Technical Interview",
    "Managerial Interview",
    "HR Interview",
    "Offer",
]
