"""Functions to manage a users shopping cart items."""
from collections import Counter
from typing import Iterable


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    return Counter(current_cart) + Counter(items_to_add)


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    return Counter(notes)


def update_recipes(ideas: dict, recipe_updates: Iterable):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    for update in recipe_updates:
        ideas.update({update[0]: update[1]})
    return ideas


def sort_entries(cart: dict):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart: dict, aisle_mapping: dict[str, list]):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    order_dict = {}
    for key, value in cart.items():
        order_dict[key] = aisle_mapping[key]
        order_dict[key].insert(0, value)
    return dict(sorted(order_dict.items(), reverse=True))


def update_store_inventory(fulfillment_cart: dict[str, list], store_inventory: dict[str, list]):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    for key, value in fulfillment_cart.items():
        if store_inventory[key][0] <= value[0]:
            store_inventory[key][0] = 'Out of Stock'
        else:
            store_inventory[key][0] -= value[0]
    return store_inventory
