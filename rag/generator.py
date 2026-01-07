from rag.retriever import retrieve_rules
from rag.rule_engine import apply_rules
from rag.prompt_builder import build_prompt
from versions.resolver import get_active_versions
from monitoring.telemetry import start_trace, end_trace

def generate_response(input_data, endpoint="/analyze-chart"):
    trace = start_trace(endpoint)

    versions = get_active_versions()

    rules = retrieve_rules(
        query=str(input_data),
        corpus_version=versions["corpus"]
    )

    applied = apply_rules(rules)

    prompt = build_prompt(
        context=applied,
        prompt_version=versions["prompt"]
    )

    # (LLM call mocked for now)
    answer = "Generated response based on strict rules"

    response = {
        "answer": answer,
        "rules_applied": applied["rules_applied"],
        "confidence": "Medium",
        "versions": versions
    }

    end_trace(
        trace=trace,
        versions=versions,
        rules_applied=applied["rules_applied"]
    )

    return response
