import requests
import configuration
import data


def create_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order_body
                         )


response = create_order(data.order_body)
track = response.json().get("track")


def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
                        params={"t": track}
                        )


response = get_order_by_track(data.order_body)
