def divide(x, y):
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = x // y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")


a = divide(10, 5)
b = divide(10, 0)

# First test_data

my_dict = {"a": 1, "b": 2, "c": 3}

try:
    value = my_dict["d"]
except IndexError:
    print("This index does not exist!")
except KeyError:
    print("This key is not in the dictionary!")
except:
    print("Some other error occurred!")

# Second test_data

try:
    value = my_dict["d"]
except (IndexError, KeyError):
    print("An IndexError or KeyError occurred!")

"""////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""

my_dict = {"a": 1, "b": 2, "c": 3}

try:
    value = my_dict["d"]
except KeyError:
    print("A KeyError occurred!")
finally:
    print("The finally statement has executed!")

"""////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""

my_dict = {"a": 1, "b": 2, "c": 3}

# Without finally

try:
    value = my_dict["a"]
except KeyError:
    print("A KeyError occurred!")
else:
    print("No error occurred!")

# With finally

try:
    value = my_dict["a"]
except KeyError:
    print("A KeyError occurred!")
else:
    print("No error occurred!")
finally:
    print("The finally statement ran!")

"""////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""

x = 5
if x < 10:
    raise ValueError('x should not be less than 10!')

"""////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""

