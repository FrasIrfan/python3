import time 
from plyer import notification


def send_reminder(reminder_text):
    notification.notify(
        title="Reminder",
        message=reminder_text,
        # Notification will automatically close after 10 seconds
        app_name="Reminder App", timeout=10
    )


def main():
    while True:
        current_hour = int(time.strftime("%H"))

        if current_hour % 1 == 0:
            send_reminder("Chase Your Dreams")

        # Wait for 1 hour (3600 seconds) before checking again
        time.sleep(3600)


if __name__ == "__main__":
    main()
