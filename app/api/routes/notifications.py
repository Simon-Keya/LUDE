from fastapi import APIRouter, HTTPException, status
from ..models.notifications import Notification
from ..services.notifications import (
    get_all_notifications,
    get_notification_by_id,
    mark_notification_as_read,
    mark_all_notifications_as_read,
)


router = APIRouter(tags=["notifications"])


@router.get("/")
async def get_all_notifications():
    return await get_all_notifications()


@router.get("/{notification_id}")
async def get_notification_by_id(notification_id: int):
    notification = await get_notification_by_id(notification_id)
    if not notification:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return notification


@router.put("/{notification_id}/mark-as-read")
async def mark_notification_as_read(notification_id: int):
    notification = await get_notification_by_id(notification_id)
    if not notification:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    notification.read = True
    notification.update_timestamps()
    await notification.save()

    return notification


@router.put("/mark-all-as-read")
async def mark_all_notifications_as_read():
    for notification in Notification.query.all():
        notification.read = True
        notification.update_timestamps()
        await notification.save()

    return None


status.HTTP_404_NOT_FOUND = 404
