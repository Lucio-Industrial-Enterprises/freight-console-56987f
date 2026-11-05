"""Shipping rate calculations."""

_ZONE_BASES = {"local": 5.0, "regional": 8.0}
_SERVICE_SURCHARGE = {"standard": 0.0, "express": 7.0}


def shipping_quote(weight_kg: float, zone: str, service: str = "standard") -> float:
    """Quote shipping in dollars.

    Args:
        weight_kg: Parcel weight; must be positive.
        zone: Delivery zone.
        service: Service level - standard (default) or express.
            Express adds a flat $7 surcharge on top of the standard rate.

    Returns:
        Total shipping cost in dollars, rounded to two decimal places.

    Raises:
        ValueError: If weight_kg is not positive, zone is unknown, or
            service is unknown.
    """
    if weight_kg <= 0:
        raise ValueError("weight must be positive")
    if zone not in _ZONE_BASES:
        raise ValueError("unknown zone")
    if service not in _SERVICE_SURCHARGE:
        raise ValueError("unknown service")
    base = _ZONE_BASES[zone]
    surcharge = _SERVICE_SURCHARGE[service]
    return round(base + 1.5 * weight_kg + surcharge, 2)
