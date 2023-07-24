from ..models.notifications import Notification


async def get_all_notifications():
    notifications = []

    for notification in Notification.query.all():
        notifications.append(notification)

    return notifications


async def get_notification_by_id(notification_id: int):
    return await Notification.query.get(notification_id)


async def mark_notification_as_read(notification_id: int):
    notification = await get_notification_by_id(notification_id)
    notification.read = True
    notification.update_timestamps()
    await notification.save()


async def mark_all_notifications_as_read():
    for notification in Notification.query.all():
        notification.read = True
        notification.update_timestamps()
        await notification.save()
