from tavily import TavilyClient
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


TRUSTED_DOMAINS = [
    "who.int",
    "cdc.gov",
    "nih.gov",
    "mayoclinic.org"
]


def search_sources(condition, question):

    query = f"{condition} {question}"

    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=5,
        include_domains=TRUSTED_DOMAINS
    )

    return response["results"]


# Testing
if __name__ == "__main__":

    results = search_sources(
        "COPD",
        "Can I exercise?"
    )

    for r in results:
        print("--------------------------------")
        print("TITLE:")
        print(r["title"])

        print("\nURL:")
        print(r["url"])

        print("\nCONTENT:")
        print(r["content"])