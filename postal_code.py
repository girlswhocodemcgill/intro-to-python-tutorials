def is_postal_code(code):

    if type(code) == str:
        if len(code) == 7:
            for i in range(7):
                
                if i == 0 or i == 2 or i == 5:
                    if not code[i].isalpha() or not code[i].isupper():
                        return False

                elif i == 1 or i == 4 or i == 6:
                    if not code[i].isdigit():
                        return False

                else:
                    if code[i] != " ":
                        return False

            return True

    return False
