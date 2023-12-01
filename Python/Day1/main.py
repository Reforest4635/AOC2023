
def sum_of_calibration():
    string_to_integer = {"one":'o1e',"two":'t2o',"three":'t3e',"four":'4',"five":'5e',"six":'6e',"seven":'7n',"eight":'e8t',"nine":'n9e'}
    calibration_codes_data = []
    calibration_codes = []

    with open("data.txt","r") as data:
        lines = data.readlines()
        for i in lines:
            calibration_codes_data.append(i)

    for index,i in enumerate(calibration_codes_data):
        updated_code = i
        for string in string_to_integer:
            updated_code = updated_code.replace(string,str(string_to_integer.get(string)))
        calibration_codes_data[index] = updated_code

    for i in calibration_codes_data:
        digits = [int(j) for j in i if j.isdigit()]
        calibration_codes.append(int(str(digits[0]) + str(digits[-1])))
    print(sum(calibration_codes))
    return

if __name__ == '__main__':
    sum_of_calibration()
