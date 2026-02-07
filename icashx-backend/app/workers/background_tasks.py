import os
import time
import logging
import threading
from datetime import datetime, timedelta
from pathlib import Path
from app.services.property_api import get_property_details, get_comparables
from app.services.notification_service import send_notification


# ==================================================
# CONFIGURATION
# ==================================================
LOG_FILE = Path("/tmp/background_tasks.log")
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
)

CACHE_REFRESH_INTERVAL = 60 * 60 * 6  # every 6 hours


# ==================================================
# GENERIC THREAD LAUNCHER
# ==================================================
def run_in_background(target, *args, **kwargs):
    """Run a function asynchronously in a lightweight thread."""
    thread = threading.Thread(target=target, args=args, kwargs=kwargs, daemon=True)
    thread.start()
    return thread


# ==================================================
# TASKS
# ==================================================
def refresh_property_cache(address_list: list[str]):
    """
    Periodically pre‑cache property data for known addresses using property_api.
    Useful for popular or frequently analyzed listings.
    """
    logging.info(f"Starting cache refresh task for {len(address_list)} properties…")

    for address in address_list:
        try:
            details = get_property_details(address)
            # Optional: if Zillow ID known, fetch comparables too.
            get_comparables(str(details.get("zpid", address)))
            logging.info(f"Cached property data for: {address}")
        except Exception as e:
            logging.error(f"Failed to refresh cache for {address}: {e}")

    logging.info("Cache refresh task completed.")


def schedule_cache_refresh(addresses: list[str], interval: int = CACHE_REFRESH_INTERVAL):
    """Runs refresh_property_cache() in a loop at a fixed interval."""
    def loop_task():
        while True:
            refresh_property_cache(addresses)
            time.sleep(interval)

    run_in_background(loop_task)
    logging.info("Scheduled recurring property cache refresh.")


def send_async_notification(to_email: str | None, to_phone: str | None, subject: str, message: str, attachment_path: str | None = None):
    """
    Sends an email or SMS in the background so API responses return instantly.
    """
    def _task():
        try:
            send_notification(to_email, to_phone, subject, message, attachment_path)
            logging.info(f"Notification sent to: {to_email or to_phone}")
        except Exception as e:
            logging.error(f"Error sending notification: {e}")

    run_in_background(_task)


def cleanup_old_logs(days: int = 3):
    """Deletes background task logs older than 'days' days."""
    if LOG_FILE.exists():
        file_mod_time = datetime.fromtimestamp(LOG_FILE.stat().st_mtime)
        if datetime.now() - file_mod_time > timedelta(days=days):
            try:
                LOG_FILE.unlink()
                logging.info("Old log file cleaned up.")
            except Exception as e:
                logging.error(f"Error cleaning logs: {e}")