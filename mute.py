import os
import time
 
original_clip_directory = "D:\SAR Video Backup/Nates_SD"
muted_clip_directory  = "D:\SAR Video Backup/Nates_SD/Nates_SD_Muted"

ignored_extensions = [".sfk", ".jpg", ".cr2"]

print(f"Looping all files and directories in the specified path: {original_clip_directory}")

for filename in os.listdir(original_clip_directory):
    
    file_extension = filename[len(filename)-4 : len(filename)]

    if file_extension.lower() in ignored_extensions:
        continue

    else:

        full_path = os.path.join(original_clip_directory,filename)
    
        if os.path.isfile(full_path):
        
            current_file_path = '%s\%s' % (original_clip_directory, filename)
            muted_file_path = "%s\%s" % (muted_clip_directory, filename)

            print(current_file_path)
            print(muted_file_path)
            
            os.system('ffmpeg -i "%s" -c copy -an "%s"' % (current_file_path, muted_file_path))

            time.sleep(0.25)