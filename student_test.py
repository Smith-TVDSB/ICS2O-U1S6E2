import pytest
import student 



def test_default():
    input_values=['5.4']
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

    assert '5.4' in output[1] and '            5.4' in output[1] and '5.4         ' in output[1] and '005.4' in output[1]
    
 def test_verify():
    input_values=['16.3']
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

    assert '16.3' in output[1] and '           16.3' in output[1] and '16.3        ' in output[1] and '016.3' in output[1]
 

