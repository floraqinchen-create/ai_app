# Skeleton: fetch core papers via PASA-Agent
import json
from pathlib import Path
import argparse

OUTPUT_DIR = Path("research_data/core_papers")

def fetch_core_papers(query, max_results=20):
    """
    Placeholder function to fetch core papers via PASA-Agent.
    Replace the TODO section with actual PASA-Agent API calls or CLI invocation.
    Saves metadata to research_data/core_papers/papers.json and returns the list.
    """
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    # TODO: implement actual PASA-Agent call
    print(f"[pasa_agent] Placeholder fetching papers for query: {query}")
    results = []
    # Example structure for each paper
    # results.append({"title": "Title", "authors": ["A"], "year": 2024, "doi": "...", "abstract": "...", "pdf": "raw_pdfs/1.pdf"})
    (OUTPUT_DIR / "papers.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", required=True)
    parser.add_argument("--max", type=int, default=20)
    args = parser.parse_args()
    fetch_core_papers(args.query, max_results=args.max)