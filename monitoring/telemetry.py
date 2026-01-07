import time
import uuid
from datetime import datetime

def start_trace(endpoint: str):
    return {
        "request_id": str(uuid.uuid4()),
        "endpoint": endpoint,
        "start_time": time.time(),
        "timestamp": datetime.utcnow().isoformat()
    }

def end_trace(trace, versions, rules_applied):
    trace["latency_ms"] = int((time.time() - trace["start_time"]) * 1000)
    trace["versions"] = versions
    trace["rules_applied"] = rules_applied
    log_trace(trace)

def log_trace(trace):
    print("[TELEMETRY]", trace)
