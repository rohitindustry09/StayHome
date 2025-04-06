import os

def search_text_in_files(directory, text):
    matched_files = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    if text in f.read():
                        matched_files.append(file_path)
                        print(f"Found in: {file_path}")
            except Exception as e:
                print(f"Skipping {file_path} due to error: {e}")

    if not matched_files:
        print("No matches found.")
    return matched_files

# Example usage
directory_to_search = "/home/kali/airbnb-clone"  # Change this to your target directory
search_text = "Airbnb your home"  # Change this to your target text
search_text_in_files(directory_to_search, search_text)
