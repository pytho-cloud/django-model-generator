class Attributes:
    def __init__(self):
        self.null = None
        self.blank = None
        self.attributes = []
        self.set_null_true()  # Call methods during initialization
        self.set_blank_true()
        
       

    def set_null_true(self):
        """ Ask the user if the attribute can be null """
        user_input = input("Set Null True like: null = True, yes/no: ").lower()
        if user_input == 'yes':
            self.null = 'null=True'  # Assign the string to self.null
            self.attributes.append(self.null)  # Append the attribute to the list
        else:
            self.null = None

    def set_blank_true(self):
        """ Ask the user if the attribute can be blank """
        user_input = input("Set Blank True like: blank = True, yes/no: ").lower()
        if user_input == 'yes':
            self.blank = 'blank=True'  # Assign the string to self.blank
            self.attributes.append(self.blank)  # Append the attribute to the list
        else:
            self.blank = None

    def get_extra_attributes(self):
        """ Get extra attributes based on the user's choices """
        attributes = []
        if self.null:
            attributes.append(self.null)  # Append if it's not None
        if self.blank:
            attributes.append(self.blank)  # Append if it's not None
        print(attributes, "this is my data")
        return " ,".join(attributes)  # Return as a string joined by commas

# Example usage:
# attributes = Attributes()
# print(attributes.get_extra_attributes())
