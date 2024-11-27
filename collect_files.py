import os
import sys

def collect_python_files(root_dir, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for foldername, subfolders, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename.endswith('.py') and filename != '__init__.py':
                    file_path = os.path.join(foldername, filename)
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        outfile.write(f"\n# File: {file_path}\n\n")
                        outfile.write(infile.read())
                        outfile.write("\n\n")
    print(f"All Python files have been written to {output_file}")

if __name__ == '__main__':
    # Check if the user provided the root directory
    if len(sys.argv) < 3:
        print("Usage: python collect_files.py <root_directory> <output_file>")
        sys.exit(1)

    root_directory = sys.argv[1]
    output_filename = sys.argv[2]

    collect_python_files(root_directory, output_filename)