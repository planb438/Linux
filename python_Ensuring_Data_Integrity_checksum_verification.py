import hashlib
import sys

def compute_checksum(file_path, algorithm='sha256'):
    """Compute checksum of a file."""
    try:
        # Open the file in binary mode
        with open(file_path, 'rb') as file:
            # Initialize the hash object
            hash_object = hashlib.new(algorithm)
            # Read the file in chunks to conserve memory
            for chunk in iter(lambda: file.read(4096), b''):
                hash_object.update(chunk)
            # Return the hexadecimal digest of the hash
            return hash_object.hexdigest()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error computing checksum: {e}")
        sys.exit(1)

def verify_checksum(file_path, expected_checksum, algorithm='sha256'):
    """Verify checksum of a file against the expected checksum."""
    computed_checksum = compute_checksum(file_path, algorithm)
    if computed_checksum == expected_checksum:
        print(f"Checksum verified: {file_path}")
    else:
        print(f"Checksum mismatch: {file_path}")
        print(f"Expected: {expected_checksum}")
        print(f"Computed: {computed_checksum}")

if __name__ == "__main__":
    # Provide file path and expected checksum as command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python script.py <file_path> <expected_checksum>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    expected_checksum = sys.argv[2]

    verify_checksum(file_path, expected_checksum)
