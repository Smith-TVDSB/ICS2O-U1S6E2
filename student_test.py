import pytest
import student 



def test_default():
    input_values=['Power Glove', '1', '299.99']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert output[3].lower()=='power glove has 1 in stock, and it costs $299.99', "It must be exact"
 
def test_two():
    input_values=['blarg', '17', '1.99']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert output[3].lower()=='blarg has 17 in stock, and it costs $1.99', "It must be exact"

