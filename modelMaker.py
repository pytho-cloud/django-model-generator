class ModelMaker:

    def __init__(self, attr_name, attr_field=None, primary_key=False, max_length=None):
        self.attr_name = attr_name
        self.attr_field = attr_field
        self.primary_key = primary_key
        self.max_length = max_length if attr_field == 'char' else None  # Set max_length only if attr_field is 'char'

        # Ensure attr_field is set correctly
        if self.attr_field is None:
            self.attr_field = 'char' 
        
        self.attr_field_type = self.setAttribute()

    def setAttribute(self):
        if self.attr_field == "char":
            if self.max_length is None:  
                self.max_length = self.get_max_length() 
            return f"CharField(max_length={self.max_length})"
        
        if self.attr_field == 'int':
            return "IntegerField"

    def get_max_length(self):
        """ Prompt user to enter max length for char fields """
        max_length = int(input("Enter your Max Length: "))
        return max_length

# Example usage:
