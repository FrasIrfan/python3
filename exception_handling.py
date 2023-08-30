try:
    num = int(input("Enter a number: "))
    result = num // 10
# "//" used for integer division
except ZeroDivisionError:
    print ("Zero Division Error")
except ValueError:
    print ("Value Error")
else:
    print ("Result:" , result)
finally:
    print("Exception Handling Complete")
