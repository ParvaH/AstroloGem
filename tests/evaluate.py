import yaml
from rag.generator import generate_response

def load_tests():
    with open("tests/golden_cases.yaml", "r") as f:
        return yaml.safe_load(f)

def run_evaluation():
    failures = []

    for test in load_tests():
        response = generate_response(test["input"])

        expected = test["expected"]

        if set(response["rules_applied"]) != set(expected["rules_applied"]):
            failures.append(
                (test["id"], "Rules applied mismatch")
            )

        if response["confidence"] != expected["confidence"]:
            failures.append(
                (test["id"], "Confidence mismatch")
            )

        if expected["uncertainty_allowed"] is False:
            if "not defined" in response["answer"].lower():
                failures.append(
                    (test["id"], "Unexpected uncertainty")
                )

    return failures

if __name__ == "__main__":
    results = run_evaluation()
    if results:
        print("❌ Evaluation failed:")
        for r in results:
            print("-", r)
        exit(1)
    else:
        print("✅ All evaluations passed")
