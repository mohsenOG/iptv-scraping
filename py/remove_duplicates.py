import re

def remove_duplicates():
    input_file = input("Enter input filename: ")
    output_file = input("Enter output filename: ")
    
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
    
    unique_titles = set()
    cleaned_titles = []
    
    for line in lines:
        cleaned_line = re.sub(r' S\d{2} E\d{2}', '', line).strip()
        if cleaned_line not in unique_titles:
            unique_titles.add(cleaned_line)
            cleaned_titles.append(cleaned_line)
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(title + "\n" for title in cleaned_titles)

# Example usage
remove_duplicates()
