"""
Slugify is a simple string formatter to make strings URL safe.
"""

import re


# pylint: disable=C0103
def Slugger(value):
    """
    Slugger is a simple string formatter to make strings URL safe.
    the uppercase S indicates that the original case should be preserved.
    """
    # Remove leading/trailing whitespaces
    value = value.strip()
    # Replace spaces with hyphens
    value = re.sub(r"\s+", "-", value)
    # Remove characters that are not alphanumeric or hyphen
    value = re.sub(r"[^a-zA-Z0-9-]", "", value)
    # Convert to lowercase and preserve the original case
    slug = "".join(c.lower() if not c.isupper() else c for c in value)
    return slug


def slugger(value):
    """
    Slugger is a simple string formatter to make strings URL safe.
    the lowercase S indicates that the original case should not be preserved.
    """
    # Remove leading/trailing whitespaces
    value = value.strip()
    # Replace spaces with hyphens
    value = re.sub(r"\s+", "-", value)
    # Remove characters that are not alphanumeric or hyphen
    value = re.sub(r"[^a-zA-Z0-9-]", "", value)
    # Convert to lowercase and preserve the original case
    slug = "".join(c.lower() if c.isupper() else c for c in value)
    return slug
