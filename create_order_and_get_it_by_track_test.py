import data
import sender_stand_request


def test_success_create_order():
    order_response = sender_stand_request.create_order(data.order_body)
    assert order_response.status_code == 201

    track_number = order_response.json()["track"]

    get_order_response = sender_stand_request.get_order_by_track(track_number)
    assert get_order_response.status_code == 200
