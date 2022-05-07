import os
import time
 
original_clip_directory = "D:\Video Backup"
muted_clip_directory    = "D:\Video Backup\Muted"

ignored_extensions = [".sfk", ".jpg", ".cr2"]

print(f"Looping all files and directories in the specified path: {original_clip_directory}")

for filename in os.listdir(original_clip_directory):
    
    # Check file extension and skip if it isn't a video format. 
    file_extension = filename[len(filename)-4 : len(filename)]

    if file_extension.lower() in ignored_extensions:
        continue

    else:

        current_file_path = os.path.join(original_clip_directory,filename)
    
        if os.path.isfile(current_file_path):
        
            muted_file_path = "%s\%s" % (muted_clip_directory, filename)

            os.system('ffmpeg -i "%s" -c copy -an "%s"' % (current_file_path, muted_file_path))

            time.sleep(0.25)