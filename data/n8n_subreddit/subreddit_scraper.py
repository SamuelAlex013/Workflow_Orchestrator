import praw
import json
import re
import sys
from datetime import datetime, timedelta

# ==========================================
# CONFIGURATION (EDIT THIS SECTION ONLY)
# ==========================================
REDDIT_CLIENT_ID = "YOUR_CLIENT_ID"
REDDIT_CLIENT_SECRET = "YOUR_CLIENT_SECRET"
REDDIT_USER_AGENT = "python:final_scraper:v1.3 (by /u/YOUR_USERNAME)"
TARGET_SUBREDDIT = "n8n"
# ==========================================


def get_reddit_instance():
    return praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT,
    )


def is_noise(text):
    """Checks for Deleted, Removed, or URL-heavy comments."""
    if not text:
        return True
    text = text.strip()
    if text in ["[deleted]", "[removed]"]:
        return True

    # URL Density Check
    url_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    urls = re.findall(url_pattern, text)
    total_url_len = sum(len(u) for u in urls)

    if len(text) > 0 and (total_url_len / len(text)) > 0.50:
        return True
    return False


def scrape_subreddit():
    saved = 0
    skipped = 0
    reddit = get_reddit_instance()
    subreddit = reddit.subreddit(TARGET_SUBREDDIT)

    # Calculate cutoff
    one_year_ago = datetime.now() - timedelta(days=365)
    cutoff_timestamp = one_year_ago.timestamp()

    filename = f"{TARGET_SUBREDDIT}.jsonl"

    print(f"\n[INIT] Starting High-Velocity Scrape for r/{TARGET_SUBREDDIT}")
    print(f"[INIT] Output File: {filename}")
    print(f"[INIT] Time Window: 1 Year")
    print("-" * 60)

    # Open file in append mode
    with open(filename, "a", encoding="utf-8") as f:
        for submission in subreddit.new(limit=None):
            # Clean title for printing (remove newlines, truncate)
            display_title = submission.title.replace("\n", " ")[:50] + "..."

            # 1. TIME CHECK
            if submission.created_utc < cutoff_timestamp:
                print(f"[STOP]  Reached Time Limit at: {submission.created_utc}")
                break

            # 2. MEDIA CHECK (Strict Text Only)
            if not submission.is_self or getattr(submission, "is_video", False):
                print(f"[SKIP : {skipped}]  [MEDIA] {display_title}")
                skipped += 1
                continue

            # 3. COMMENT PROCESSING
            try:
                submission.comments.replace_more(limit=0)
                all_comments = submission.comments.list()
                all_comments.sort(key=lambda x: x.score, reverse=True)

                clean_comments = []
                for comment in all_comments:
                    if len(clean_comments) >= 5:
                        break

                    author = comment.author.name if comment.author else "[deleted]"
                    if author.lower() == "automoderator":
                        continue

                    body = comment.body.strip()
                    if is_noise(body):
                        continue

                    clean_comments.append(body)

                # 4. DATA CONSTRUCTION
                # We merge Title + Body into "post_text" so we don't lose the question context
                # but we REMOVE the "title" key as requested.
                full_text_content = (
                    f"{submission.title}\n\n{submission.selftext}".strip()
                )

                post_data = {"post_text": full_text_content, "comments": clean_comments}

                # 5. WRITE & FLUSH
                json.dump(post_data, f, ensure_ascii=False)
                f.write("\n")
                f.flush()

                # 6. TERMINAL FEEDBACK
                print(
                    f"[SAVE : {saved}]  [{len(clean_comments)} Cmnts] {display_title}"
                )
                saved += 1

            except Exception as e:
                print(f"[ERR]   {e}")
                continue

    print("-" * 60)
    print(f"[DONE] Scrape Complete. Saved: {saved}, Skipped: {skipped}")
    print(f"Total Posts Processed: {saved + skipped}\n")


if __name__ == "__main__":
    scrape_subreddit()
