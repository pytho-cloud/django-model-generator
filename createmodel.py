import os
import re
import sys
from modelMaker import ModelMaker


class ModelManager:
    def __init__(self):
        self.model_name = None
        self.attributes = []
        self.attribute_names = set()

    def model_exists(self):
        """Check if the model already exists in models.py"""
        try:
            with open("models.py", "r") as f:
                content = f.read()
            if f"class {self.model_name}(models.Model):" in content:
                return True
            return False
        except Exception as e:
            print(f"Error reading models.py: {str(e)}")
            return False

    def create_model_file(self):
        """Create the models.py file if it doesn't exist"""
        try:
            if os.path.exists("models.py"):
                return True
            else:
                print("Creating models.py...")
                with open("models.py", "w") as f:
                    pass
                print("models.py created successfully.")
                return True
        except Exception as e:
            print(f"Error creating models.py: {str(e)}")
            return False

    def take_model_name(self):
        """Prompt the user for a model name and check if it exists"""
        self.model_name = input("Enter Your Model Name: ")

        if self.model_exists():
            print(f"Model '{self.model_name}' already exists in models.py.")
            return self.model_name

        try:
            with open("models.py", "a") as f:
                f.write(f"\nfrom django.db import models \n")
                f.write(f"\nclass {self.model_name}(models.Model):\n")
                print(f"Model '{self.model_name}' has been added to models.py.")
            return self.model_name
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

    def check_models(self):
        """Check for existing models in models.py"""
        try:
            with open("models.py", "r") as f:
                content = f.read()

            models = re.findall(r"class\s+(\w+)\(models.Model\):", content)

            if len(models) != 0:
                return (
                    f"There are {len(models)} models in models.py: {', '.join(models)}."
                )
            else:
                return "No models found in models.py."
        except Exception as e:
            print(f"Error reading models.py: {str(e)}")

    def add_attributes(self):
        """Add attributes to the model"""
        model_length = int(
            input(f"Enter the number of attributes for the '{self.model_name}' model: ")
        )

        while model_length > 0:
            print(model_length, "times running ")
            model_attr_name = input("Enter your attribute name: ")

            if model_attr_name in self.attribute_names:
                print(
                    f"Attribute name '{model_attr_name}' already exists. Please enter a unique name."
                )
                continue

            self.attribute_names.add(model_attr_name)

            model_attr_field = input(
                "Set model field (char, int, email, datetime, text): "
            ).lower()

            if model_attr_field not in ["char", "int", "email", "datetime", "text"]:
                print(
                    "Invalid field type. Please enter 'char', 'int', 'datetime', 'email', or 'text'."
                )
                continue

            is_primary_key = input("Set as Primary Key? (yes/no): ").lower() == "yes"

            model_attr = ModelMaker(
                model_attr_name, model_attr_field, primary_key=is_primary_key
            )

            self.attributes.append(model_attr)
            model_attr.write_model_attributes()  # Call to write the attribute immediately
            model_length -= 1

    def run(self):
        """Run the main logic"""
        if len(sys.argv) < 2:
            print("Usage: py createModel.py <command>")
            return

        command = sys.argv[1]

        if command == "showmodels":
            result = self.check_models()
            print(result)

        elif command == "createModel":
            if self.create_model_file():
                self.take_model_name()
                if self.model_name:
                    self.add_attributes()

        else:
            print("Invalid command. Only 'showmodels' or 'createModel' are supported.")


if __name__ == "__main__":
    manager = ModelManager()
    manager.run()
