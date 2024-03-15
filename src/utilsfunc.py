import os
import uuid
from datetime import datetime

def save_uploaded_file(uploaded_file) -> str:
    """
    Save an uploaded file to a specified directory.

    :param uploaded_file: Streamlit UploadedFile object.
    :return: Path to the saved file.
    """
    upload_directory = os.path.join("utils", "uploads")
    if not os.path.exists(upload_directory):
        os.makedirs(upload_directory)

    conversation_id = str(uuid.uuid4())
    date_str = datetime.now().strftime("%Y%m%d")

    subdirectory = os.path.join(
        upload_directory, f"{conversation_id}_{date_str}"
    )
    if not os.path.exists(subdirectory):
        os.makedirs(subdirectory)

    file_path = os.path.join(subdirectory, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path

