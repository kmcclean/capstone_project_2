class ErrorHandling:

    def nonblank_string(self, check_text):
        if check_text == "":
            return False
        else:
            return True

    def float_check(self, test_text):
        try:
            check = float(test_text)
            return True
        except ValueError:
            return False

    # This is used when an integer between a certain range is required.
    def range_integer_input_checking(self, check_text, low, high):
            try:
                a = int(check_text)
                if a >= low and a <= high:
                    return True
                else:
                    return False
            except ValueError:
                print("The entry needs to be an integer.")
                return False

    def variable_length_checking(self, check_text, required_length):
        try:
            a = len(check_text)
            if a == required_length:
                return True
            else:
                return False
        except ValueError:
            print("The entry needs to be an integer.")
            return False


    # this checks to make sure the truth of the number being within the range provided.
    def range_provided_truth_check(self, test_number, low, high):
        if test_number >= low and test_number <= high:
            return True
        else:
            print("Choose a number between " + str(low) + " and " + str(high))
            return False