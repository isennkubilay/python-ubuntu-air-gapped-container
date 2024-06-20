from pymongo import MongoClient

def check_mongo_connection():
    # Replace the connection string with your MongoDB connection string
    # Example connection string: "mongodb://username:password@localhost:27017/mydatabase"
    mongo_uri = "mongodb://root:12345@192.168.1.1:32510/admin"

    try:
        # Attempt to connect to MongoDB
        client = MongoClient(mongo_uri)

        # Check if the connection is successful
        db = client.get_database()
        print("MongoDB connection successful!")

        # Optionally, you can perform additional operations here

    except Exception as e:
        print(f"Unable to connect to MongoDB: {e}")

    finally:
        # Close the connection (even if unsuccessful)
        if client:
            client.close()

if __name__ == "__main__":
    check_mongo_connection()
