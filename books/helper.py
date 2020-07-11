def get_email_message(order):
    return f'USER {order.client.username}, PHONE: {order.call}, ordered BOOK ' \
           f'{order.book.name}(id: {order.book.id}). at {order.created} ' \
           f'Order id: {order.id}.'
