import os

def delete_all_files(folder_path):
  for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):  # Check if it's a file, not a directory
      os.remove(file_path)
      
clear_hats = "enfeites/hats"
clear_baloons = "enfeites/baloons"
clear_confety = "enfeites/confety"
clear_images = "images"
clear_info = "info_insta"
clear_gemini = "gemini_res"
clear_happybirthday = "happyBirthday"

delete_all_files(clear_hats)
delete_all_files(clear_baloons)
delete_all_files(clear_confety)
delete_all_files(clear_images)
delete_all_files(clear_info)
delete_all_files(clear_gemini)
delete_all_files(clear_happybirthday)