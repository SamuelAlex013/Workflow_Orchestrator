"""
Single runner to refresh the RAG knowledge base.

What it does:
1) Re-extract chunks from source docs (2_extract_content.py)
2) Rebuild FAISS vector store (4_build_vector_store.py)
3) Optionally run a retrieval smoke test

Usage examples:
    python refresh_kb.py
    python refresh_kb.py --test --query "telegram trigger to database"
    python refresh_kb.py --skip-extract --test
"""

from __future__ import annotations

import argparse
import importlib.util
import sys
import time
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
EXTRACT_SCRIPT = SCRIPT_DIR / "2_extract_content.py"
BUILD_SCRIPT = SCRIPT_DIR / "4_build_vector_store.py"


def _load_module(module_path: Path, module_name: str):
    """Load a Python module from file path (works for filenames starting with digits)."""
    spec = importlib.util.spec_from_file_location(module_name, str(module_path))
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load module from {module_path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def refresh_knowledge_base(
    *,
    skip_extract: bool,
    skip_build: bool,
    reset_index: bool,
    run_test: bool,
    test_query: str,
) -> int:
    start = time.time()

    print("=" * 70)
    print("🔄 Refreshing RAG Knowledge Base")
    print("=" * 70)

    # Step 1: Extract chunks
    if not skip_extract:
        print("\n[1/2] Running chunk extraction...")
        extract_module = _load_module(EXTRACT_SCRIPT, "extract_content_module")
        extract_module.main()
        print("✅ Chunk extraction complete")
    else:
        print("\n[1/2] Skipped chunk extraction (--skip-extract)")

    # Step 2: Build vector store
    index = metadata_list = text_list = model = None
    if not skip_build:
        print("\n[2/2] Building vector store...")
        build_module = _load_module(BUILD_SCRIPT, "build_vector_store_module")
        index, metadata_list, text_list, model = build_module.build_vector_store(reset=reset_index)
        print("✅ Vector store build complete")

        if run_test:
            print("\n🧪 Running retrieval smoke test...")
            build_module.test_retrieval(
                index,
                metadata_list,
                text_list,
                model,
                query=test_query,
                top_k=3,
            )
            print("✅ Smoke test complete")
    else:
        print("\n[2/2] Skipped vector store build (--skip-build)")

    duration = time.time() - start
    print("\n" + "=" * 70)
    print("✅ Knowledge base refresh finished")
    print(f"⏱️  Duration: {duration:.1f}s")
    print("=" * 70)

    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Single runner to refresh RAG knowledge base")
    parser.add_argument("--skip-extract", action="store_true", help="Skip 2_extract_content step")
    parser.add_argument("--skip-build", action="store_true", help="Skip 4_build_vector_store step")
    parser.add_argument("--no-reset", action="store_true", help="Do not reset index before build")
    parser.add_argument("--test", action="store_true", help="Run retrieval smoke test after build")
    parser.add_argument(
        "--query",
        type=str,
        default="telegram trigger to database",
        help="Query for smoke test",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    return refresh_knowledge_base(
        skip_extract=args.skip_extract,
        skip_build=args.skip_build,
        reset_index=not args.no_reset,
        run_test=args.test,
        test_query=args.query,
    )


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("\n⚠️  Cancelled by user")
        raise SystemExit(130)
    except Exception as exc:
        print(f"\n❌ Failed to refresh knowledge base: {exc}")
        raise SystemExit(1)
