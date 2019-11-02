"""
Member Object class

"""

# Member Class
class Member:
    # Class Variables

    # Constructor
    def __init__(self, memberCode, firstName, lastName, tanzeem, jamat):
        self.memberCode = memberCode
        self.firstName = firstName
        self.lastName = lastName
        self.tanzeem = tanzeem
        self.jamat = jamat
        
    """ 
    Setter Functions:
    These functions will set the values after validating the data.
    """
    # Set Member Code

    # Set First Name

    # Set Last Name

    # Set Tanzeem

    # Set Jamat

    """
    Getter Functions:
    These function will return the values for the fields.
    """
    # Get Member Code

    # Get First Name

    # Get Last Name

    # Get Name
    "This will return full name of the member"

    # Get Tanzeem

    # Get Jamat

    # Get Member
    "Function to return a string with the member data"

    """
    Validation Functions:
    These function will check if the data types are correct, i.e. member code is an integer
    """

    # Validate Member Code
    "Member code is an integer"

    # Validate Name
    "Name is a string"

    # Validate Tanzeem
    "Tanzeem has to be one of the five Jamat tanzeems"

    # Validate Jamat
    "Jamat is a valid US city"

    """
    Exception Function:
    This function will throw an exception based on the failed validation.
    You will send the type of exception and the correct error will be return
    i.e type "code" will return "member code needs to be an integer"
    """
    # Exception