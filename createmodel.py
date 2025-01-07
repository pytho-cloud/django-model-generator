import os
import re
import sys
from modelMaker import ModelMaker


class ModelManager:
    def __init__(self):
        self.model_name = None
        self.attributes = []
        self.attribute_names = set()

    def model_exists(self, inputs=None):
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

    def add_model_attr_after_model_exists(self, inputs):

        if len(inputs) == 0:
            return "enter your model name which u want update"

        model_exists = self.model_counts_list(inputs)

        if not model_exists:
            return f"models does not exist "
        return "You have Chance to Update Guys "

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

    def model_counts_list(self, model_name=""):
        "Here we Check counts of models in our models.py files"

        try:
            with open("models.py", "r") as f:
                content = f.read()

            models = re.findall(r"class\s+(\w+)\(models.Model\):", content)

            if len(model_name) != 0:

                if model_name not in models:

                    return False
                return True
            return len(models), models

        except Exception as e:
            print(f"Error reading models.py: {str(e)},")

    def check_models(self):
        """Check for existing models in models.py"""
        try:
            with open("models.py", "r") as f:
                content = f.read()

            models = re.findall(r"class\s+(\w+)\(models.Model\):", content)
            print(models, "this is my models data ")

            if len(models) != 0:
                return f"There are {len(models)} models in models.py: {', '.join(models)}.,{len(models)}"
            else:
                return f"No models found in models.py.{len(models)}"
        except Exception as e:
            print(f"Error reading models.py: {str(e)}")

    def add_attributes(self):
        """Add attributes to the model"""

        while True:
            try:
                model_length = int(
                    input(
                        f"Enter the number of attributes for the '{self.model_name}' model: "
                    )
                )
                break
            except ValueError as e:
                print(
                    f"Invalid input for number of attributes. Please enter a valid integer."
                )
                continue
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

    def createStr(self):
        return "String is creating "
    def run(self):
        """Run the main logic"""
        print(sys.argv, "fdsfsds")
        command = sys.argv

        if 'set' in command:
            lengths = self.check_models()
            print(lengths[len(lengths) - 1])
            if int(lengths[len(lengths) - 1]) == 0:
                print("models.py doesn't have any models, create it by using py createmodel.py createModel")
            else:
                self.createStr()
        
        elif "showmodel" in command:  
            result = self.check_models()
            print(result, '--------')
        
        elif "updatemodel" in command:  
            print("dfsdfds", len(sys.argv))
            if len(sys.argv) == 2:  
                model_name = input("Enter your model name: ")
            else:
                model_name = sys.argv[2]

            result = self.model_counts_list(model_name)
            if not result:
                print(f"No models exist with the given name {model_name}")
            else:
                self.add_attributes()

        elif "createModel" in command:  
            if self.create_model_file():
                self.take_model_name()
                if self.model_name:
                    self.add_attributes()

        else:  
            print("why")
            print("Invalid command. Only 'showmodel', 'updatemodel', or 'createModel' are supported.")


if __name__ == "__main__":
    manager = ModelManager()
    manager.run()
