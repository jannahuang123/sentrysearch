"""Query and retrieval logic."""

from .embedder import embed_query
from .store import SentryStore


def search_footage(
    query: str,
    store: SentryStore,
    n_results: int = 5,
) -> list[dict]:
    """Search indexed footage with a natural language query.

    Args:
        query: Natural language search string.
        store: SentryStore instance to search against.
        n_results: Maximum number of results to return.

    Returns:
        List of result dicts sorted by relevance (best first).
        Each dict contains: source_file, start_time, end_time, similarity_score.
    """
    query_embedding = embed_query(query)
    hits = store.search(query_embedding, n_results=n_results)

    results = []
    for hit in hits:
        results.append({
            "source_file": hit["source_file"],
            "start_time": hit["start_time"],
            "end_time": hit["end_time"],
            "similarity_score": hit["score"],
        })

    # Already sorted by ChromaDB (lowest distance first = highest score first),
    # but enforce the contract explicitly.
    results.sort(key=lambda r: r["similarity_score"], reverse=True)
    return results
