# Define the new access levels
NEW_ACCESS_LEVELS = [
    {
        "name": f"{ACCESS_POLICY_NAME}/accessLevels/LEVEL_1",
        "title": "Level 1",
        "description": "Description for Level 1",
        "basic": {
            "conditions": [
                {
                    "ipSubnetworks": ["192.0.2.0/24"],
                    "requiredAccessLevels": []
                }
            ]
        }
    },
    {
        "name": f"{ACCESS_POLICY_NAME}/accessLevels/LEVEL_2",
        "title": "Level 2",
        "description": "Description for Level 2",
        "basic": {
            "conditions": [
                {
                    "ipSubnetworks": ["198.51.100.0/24"],
                    "requiredAccessLevels": []
                }
            ]
        }
    }
]