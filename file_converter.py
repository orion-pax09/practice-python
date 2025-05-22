import os

def convert_files():
    text_files = [
        "Bank project.txt",
        "encryption.txt",
        "hangman game.txt",
        "python slot machine.txt",
        "question quiz.txt"
    ]
    
    for text_file in text_files:
        # Read content from text file
        with open(text_file, 'r') as f:
            content = f.read()
        
        # Create python filename by removing spaces
        python_file = text_file.replace(' ', '').replace('.txt', '.py')
        
        # Write content to python file
        with open(python_file, 'w') as f:
            f.write(content)
        
        print(f"Converted {text_file} to {python_file}")

if __name__ == "__main__":
    convert_files()
