# Sport scoring configurations.
# Increment button order within each sport = display order on the control page.
# Move items up to make them more prominent. Top-level list order = sport selector order.

SPORTS = [
    {
        "name": "Basketball",
        "slug": "basketball",
        "increments": [
            {"label": "+2", "value": 2},
            {"label": "+3", "value": 3},
            {"label": "+1", "value": 1},
        ],
    },
    {
        "name": "Football",
        "slug": "football",
        "increments": [
            {"label": "TD +6", "value": 6},
            {"label": "FG +3", "value": 3},
            {"label": "PAT +1", "value": 1},
            {"label": "SFTY +2", "value": 2},
        ],
    },
    {
        "name": "Hockey",
        "slug": "hockey",
        "increments": [
            {"label": "+1", "value": 1},
        ],
    },
    {
        "name": "Soccer",
        "slug": "soccer",
        "increments": [
            {"label": "+1", "value": 1},
        ],
    },
    {
        "name": "Volleyball",
        "slug": "volleyball",
        "increments": [
            {"label": "+1", "value": 1},
        ],
    },
]

# Build a lookup dict for the view
SPORTS_BY_SLUG = {s["slug"]: s for s in SPORTS}
