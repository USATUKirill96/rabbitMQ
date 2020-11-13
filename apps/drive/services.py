from apps.drive.models import DriveOrder


def create_order(data):
    DriveOrder.objects.create(
        order_id=data["id"],
        delivery_at=data["delivery_at"]
    )
