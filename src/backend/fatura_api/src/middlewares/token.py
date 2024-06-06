import jwt
import os

# Example secret key for demonstration; in production, use a secure, unpredictable value
SECRET_KEY = os.environ.get('SECRET_KEY')

def generate_test_token(payload):
    """
    Generates a JWT for testing purposes.
    
    :param payload: The payload to encode in the JWT.
    :return: A JWT string.
    """
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

test_payload = {
    'sub': 'test_subject',
    'user_id': '7a871f67-c086-4c66-9fb4-1b663d3d893c',
    'name': 'Test User',
    'iat': 1516239072,  # Issued at timestamp
}

test_token = generate_test_token(test_payload)
print(f"Generated Test Token: {test_token}")
