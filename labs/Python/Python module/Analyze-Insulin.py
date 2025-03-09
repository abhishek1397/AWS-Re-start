"""
In GenBank format, records typically start with "ORIGIN" and end with "//".
Writing a general python script to filter protein data  
"""

# Retrieve the protein sequence of human insulin from human preproinsulin
import re
import os

text="""
ORIGIN      
        1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
       61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
//
"""
# note here """ """ is multi-line string

cleaned_text = re.sub(r'(?i)\borigin\b', '', text)      # Remove 'origin' (case-insensitive)
cleaned_text = re.sub(r'\d+', '', cleaned_text)     # Remove numbers
cleaned_text = re.sub(r'\s+', '', cleaned_text)     # Remove all spaces and newlines
val = re.sub(r'//', '', cleaned_text)      # Remove the '//' symbol

print(val)
print("Length of protein sample:", len(val))


# Exercise 2: Obtaining the protein sequence of human insulin

val_1=val[:24]          #lsinsulin-seq-clean.txt
print(val_1)
print("Length of val_1:",len(val_1))
print()

val_2=val[24:54]        #binsulin-seq-clean.txt
print(val_2)
print("Length of val_2:",len(val_2))
print()

val_3=val[54:89]        #cinsulin-seq-clean.txt
print(val_3)
print("Length of val_3:",len(val_3))
print()

val_4=val[89:110]       #ainsulin-seq-clean.txt
print(val_4)
print("Length of val_4:",len(val_4))
print()

""" additional code to automate file creation"""

# Define the file paths for each sequence
file_paths = {
    "/home/ec2-user/environment/Insulin files/lsinsulin-seq-clean.txt": val_1,
    "/home/ec2-user/environment/Insulin files/binsulin-seq-clean.txt": val_2,
    "/home/ec2-user/environment/Insulin files/cinsulin-seq-clean.txt": val_3,
    "/home/ec2-user/environment/Insulin files/ainsulin-seq-clean.txt": val_4,
}

# Write each extracted protein sequence to a separate file if the file doesn't exist
for file_name, sequence in file_paths.items():
    try:
        # Check if the file exists
        if not os.path.exists(file_name):  # If the file does not exist
            # Create and write to the file
            with open(file_name, 'w') as file:
                file.write(sequence + "\n")  # Write the sequence to the file
            print(f"The file {file_name} did not exist. It has been created and data has been written.")
        else:
            print(f"The file {file_name} already exists. No new data was written.")
    
    except FileNotFoundError:
        print(f"Error: The file path {file_name} does not exist.")
    except PermissionError:
        print(f"Error: Permission denied when trying to write to {file_name}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")