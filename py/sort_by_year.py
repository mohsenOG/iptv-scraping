import re

def sort_movies_by_year():
    input_file = input("Enter input filename: ")
    output_file = input("Enter output filename: ")
    
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
    
    movies_with_year = []
    movies_without_year = []
    
    for line in lines:
        match = re.search(r'\((\d{4})\)', line)
        if match:
            year = int(match.group(1))
            movies_with_year.append((year, line.strip()))
        else:
            movies_without_year.append(line.strip())
    
    # Sort movies by year
    movies_with_year.sort(key=lambda x: x[0])
    
    # Combine sorted movies and those without a year
    sorted_movies = [movie[1] for movie in movies_with_year] + movies_without_year
    
    # Write sorted output to file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(line + "\n" for line in sorted_movies)

# Example usage
sort_movies_by_year()
