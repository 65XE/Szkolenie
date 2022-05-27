from enum import IntEnum


class Status(IntEnum):
    PASSED = 0
    FAILURES = 1
    EXCEPTIONS = 2
    WARNINGS = 3
    SKIPPED = 4
    BLOCKED = 5
    WORKAROUNDS = 6
    TOTAL_FILES = 7


class CONSTANTS:
    __slots__ = ()
    PASSED = "Passed"
    FAILURES = "Failures"
    EXCEPTIONS = "Exceptions"
    WARNINGS = "Warnings"
    SKIPPED = "Skipped"
    BLOCKED = "Blocked"
    WORKAROUNDS = "Workarounds"

    PASSED_TAG = "<Passed>"
    FAILURES_TAG = "<Failures>"
    EXCEPTIONS_TAG = "<Exceptions>"
    WARNINGS_TAG = "<Warnings>"
    SKIPPED_TAG = "<Skipped>"
    BLOCKED_TAG = "<Blocked>"
    WORKAROUNDS_TAG = "<Workarounds>"
