import yt_dlp
import os
import re
import requests
from dotenv import load_dotenv

# ==============================
# CONFIG
# ==============================
BASE_DIR = "research/youtube-transcripts"

load_dotenv()
API_KEY = os.getenv("SUPADATA_API_KEY")


# ==============================
# UTIL FUNCTIONS
# ==============================
def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name)


def extract_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    return None


def get_video_info(video_url):
    with yt_dlp.YoutubeDL({"quiet": True}) as ydl:
        info = ydl.extract_info(video_url, download=False)
        return info.get("id"), info.get("title")


def transcript_exists(folder, video_id):
    for file in os.listdir(folder):
        if video_id in file and file.endswith(".txt"):
            return True
    return False


# ==============================
# YT-DLP METHOD
# ==============================
def download_transcript_yt_dlp(video_url, author_name):
    safe_author = author_name.lower().replace(" ", "_")
    output_dir = os.path.join(BASE_DIR, safe_author)
    os.makedirs(output_dir, exist_ok=True)

    video_id, title = get_video_info(video_url)

    if not video_id:
        print("❌ Could not fetch video info")
        return

    safe_title = sanitize_filename(title)

    if transcript_exists(output_dir, video_id):
        print(f"⏩ Skipping (already exists): {safe_title}")
        return

    print(f"⬇️ Downloading (yt-dlp): {safe_title}")

    ydl_opts = {
        "skip_download": True,
        "writesubtitles": True,
        "writeautomaticsub": True,
        "subtitleslangs": ["en"],
        "subtitlesformat": "vtt",
        "outtmpl": os.path.join(output_dir, f"{safe_title}_{video_id}.%(ext)s"),
        "quiet": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])


# ==============================
# CLEANING FUNCTIONS
# ==============================
def clean_vtt_with_timestamps(file_path):
    lines = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if line == "" or line.isdigit():
                continue

            line = re.sub(r"<.*?>", "", line)
            lines.append(line)

    return "\n".join(lines)


def clean_vtt(file_path):
    lines = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if "-->" in line or line == "" or line.isdigit():
                continue

            line = re.sub(r"<.*?>", "", line)
            lines.append(line)

    seen = set()
    unique_lines = []

    for line in lines:
        if line not in seen:
            seen.add(line)
            unique_lines.append(line)

    text = " ".join(unique_lines)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"(?<=[.!?])\s+", "\n\n", text)

    return text.strip()


def convert_vtt_in_folder(folder, author):
    for file in os.listdir(folder):
        if file.endswith(".vtt"):
            full_path = os.path.join(folder, file)

            base_name = file.replace(".vtt", "")

            raw_txt = os.path.join(folder, f"{base_name}_raw.txt")
            clean_txt = os.path.join(folder, f"{base_name}_clean.txt")

            if os.path.exists(clean_txt) and os.path.exists(raw_txt):
                continue

            raw_text = clean_vtt_with_timestamps(full_path)
            clean_text = clean_vtt(full_path)

            with open(raw_txt, "w", encoding="utf-8") as f:
                f.write(f"Author: {author}\n")
                f.write(f"Source File: {file}\n\n")
                f.write(raw_text)

            with open(clean_txt, "w", encoding="utf-8") as f:
                f.write(f"Author: {author}\n")
                f.write(f"Source File: {file}\n\n")
                f.write(clean_text)

            print(f"✅ Saved: {base_name}_raw.txt & _clean.txt")


# ==============================
# SUPADATA METHOD
# ==============================
def fetch_transcript_supadata(video_url):
    video_id = extract_video_id(video_url)

    if not video_id:
        print("❌ Invalid URL")
        return None

    url = f"https://api.supadata.ai/v1/youtube/transcript?videoId={video_id}"

    headers = {
        "x-api-key": API_KEY
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data.get("transcript", "")
    else:
        print("❌ API Error:", response.status_code)
        return None


def save_supadata_transcript(video_url, author_name):
    safe_author = author_name.lower().replace(" ", "_")
    folder = os.path.join(BASE_DIR, safe_author)
    os.makedirs(folder, exist_ok=True)

    video_id, title = get_video_info(video_url)
    safe_title = sanitize_filename(title)

    if transcript_exists(folder, video_id):
        print(f"⏩ Skipping (already exists): {safe_title}")
        return

    print(f"🌐 Fetching (API): {safe_title}")

    transcript = fetch_transcript_supadata(video_url)

    if not transcript:
        print("❌ No transcript from API")
        return

    base_name = f"{safe_title}_{video_id}"

    raw_file = os.path.join(folder, f"{base_name}_raw.txt")
    clean_file = os.path.join(folder, f"{base_name}_clean.txt")

    # RAW
    with open(raw_file, "w", encoding="utf-8") as f:
        f.write(f"Author: {author_name}\n")
        f.write(f"Source: {video_url}\n\n")
        f.write(transcript)

    # CLEAN
    clean_text = re.sub(r"\s+", " ", transcript)
    clean_text = re.sub(r"(?<=[.!?])\s+", "\n\n", clean_text)

    with open(clean_file, "w", encoding="utf-8") as f:
        f.write(f"Author: {author_name}\n")
        f.write(f"Source: {video_url}\n\n")
        f.write(clean_text)

    print(f"✅ Saved (API): {base_name}_raw.txt & _clean.txt")


# ==============================
# MAIN PROGRAM
# ==============================
def main():
    print("=== YouTube Transcript Scraper ===")

    mode = input("Choose method (1 = yt-dlp, 2 = Supadata API): ").strip()

    while True:
        author = input("\nEnter expert name (or type 'exit' to quit): ").strip()
        if author.lower() == "exit":
            break

        safe_author = author.lower().replace(" ", "_")
        author_folder = os.path.join(BASE_DIR, safe_author)
        os.makedirs(author_folder, exist_ok=True)

        print(f"\nInput YouTube links for {author}")
        print("Type 'done' when finished.\n")

        video_links = []

        while True:
            link = input("YouTube URL: ").strip()
            if link.lower() == "done":
                break
            if link:
                video_links.append(link)

        for url in video_links:
            if mode == "1":
                download_transcript_yt_dlp(url, author)
            elif mode == "2":
                save_supadata_transcript(url, author)

        if mode == "1":
            print(f"\n🧠 Processing transcripts for {author}...")
            convert_vtt_in_folder(author_folder, author)

        print(f"🎉 Done for {author}!\n")


if __name__ == "__main__":
    main()