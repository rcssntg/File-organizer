import os
import shutil

def organize_folder(folder_path):
  """Organizes the files and folders in the given folder into subfolders based on all possible file types.

  Args:
    folder_path: The path to the folder to organize.
  """

  # Create a dictionary to map file extensions to subfolder names.
  subfolder_names = {}

  # Iterate over the files and folders in the folder.
  for file_or_folder in os.listdir(folder_path):

    # Get the full path to the file or folder.
    file_or_folder_path = os.path.join(folder_path, file_or_folder)

    # Check if the file or folder is a file.
    if os.path.isfile(file_or_folder_path):

      # Get the file extension.
      file_extension = os.path.splitext(file_or_folder_path)[1]

      # If the file extension is not already in the dictionary, add it.
      if file_extension not in subfolder_names:
        subfolder_names[file_extension] = file_extension

  # Create the subfolders.
  for subfolder_name in subfolder_names.values():
    subfolder_path = os.path.join(folder_path, subfolder_name)
    if not os.path.exists(subfolder_path):
      os.makedirs(subfolder_path)

  # Move the files to the subfolders.
  for file_or_folder in os.listdir(folder_path):

    # Get the full path to the file or folder.
    file_or_folder_path = os.path.join(folder_path, file_or_folder)

    # Check if the file or folder is a file.
    if os.path.isfile(file_or_folder_path):

      # Get the file extension.
      file_extension = os.path.splitext(file_or_folder_path)[1]

      # Get the subfolder path for the file extension.
      subfolder_path = os.path.join(folder_path, subfolder_names[file_extension])

      # Move the file to the subfolder.
      shutil.move(file_or_folder_path, subfolder_path)

if __name__ == "__main__":
  # Get the path to the folder to organize.
  folder_path = input("Enter the path to the folder to organize: ")

  # Organize the folder.
  organize_folder(folder_path)

  # Print a success message.
  print("The folder has been organized.")