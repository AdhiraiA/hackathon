from search import search_sources
from evidence import extract_evidence
from recommendation import generate_recommendation
from explain import generate_explanation


def run_agent(condition, question):

    print("Searching trusted medical sources...")

    # Step 1: Search articles
    search_results = search_sources(
        condition,
        question
    )

    print("Extracting medical evidence...")

    # Step 2: Extract evidence
    evidence = extract_evidence(
        search_results
    )

    print("Generating recommendation...")

    # Step 3: Generate recommendation
    recommendation = generate_recommendation(
        condition,
        question,
        evidence
    )

    print("Generating explanation...")

    # Step 4: Explain reasoning
    explanation = generate_explanation(
        recommendation,
        evidence
    )

    return {

        "condition": condition,

        "question": question,

        "recommendation": recommendation,

        "explanation": explanation,

        "evidence": evidence

    }
if __name__ == "__main__":

    result = run_agent(
        "COPD",
        "Can I exercise?"
    )

    print("\n========== RESULT ==========\n")

    print("Recommendation:")
    print(result["recommendation"]["recommendation"])

    print("\nConfidence:")
    print(result["recommendation"]["confidence"])

    print("\nExplanation:")
    print(result["explanation"])

    print("\nSources:")

    unique_sources = sorted(
        {item["source"] for item in result["evidence"]}
    )

    for source in unique_sources:
        print(source)