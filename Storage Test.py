import os
import time


def test_sd_card_health(test_file="sd_card_test_file", file_size_mb=100):
    """
    Test the health of an SD card by measuring write and read speeds
    and checking data integrity.

    Parameters:
        test_file (str): The name of the test file to create on the SD card.
        file_size_mb (int): Size of the test file in megabytes.
    """
    try:
        # Generate test data
        test_data = b"A" * (1024 * 1024)  # 1 MB of data
        file_path = os.path.join(os.getcwd(), test_file)

        print(f"Testing SD card health. File: {file_path}")

        # Write test
        start_time = time.time()
        with open(file_path, "wb") as f:
            for _ in range(file_size_mb):
                f.write(test_data)
        write_time = time.time() - start_time
        write_speed = file_size_mb / write_time
        print(f"Write Speed: {write_speed:.2f} MB/s")

        # Read test
        start_time = time.time()
        with open(file_path, "rb") as f:
            while f.read(1024 * 1024):  # Read in 1 MB chunks
                pass
        read_time = time.time() - start_time
        read_speed = file_size_mb / read_time
        print(f"Read Speed: {read_speed:.2f} MB/s")

        # Verify data integrity
        with open(file_path, "rb") as f:
            for _ in range(file_size_mb):
                data = f.read(1024 * 1024)
                if data != test_data:
                    print("Data integrity check failed!")
                    os.remove(file_path)
                    return

        print("Data integrity check passed.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Clean up test file
        if os.path.exists(file_path):
            os.remove(file_path)
            print("Test file removed.")
        else:
            print("No test file to clean up.")


# Run the test
test_sd_card_health()
