import os
# DO NOT CHANGE THIS CODE


API_KEY = input("Enter your API key: ")

# Save the API_KEY in the dotenv file
with open(".env", "w") as f:
    f.write(f"GROQ_API_KEY={API_KEY}\n")

# Export the API_KEY as an environment variable
os.environ["GROQ_API_KEY"] = API_KEY

# Install the dependencies in the requirements.txt file
print("Installing dependencies...")
os.system("pip install -r requirements.txt")
