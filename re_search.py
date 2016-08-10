import re

# compile re pattern only once
head_pattern = re.compile(r'\W*PROCEDURE\s+(?P<func>[\d\w_]+);')
end_pattern = re.compile(r'ENDPROCEDURE\s+(?P<func>[\d\w_]+);')


def get_procedure_name(line):
    match = head_pattern.search(line)
    if match:
        return match.groupdict()['func']


def is_strict_procedure_end(line, procedure_name):
    match = end_pattern.search(line)
    if match:
        if match.groupdict()['func'] == procedure_name:
            return True
    return False

def is_an_procedure_end(line):
    return line.find('ENDPROCEDURE') >= 0



if __name__ == '__main__':
    import unittest

    class SearchUnitTestSuite(unittest.TestCase):

        def test_procedure_head(self):
            line = ' PROCEDURE is_this_parameter_ok; /* comments */'
            expected = 'is_this_parameter_ok'
            result = get_procedure_name(line)
            self.assertEqual(expected, result)


        def test_strict_procedure_end_not_end(self):
            line = ' PROCEDURE is_this_parameter_ok; /* comments */'
            expected = False
            result = is_strict_procedure_end(line, 'is_this_parameter_ok')
            self.assertEqual(expected, result)


        def test_strict_procedure_end_not_this_function(self):
            line = ' ENDPROCEDURE another_func; /* comments */'
            expected = False
            result = is_strict_procedure_end(line, 'is_this_parameter_ok')
            self.assertEqual(expected, result)

        def test_strict_procedure_end_true(self):
            line = ' ENDPROCEDURE is_this_parameter_ok; /* comments */'
            expected = True
            result = is_strict_procedure_end(line, 'is_this_parameter_ok')
            self.assertEqual(expected, result)


        def test_procedure_end_true(self):
            line = ' ENDPROCEDURE is_this_parameter_ok; /* comments */'
            expected = True
            result = is_an_procedure_end(line)
            self.assertEqual(expected, result)


        def test_procedure_end_false(self):
            line = ' PROCEDURE is_this_parameter_ok; /* comments */'
            expected = False
            result = is_an_procedure_end(line)
            self.assertEqual(expected, result)

    def test():
        text = 'PROCEDURE bcd_to_wordnum__r;'
        print get_procedure_name('PROCEDURE bcd_to_wordnum__r;')

    unittest.main()
    # test()