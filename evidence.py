MEDICAL_KEYWORDS = [
    "exercise",
    "physical activity",
    "rehabilitation",
    "breathing",
    "lung",
    "copd",
    "symptoms",
    "quality of life",
    "patients"
]


def extract_evidence(search_results):

    all_evidence = []

    for result in search_results:

        source = result["url"]

        content = result["content"]

        text_lower = content.lower()

        if any(keyword in text_lower for keyword in MEDICAL_KEYWORDS):

            all_evidence.append(
                {
                    "source": source,
                    "url": result["url"],
                    "evidence": content
                }
            )

    return all_evidence


if __name__ == "__main__":

    from search import search_sources

    results = search_sources(
        "COPD",
        "Can I exercise?"
    )

    evidence = extract_evidence(results)

    for item in evidence:

        print("--------------------------------")
        print("Source:", item["source"])
        print("Evidence:", item["evidence"])