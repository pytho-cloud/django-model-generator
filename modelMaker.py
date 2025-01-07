from setExtraAttr import Attributes


class ModelMaker:
    def __init__(self, attr_name, attr_field=None, primary_key=False, max_length=None):
        self.attr_name = attr_name
        self.attr_field = attr_field
        self.primary_key = primary_key
        self.on_delete = None
        self.foreign_key = None
        self.date_field = False
        self.max_length = (
            max_length if attr_field == "char" else None
        )  # Set max_length only if attr_field is 'char'

        # Ensure attr_field is set correctly
        if self.attr_field is None:
            self.attr_field = "char"

        self.attr_field_type = self.set_attribute()

    def set_attribute(self):
        if self.attr_field == "char":
            if self.max_length is None:
                self.max_length = self.get_max_length()
            return f"CharField(max_length={self.max_length})"

        if self.attr_field == "int":
            return "IntegerField"

        if self.attr_field == "datetime":
            return self.set_date_time_field()

    def get_max_length(self):
        """Prompt user to enter max length for char fields"""
        max_length = int(input("Enter your Max Length: "))
        return max_length

    def set_date_time_field(self):
        """Set up DateTimeField attributes"""
        add_auto_now_add = input("Do you want to add auto_now_add? (yes/no): ").lower()
        if add_auto_now_add == "yes":
            self.date_field = True
            return "DateTimeField(auto_now_add=True)"
        else:
            return "DateTimeField"

    def _write_attribute(self):
        attr_dict = {
            "char": f"    {self.attr_name} = models.CharField(max_length={self.max_length} {self.is_primary_key()},{self.set_extra_attr()})\n",
            "int": f"    {self.attr_name} = models.IntegerField({self.is_primary_key()})\n",
            "email": f"    {self.attr_name} = models.EmailField(primary_key={self.primary_key})\n",
            "datetime": f"    {self.attr_name} = models.DateTimeField({self.is_primary_key()})\n",
            "text": f"    {self.attr_name} = models.TextField({self.is_primary_key()},{self.set_extra_attr()})\n",
        }

        if self.attr_field in attr_dict:
            return attr_dict[self.attr_field]
        else:
            print(f"Unknown field type: {self.attr_field}")
            return None

    def write_model_attributes(self):
        """Write the attributes to models.py"""
        try:
            with open("models.py", "a") as f:
                values = self._write_attribute()
                if values:
                    f.write(values)
                print(
                    f"Attributes for '{self.attr_name}' have been added to models.py."
                )
        except Exception as e:
            print(f"Error adding attributes to {self.attr_name}: {str(e)}")

    def is_primary_key(self):
        """Return primary key field string if primary_key is True"""
        return f"primary_key={self.primary_key}" if self.primary_key else ""

    def set_extra_attr(self):
        """Handle extra attributes using the Attributes class"""
        extra = Attributes()

        extra_data = extra.get_extra_attributes()  # Retrieve extra attributes
        return extra_data
