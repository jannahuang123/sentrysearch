"""Click-based CLI entry point."""

import click
from dotenv import load_dotenv

load_dotenv()


@click.group()
def cli():
    """Search dashcam footage using natural language queries."""


@cli.command()
@click.argument("path", type=click.Path(exists=True))
@click.option("--chunk-duration", default=30, help="Chunk duration in seconds.")
@click.option("--overlap", default=5, help="Overlap between chunks in seconds.")
def index(path, chunk_duration, overlap):
    """Index video files from PATH for searching."""
    import os
    from .chunker import chunk_video, scan_directory
    from .embedder import embed_chunks
    from .store import SentryStore

    if os.path.isdir(path):
        videos = scan_directory(path)
    else:
        videos = [path]

    click.echo(f"Found {len(videos)} video(s) to index.")
    store = SentryStore()

    for video_path in videos:
        abs_path = str(os.path.abspath(video_path))
        if store.is_indexed(abs_path):
            click.echo(f"Skipping {video_path} (already indexed).")
            continue
        click.echo(f"Processing {video_path}...")
        chunks = chunk_video(video_path, chunk_duration=chunk_duration, overlap=overlap)
        click.echo(f"  Created {len(chunks)} chunk(s).")
        embedded = embed_chunks(chunks)
        store.add_chunks(embedded)
        click.echo(f"  Indexed {len(embedded)} chunk(s).")

    stats = store.get_stats()
    click.echo(f"Done. {stats['total_chunks']} chunks from {stats['unique_source_files']} file(s) in store.")


@cli.command()
@click.argument("query")
@click.option("-n", "--num-results", default=5, help="Number of results to return.")
@click.option("--trim-top", type=click.Path(), default=None,
              help="If set, trim the top result and save to this directory.")
def search(query, num_results, trim_top):
    """Search indexed footage with a natural language QUERY."""
    from .search import search_footage
    from .store import SentryStore

    store = SentryStore()
    results = search_footage(query, store, n_results=num_results)
    if not results:
        click.echo("No results found.")
        return

    for i, result in enumerate(results, 1):
        click.echo(f"\n--- Result {i} ---")
        click.echo(f"  Source: {result['source_file']}")
        click.echo(f"  Time:  {result['start_time']:.1f}s - {result['end_time']:.1f}s")
        click.echo(f"  Score: {result['similarity_score']:.4f}")

    if trim_top:
        from .trimmer import trim_top_result
        clip_path = trim_top_result(results, trim_top)
        click.echo(f"\nTrimmed top result to {clip_path}")


@cli.command()
@click.argument("video", type=click.Path(exists=True))
@click.option("--start", required=True, type=float, help="Start time in seconds.")
@click.option("--end", required=True, type=float, help="End time in seconds.")
@click.option("-o", "--output", required=True, type=click.Path(), help="Output file path.")
@click.option("--padding", default=2.0, help="Extra seconds before/after the clip.")
def trim(video, start, end, output, padding):
    """Trim a clip from VIDEO between --start and --end seconds."""
    from .trimmer import trim_clip

    out = trim_clip(video, start, end, output, padding=padding)
    click.echo(f"Saved clip to {out}")
