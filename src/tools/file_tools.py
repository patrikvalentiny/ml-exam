from datetime import datetime

def save_file(content: str, filename: str) -> str:
    """
    Saves the provided content to a file with the given filename.
    
    Args:
        content (str): The content to save.
        filename (str): The name of the file to save to.
        
    Returns:
        str: A message indicating success or failure.
    """
    try:
        timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename_with_timestamp = f"{filename}_{timestamp_str}"
        with open(filename_with_timestamp, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Successfully saved content"
    except Exception as e:
        return f"Error saving file: {str(e)}"
