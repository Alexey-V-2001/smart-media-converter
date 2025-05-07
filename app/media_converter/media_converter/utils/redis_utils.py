import json
import redis
from django.conf import settings

class RedisClient:
    """
    Class for working with Redis.
    
    Provides a single point of interaction with Redis, encapsulating connection details
    and offering methods for typical operations within the project context.
    """
    
    def __init__(self):
        """Initialize the Redis connection based on settings in settings.py."""
        self.redis = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB,
            password=settings.REDIS_PASSWORD,
            decode_responses=True  # Automatically decode responses from bytes to strings
        )
    
    def get_connection(self):
        """Get direct access to the Redis connection."""
        return self.redis
    
    def store_conversion_progress(self, conversion_id, progress_data, ttl=None):
        """
        Store conversion progress in Redis.
        
        Args:
            conversion_id (str): Unique identifier of the conversion task
            progress_data (dict): Conversion progress data
            ttl (int, optional): Time-to-live for the record in seconds
        """
        key = f"{settings.REDIS_CONVERSION_PREFIX}progress:{conversion_id}"
        self.redis.set(key, json.dumps(progress_data))
        if ttl or settings.FILE_TTL:
            self.redis.expire(key, ttl or settings.FILE_TTL)
    
    def get_conversion_progress(self, conversion_id):
        """
        Retrieve conversion progress from Redis.
        
        Args:
            conversion_id (str): Unique identifier of the conversion task
            
        Returns:
            dict: Conversion progress data or None if data is not found
        """
        key = f"{settings.REDIS_CONVERSION_PREFIX}progress:{conversion_id}"
        data = self.redis.get(key)
        return json.loads(data) if data else None
    
    def delete_conversion_data(self, conversion_id):
        """
        Delete conversion data from Redis.
        
        Args:
            conversion_id (str): Unique identifier of the conversion task
        """
        key_pattern = f"{settings.REDIS_CONVERSION_PREFIX}*:{conversion_id}"
        for key in self.redis.scan_iter(match=key_pattern):
            self.redis.delete(key)
    
    def set_with_ttl(self, key, value, ttl=None):
        """
        Set a value with an optional time-to-live.
        
        Args:
            key (str): Key
            value (str, dict): Value (dictionary will be serialized to JSON)
            ttl (int, optional): Time-to-live in seconds
        """
        if isinstance(value, dict):
            value = json.dumps(value)
        self.redis.set(key, value)
        if ttl:
            self.redis.expire(key, ttl)
    
    def get_json(self, key):
        """
        Retrieve and deserialize a JSON value.
        
        Args:
            key (str): Key
            
        Returns:
            dict: Deserialized dictionary or None if the key is not found
        """
        data = self.redis.get(key)
        return json.loads(data) if data else None
    
    def publish_message(self, channel, message):
        """
        Publish a message to a Redis channel (for WebSockets).
        
        Args:
            channel (str): Channel name
            message (dict): Message to publish
        """
        self.redis.publish(channel, json.dumps(message))
    
    def close(self):
        """Close the Redis connection."""
        self.redis.close()


# Creating a singleton instance of the Redis client
redis_client = RedisClient()
