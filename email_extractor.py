import re
import os # While not strictly required for just regex and file I/O, it's good practice for path awareness in automation

def extract_emails_from_file(input_filename, output_filename):
    """
    Extracts all valid email addresses from an input text file
    and saves them to a new output text file.

    Args:
        input_filename (str): The name of the file to read emails from.
        output_filename (str): The name of the file to write extracted emails to.
    """
    # Regex pattern for a common email address format
    # This pattern covers many, but not all, valid email formats.
    # It looks for:
    #   \b: word boundary
    #   [A-Za-z0-9._%+-]+: one or more letters, numbers, or specific symbols before @
    #   @: the at symbol
    #   [A-Za-z0-9.-]+: one or more letters, numbers, or hyphens after @
    #   \.: a literal dot
    #   [A-Z|a-z]{2,}: two or more letters for the top-level domain
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    extracted_emails = []

    try:
        # Ensure the input file exists
        if not os.path.exists(input_filename):
            print(f"Error: Input file '{input_filename}' not found.")
            return

        with open(input_filename, 'r', encoding='utf-8') as infile:
            content = infile.read()
            # Find all matches of the email pattern in the file content
            extracted_emails = re.findall(email_pattern, content)

        if not extracted_emails:
            print(f"No email addresses found in '{input_filename}'.")
            return

        # Write the extracted emails to the output file
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            for email in extracted_emails:
                outfile.write(email + '\n')
        print(f"Successfully extracted {len(extracted_emails)} email(s) and saved to '{output_filename}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

# --- How to use the script ---
if __name__ == "__main__":
    # 1. Create a dummy input file for testing
    #    You can manually create 'input_emails.txt' or let the script create it once.
    dummy_input_content = """
    Hello, this is a sample text with some emails.
    Contact us at user1@example.com or support@my-domain.co.uk.
    Also, check out info.name@another.org for details.
    Invalid email: not-an-email.com
    Another one: jane.doe123@sub.domain.net
    And a local email: test@localhost
    """
    input_file_name = "input_emails.txt"
    output_file_name = "extracted_emails.txt"

    # Create the dummy input file if it doesn't exist
    if not os.path.exists(input_file_name):
        with open(input_file_name, 'w', encoding='utf-8') as f:
            f.write(dummy_input_content.strip())
        print(f"Created a dummy input file: '{input_file_name}'")

    # Run the email extraction function
    extract_emails_from_file(input_file_name, output_file_name)

    # Optional: Display the content of the output file
    if os.path.exists(output_file_name):
        print("\n--- Content of extracted_emails.txt ---")
        with open(output_file_name, 'r', encoding='utf-8') as f:
            print(f.read())