import os

# Select the directory whose content you want to list 
directory_path = r'C:\Users\theak\OneDrive\Documents'

#OS module ka use krenge hm selected directory ka content list krne ke liye 
contents = os.listdir(directory_path)

# Print krenge directory content ko
print(contents)
