import os
import re
import sys
from modelMaker import ModelMaker

# Function to check if a model already exists in models.py
def modelExists(model_name):
    try:
        with open('models.py', 'r') as f:
            content = f.read()

        # Check if the model class definition already exists
        if f"class {model_name}(models.Model):" in content:
            return True
        return False
    except Exception as e:
        print(f"Error reading models.py: {str(e)}")
        return False

# Function to create a model class in models.py
def takeModelName():
    model_name = input("Enter Your Model Name: ")

    if modelExists(model_name):
        print(f"Model '{model_name}' already exists in models.py.")
        return model_name

    try:
        with open("models.py", 'a') as f:
            
            f.write(f"\nfrom django.db import models :\n")

            f.write(f"\nclass {model_name}(models.Model):\n")
            print(f"Model '{model_name}' has been added to models.py.")
        return model_name
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


def createModelFile():
    try:
        if os.path.exists("models.py"):
         
            return True
        else:
            print("Creating models.py...")
            with open('models.py', 'w') as f:
                pass  

            print("models.py created successfully.")
            return True

    except Exception as e:
        print(f"Error creating models.py: {str(e)}")
        return False


def checkModels():
    try:
        with open('models.py', 'r') as f:
            content = f.read()

        models = re.findall(r'class\s+(\w+)\(models.Model\):', content)

        if len(models) != 0:
            return f"There are {len(models)} models in models.py: {', '.join(models)}."
        else:
            return "No models found in models.py."

    except Exception as e:
        print(f"Error reading models.py: {str(e)}")

def addAttributes(model_name):
    model_length = int(input(f"Enter the number of attributes for the '{model_name}' model: "))
    attributes = []
    attribute_names = set()  
    
    while model_length > 0:
        model_attr_name = input("Enter your attribute name: ")

        # Check if attribute name is unique
        if model_attr_name in attribute_names:
            print(f"Attribute name '{model_attr_name}' already exists. Please enter a unique name.")
            continue

        attribute_names.add(model_attr_name)
        
        model_attr_field = input("Set model field (char, int, email, etc.): ").lower()
        
        if model_attr_field not in ['char', 'int', 'email']:
            print("Invalid field type. Please enter 'char', 'int', or 'email'.")
            continue
        
        is_primary_key = input("Set as Primary Key? (yes/no): ").lower() == 'yes'
        
        # Create ModelMaker instance for the attribute
        model_attr = ModelMaker(model_attr_name, model_attr_field, primary_key=is_primary_key)
        attributes.append(model_attr)
        
        model_length -= 1
    

    try:
        with open("models.py", 'a') as f:
            for attr in attributes:
                if attr.attr_field == 'char':
                    f.write(f"    {attr.attr_name} = models.CharField(max_length={attr.max_length})\n")
                elif attr.attr_field == 'int':
                    f.write(f"    {attr.attr_name} = models.IntegerField()\n")
                elif attr.attr_field == 'email':
                    f.write(f"    {attr.attr_name} = models.EmailField()\n")
                
                if attr.primary_key:
                    f.write(f"    {attr.attr_name}_primary_key = models.PrimaryKey\n")
            print(f"Attributes for '{model_name}' have been added to models.py.")
    except Exception as e:
        print(f"Error adding attributes to {model_name}: {str(e)}")

# Main command execution logic
def main():
    # Check if the user provided a command
    if len(sys.argv) < 2:
        print("Usage: py createModel.py <command>")
        return

    command = sys.argv[1]

    if command == "show models":
        result = checkModels()
        print(result)

    elif command == "createModel":
        if createModelFile():
            model_name = takeModelName()
            if model_name:
                addAttributes(model_name)

    else:
        print("Invalid command. Only 'show models' or 'createModel' are supported.")

# Run the script
if __name__ == "__main__":
    main()
