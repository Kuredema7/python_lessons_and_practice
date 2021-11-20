
# This takes how many times we will test the cases...
test_case = int(input())

# Here we'll iterate through the test case number
for i in range(test_case):

    # We'll take the string data will be tested
    string = input()

    # This variable will hold the letters in the even index/seat
    even_index = ''

    # This variable will hold the letters in the odd index/seat
    odd_index = ''

    # Here we'll iterate through the string specified
    for index in range(len(string)):

        # This will check if the index/seat is the even one
        if index % 2 == 0:
            # This will assign every letter which has the even index/seat
            even_index += string[index]
        else:
            # This will assign every letter which has the odd index/seat
            odd_index += string[index]
        
    # Then we'll print/output the even letters space the odd letters
    print(even_index, odd_index)