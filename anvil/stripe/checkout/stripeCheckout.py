def charge(amount, currency, title=None, description=None, icon_url=None, billing_address=None, shipping_address=None,
           zipcode=None):
    """Charge the user for a one-off payment, by showing a Stripe checkout form. Returns a dictionary of information
    about the transaction on success. """
    pass


def get_token(amount, currency, title=None, description=None, icon_url=None, billing_address=None, zipcode=None,
              raw=None):
    """Show the Stripe checkout form, and return a raw (token, user_details) tuple.The token can be used to place
    charges from server modules. The user_details are a dictionary of user-supplied data (eg ‘email’).‘amount’ is a
    number, in least units of currency (eg cents or pennies).‘currency’ is a three-letter currency code (eg
    ‘USD’).‘title’ and ‘description’ configure the checkout dialog.Setting ‘zipcode’ to True requires the user to
    enter their postal code.Setting ‘billing_address’ to True requires the user to entier a billing address.Setting
    ‘raw’ to True returns a token for your own API key, which is only useful if you are using the Stripe API
    directly. If you do this, you cannot use this token with the Anvil Stripe APIs. """
    pass
