import os
from dotenv import load_dotenv
from datetime import datetime, timezone
from supabase import create_client, Client
from sophons.utils.logger import logger

load_dotenv()

SUPABSE_URL = os.environ.get("SUPABSE_URL")
SUPABASE_ACCESS_KEY = os.environ.get("SUPABASE_ACCESS_KEY")


def add_row(
    user_id,
    posted_at,
    single_line_summary,
    full_summary,
    topic_name,
):
    url = SUPABSE_URL
    key = SUPABASE_ACCESS_KEY
    supabase = create_client(url, key)
    row = {
        "id": user_id,
        "prcoessed_at": datetime.now(timezone.utc).isoformat(),
        "posted_at": posted_at,
        "single_line": single_line_summary,
        "full_summary": full_summary,
        "topic": topic_name,
    }
    try:
        response = supabase.table("summary").upsert(row).execute()
        return response, True
    except Exception as e:
        logger.error(f"Error while upserting the data: {e}")
        return None, False
