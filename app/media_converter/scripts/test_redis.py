#!/usr/bin/env python

"""
Script for testing connection to Redis and basic operations.
Run: python scripts/test_redis.py
"""

import os
import sys
import json
import time
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'media_converter.settings')
django.setup()

from media_converter.utils.redis_utils import redis_client

def test_redis_connection():
    """Tests connection to Redis."""
    try:
        response = redis_client.get_connection().ping()
        print(f"Redis connection test: {'SUCCESS' if response else 'FAILED'}")
        return response
    except Exception as e:
        print(f"Redis connection test FAILED: {e}")
        return False

def test_basic_operations():
    """Tests basic operations with Redis."""
    try:
        key = 'test:key'
        value = {'test': True, 'timestamp': time.time()}
        
        redis_client.set_with_ttl(key, value, ttl=60)
        print(f"Set value: {value}")
        
        retrieved = redis_client.get_json(key)
        print(f"Retrieved value: {retrieved}")
        
        assert retrieved['test'] == value['test'], "Values don't match"
        print("Basic operations test: SUCCESS")
        
        redis_client.get_connection().delete(key)
        return True
    except Exception as e:
        print(f"Basic operations test FAILED: {e}")
        return False

def test_conversion_progress():
    """Tests storing and retrieving conversion progress"""
    try:
        conversion_id = 'test-conversion-123'
        progress_data = {
            'status': 'processing',
            'progress': 45,
            'file_name': 'test_video.mp4',
            'target_format': 'webm',
            'started_at': time.time()
        }
        
        redis_client.store_conversion_progress(conversion_id, progress_data)
        print(f"Stored conversion progress: {progress_data}")
        
        retrieved = redis_client.get_conversion_progress(conversion_id)
        print(f"Retrieved conversion progress: {retrieved}")
        
        assert retrieved['status'] == progress_data['status'], "Status doesn't match"
        assert retrieved['progress'] == progress_data['progress'], "Progress doesn't match"
        print("Conversion progress test: SUCCESS")
        
        redis_client.delete_conversion_data(conversion_id)
        return True
    except Exception as e:
        print(f"Conversion progress test FAILED: {e}")
        return False
    
def test_hiredis():
    try:
        import redis
        assert redis.connection.HIREDIS_AVAILABLE == True, "Hiredis isn't available"
        print("Hiredis test: SUCCESS")
        return True
    except Exception as e:
        print(f"Hiredis FAILED: {e}")
        return False

def main():
    """Run all Redis tests."""
    print("\n=== Redis Test Script ===\n")
    
    if not test_redis_connection():
        print("\nFATAL: Could not connect to Redis. Please check your configuration.")
        return
    
    test_basic_operations()
    
    test_conversion_progress()
    
    test_hiredis()

    print("\n=== Redis Test Complete ===\n")

if __name__ == "__main__":
    main()