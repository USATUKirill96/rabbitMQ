from .models import TabletOrder


def create_order(data):
    TabletOrder.objects.create(
        name=data["name"],
        quantity=data["quantity"],
        delivery_at=data["delivery_at"],
        order_id=data["id"]
    )
