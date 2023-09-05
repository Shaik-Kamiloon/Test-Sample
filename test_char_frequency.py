from char_frequency import FrequencyCalculator

def test_when_string_given_char_frequency_return_frequency_dictionary():
    frequency_malayalam = FrequencyCalculator().char_frequency("malayalam")
    frequency_halocination = FrequencyCalculator().char_frequency("halocination")
    assert frequency_malayalam == {'a': 4, 'l': 2, 'm': 2, 'y': 1}
    assert frequency_halocination == {'a': 2, 'c': 1, 'h': 1, 'i': 2, 'l': 1, 'n': 2, 'o': 2, 't': 1}

def test_when_numeric_string_given_return_frequency_dictionary():
    frequency_invalid_string = FrequencyCalculator().char_frequency("123")
    assert frequency_invalid_string == {'1': 1, '2': 1, '3': 1}
    # assert False
