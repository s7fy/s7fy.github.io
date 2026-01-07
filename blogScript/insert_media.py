import argparse
import shutil
import re
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="Insert media into article"
    )

    parser.add_argument("article_name", help="Target article name")

    subparsers = parser.add_subparsers(
        dest="mode",
        required=True
    )

    # picture
    pic = subparsers.add_parser("picture", help="Insert picture")
    pic.add_argument("picture_name", help="Picture file name")
    pic.add_argument("-l", "--line", type=int, required=True)

    # callout
    callout = subparsers.add_parser("callout", help="Insert callout")
    callout.add_argument(
        "callout_type",
        choices=["alert", "warning", "tip"],
        help="Callout type"
    )
    callout.add_argument("-l", "--line", type=int, required=True)

    # youtube
    yt = subparsers.add_parser("youtube", help="Insert YouTube embed")
    yt.add_argument("url", help="YouTube URL")
    yt.add_argument("-l", "--line", type=int, required=True)

    # tweet
    tw = subparsers.add_parser("tweet", help="Insert tweet embed")
    tw.add_argument("url", help="Tweet URL")
    tw.add_argument("-l", "--line", type=int, required=True)

    args = parser.parse_args()
    handle(args)


def handle(args):
    article_path = resolve_article(args.article_name)

    insert_text = build_insert_text(args)
    new_content = insert_at_line(article_path, insert_text, args.line)

    safe_write(article_path, new_content)

    print(f"Inserted {args.mode} into {article_path} at line {args.line}")


# --------------- #
# Core functions  # 
# --------------- #

def resolve_article(article_name: str) -> Path:
    candidates = [
        Path(f"/Users/s7fy/blog/content/posts/{article_name}/index.md")
    ]
    for p in candidates:
        if p.exists():
            return p
    raise FileNotFoundError("Article not found")


def insert_at_line(path: Path, insert_text: str, line_no: int) -> str:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)

    if line_no < 1 or line_no > len(lines) + 1:
        raise ValueError("line number out of range")

    lines.insert(line_no - 1, insert_text + "\n")
    return "".join(lines)


def safe_write(path: Path, new_content: str):
    backup = path.with_suffix(path.suffix + ".bak")
    tmp = path.with_suffix(path.suffix + ".tmp")

    shutil.copy2(path, backup)
    tmp.write_text(new_content, encoding="utf-8")
    tmp.replace(path)


def build_insert_text(args) -> str:
    if args.mode == "picture":
        return f'{{{{< figure src="{args.picture_name}" title="">}}}}'

    if args.mode == "callout":
        return f'{{{{< callout type="{args.callout_type}" text="">}}}}\n' # {{< callout type="alert" text="" >}}


    if args.mode == "youtube":
        video_id = extract_youtube_id(args.url)
        return f'{{{{< youtube {video_id} >}}}}' # https://www.youtube.com/watch?v=w7Ft2ymGmfc → w7Ft2ymGmfc

    if args.mode == "tweet":
        tweet_id = extract_tweet_id(args.url)
        return f'{{{{< tweet {tweet_id} >}}}}' # https://x.com/GoHugoIO/status/877500564405444608 → user="GoHugoIO" id="877500564405444608"

    raise ValueError("Unknown mode")


def extract_youtube_id(url: str) -> str:

    m = re.search(r"v=([^&]+)", url)
    if m:
        return m.group(1)
    raise ValueError("Invalid YouTube URL")

def extract_tweet_id(url: str) -> str:
    m = re.search(r"https://x\.com/([^/]+)/status/([0-9]+)", url)
    if m:
        user = f'user="{m.group(1)}"'
        tweet_id = f'id="{m.group(2)}"'
        tweet = f"{user} {tweet_id}"
        return tweet

    raise ValueError("Invalid tweet URL")




if __name__ == "__main__":
    main()
