import re

def process_file():
    input_file = input("Enter input filename: ")
    extracted_info_file = input("Enter extracted info filename: ")
    
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
    
    cleaned_lines = []
    extracted_info = []
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("#EXTINF"):
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if not next_line.startswith("http") or not re.search(r'\.(mkv|mp4|avi)$', next_line, re.IGNORECASE):
                    i += 2  # Skip both lines
                    continue
            
            # Extract info after #EXTINF:-1,
            match = re.search(r'#EXTINF:-1,(.*)', line)
            if match:
                extracted_info.append(match.group(1).strip())
        
        cleaned_lines.append(line + "\n")
        i += 1
    
    # Write extracted info to another file
    with open(extracted_info_file, 'w', encoding='utf-8') as infofile:
        infofile.writelines(line + "\n" for line in extracted_info)

# Example usage
process_file()
