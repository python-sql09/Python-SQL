# Exercise 6: File System
# Base class representing a general file in the OS
class FileItem:
    def __init__(self, name, size, owner, permissions, created_date):
        self.name = name
        self.size = size  # in bytes
        self.owner = owner
        self.permissions = permissions
        self.created_date = created_date

    def display_info(self):
        print(f"File Name: {self.name}")
        print(f"Size: {self.size} bytes")
        print(f"Owner: {self.owner}")
        print(f"Permissions: {self.permissions}")
        print(f"Created Date: {self.created_date}")

# CSVFile class inheriting from FileItem
class CSVFile(FileItem):
    def __init__(self, name, size, owner, permissions, created_date, delimiter, row_count):
        # Call the constructor of the base class
        super().__init__(name, size, owner, permissions, created_date)
        self.delimiter = delimiter  # Specific to CSV files
        self.row_count = row_count  # Number of rows in the CSV file

    def display_info(self):
        # Call the base class display_info method
        super().display_info()
        print(f"Delimiter: {self.delimiter}")
        print(f"Row Count: {self.row_count}")

# JPGFile class inheriting from FileItem
class JPGFile(FileItem):
    def __init__(self, name, size, owner, permissions, created_date, resolution, color_depth):
        # Call the constructor of the base class
        super().__init__(name, size, owner, permissions, created_date)
        self.resolution = resolution  # Specific to JPG files (e.g., 1920x1080)
        self.color_depth = color_depth  # Specific to JPG files (e.g., 24-bit)

    def display_info(self):
        # Call the base class display_info method
        super().display_info()
        print(f"Resolution: {self.resolution}")
        print(f"Color Depth: {self.color_depth}")

# MP3File class inheriting from FileItem
class MP3File(FileItem):
    def __init__(self, name, size, owner, permissions, created_date, bitrate, duration):
        # Call the constructor of the base class
        super().__init__(name, size, owner, permissions, created_date)
        self.bitrate = bitrate  # Specific to MP3 files (e.g., 320 kbps)
        self.duration = duration  # Specific to MP3 files (e.g., 3:45)

    def display_info(self):
        # Call the base class display_info method
        super().display_info()
        print(f"Bitrate: {self.bitrate}")
        print(f"Duration: {self.duration}")

# Example usage:

# Create a CSV file object
csv_file = CSVFile("data.csv", 1024, "john_doe", "rw-r--r--", "2024-08-24", ",", 100)
print("CSV File Information:")
csv_file.display_info()
print("---------------------------")

# Create a JPG file object
jpg_file = JPGFile("image.jpg", 204800, "jane_doe", "rw-r--r--", "2024-08-23", "1920x1080", "24-bit")
print("JPG File Information:")
jpg_file.display_info()
print("---------------------------")

# Create an MP3 file object
mp3_file = MP3File("song.mp3", 5120000, "john_doe", "rw-r--r--", "2024-08-22", "320 kbps", "3:45")
print("MP3 File Information:")
mp3_file.display_info()