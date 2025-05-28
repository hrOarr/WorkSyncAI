from plyer import notification

def show_notification(title: str, message: str, timeout: int = 5):
    """
    Display a popup notification on the screen.

    :param title: Title of the notification
    :param message: Message body of the notification
    :param timeout: Duration in seconds before the popup disappears
    """
    notification.notify(
        title=title,
        message=message,
        timeout=timeout
    )