import os
import re

BASE_DIR = "research/linkedin-posts"


def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name)


def clean_post(text):
    # Remove excessive blank lines
    text = re.sub(r"\n\s*\n", "\n\n", text)

    # Trim spaces
    text = text.strip()

    return text


def save_post(author, url, content, index):
    safe_author = author.lower().replace(" ", "_")
    folder = os.path.join(BASE_DIR, safe_author)
    os.makedirs(folder, exist_ok=True)

    filename = f"post_{index}.md"
    filepath = os.path.join(folder, filename)

    cleaned = clean_post(content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# LinkedIn Post\n\n")
        f.write(f"**Author:** {author}\n")
        f.write(f"**Source:** {url}\n\n")
        f.write(f"---\n\n")
        f.write(cleaned)

    print(f"✅ Saved: {filepath}")


def main():
    print("=== LinkedIn Post Collector ===")

    while True:
        author = input("\nEnter expert name (or 'exit'): ").strip()
        if author.lower() == "exit":
            break

        print("\nPaste LinkedIn posts (type 'done' when finished)\n")

        index = 1

        while True:
            url = input("Post URL: ").strip()
            if url.lower() == "done":
                break

            print("Paste post content (type 'END' on a new line when finished):")

            lines = []
            while True:
                line = input()
                if line.strip() == "END":
                    break
                lines.append(line)

            content = "\n".join(lines)

            save_post(author, url, content, index)
            index += 1


if __name__ == "__main__":
    main()