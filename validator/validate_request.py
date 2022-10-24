schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["name", "username", "age"],
        "properties": {
            "name": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
            },
            "username": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "age": {
                "bsonType": "int",
                "description": "must be a int if the field exists"
            }
        }
    }
}
