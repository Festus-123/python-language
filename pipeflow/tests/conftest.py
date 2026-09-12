# tests/conftest.py
import pytest


@pytest.fixture
def sample_log_records() -> list[dict]:
    """Reusable fixture providing sample log dictionaries."""
    return [
        {
            "timestamp": "2026-09-12T16:00:00",
            "level": "ERROR",
            "service": "auth_service",
            "user_id": 101,
            "message": "Authentication failed",
            "latency_ms": 120,
        },
        {
            "timestamp": "2026-09-12T16:01:00",
            "level": "INFO",
            "service": "payment_service",
            "user_id": 202,
            "message": "Payment processed",
            "latency_ms": 45,
        },
        {
            "timestamp": "2026-09-12T16:02:00",
            "level": "ERROR",
            "service": "user_service",
            "user_id": 303,
            "message": "Timeout occurred",
            "latency_ms": 4500,
        },
    ]