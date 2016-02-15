class ErrorHandling:

    def nonblank_string(self, check_text):
        a = False
        while a == False:
            text = input(check_text)
            a = self.is_nonblank_string_truth_check(text)
        return text

    # This does a simple check to make sure that the entry is non-blank.
    def is_nonblank_string_truth_check(self, test_text):
            if test_text is not "":
                return True
            else:
                print("Blank entries are not accepted.")
                return False

    # This is the integer checking for the game. It makes sure that the data given is a positive integer.
    def positive_integer_input_checking(self, check_text):
        a = False
        while a == False:
            try:
                check = int(input(check_text))
                a = self.range_provided_truth_check(check, 0, float('inf'))
            except ValueError:
                print("The entry needs to be an integer.")
        return check

    # This is used when an integer between a certain range is required.
    def range_integer_input_checking(self, check_text, low, high):
        a = False
        while a == False:
            try:
                check = int(input(check_text))
                a = self.range_provided_truth_check(check, low, high)
            except ValueError:
                print("The entry needs to be an integer.")
        return check

    # this checks to make sure the truth of the number being within the range provided.
    def range_provided_truth_check(self, test_number, low, high):
        if test_number >= low and test_number <= high:
            return True
        else:
            print("Choose a number between " + str(low) + " and " + str(high))
            return False