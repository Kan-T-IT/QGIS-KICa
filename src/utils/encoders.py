"""Custom JSON encoders for the application."""

import json
from decimal import Decimal


class CustomJsonDecimalEncoder(json.JSONEncoder):
    """Custom JSON encoder for Decimal objects."""

    def default(self, o):
        """Encode Decimal objects as float."""

        if isinstance(o, Decimal):
            return float(o)
        return super().default(o)
