class Attributes:
    def __init__(self):
        self.null = None
        self.blank = None
        self.decimal = None
        self.max_digits =None
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

    def set_decimal(self):
        """ Ask the user for decimal places """
        self.decimal = int(input("Enter your decimal places number: "))
        self.max_digits = int(input("Enter Your max digits "))
        return self.decimal ,   self.max_digits 

    def get_extra_attributes(self, decimal=None):
        """ Get extra attributes based on the user's choices """
        if decimal:  # Check if decimal is passed as True
            decimal_places = self.set_decimal()  # Get decimal places from user input
            self.attributes.append(f'decimal_places={decimal_places[0]},max_digits={decimal_places[1]}')
        
        # If there are any other attributes (null, blank), add them to the list
        if self.null:
            self.attributes.append(self.null)
        if self.blank:
            self.attributes.append(self.blank)

        print(self.attributes, "this is my data")
        return ", ".join(self.attributes)  # Return as a string joined by commas


# Example usage:
