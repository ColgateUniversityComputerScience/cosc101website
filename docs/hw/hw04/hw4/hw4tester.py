import sys
import os
import re
import importlib
import contextlib
import unittest
import difflib
import builtins
from io import StringIO


class mocked_input(contextlib.ContextDecorator):
    def __init__(self, inputs=[], write_prompt=True, write_input=True):
        self._inputs = iter(inputs)
        self._write_prompt = write_prompt
        self._write_input = write_input
        self._realinput = builtins.input

    def _fake_input(self, prompt=''):
        try:
            _input = str(next(self._inputs))
            if self._write_prompt:
                sys.stdout.write(prompt)
            if self._write_input:
                sys.stdout.write(_input + '\n')
            return _input
        except StopIteration:
            raise IOError('Received more calls to input() than expected!  (Your code called input() more times than was expected by the tester.)')

    def __enter__(self):
        builtins.input = self._fake_input

    def __exit__(self, *exc):
        builtins.input = self._realinput
        return False


def run_program(filename, inputs=[], write_input=True, run_main=False):
    fake_stdout = StringIO()
    assert filename.endswith('.py')
    directory, filename = os.path.split(filename)
    module_name = filename.replace('.py', '')
    sys.path.insert(0, directory)
    if module_name in sys.modules:    # so ugly: check if already imported
        del sys.modules[module_name]  # force "hard" reload

    with contextlib.redirect_stdout(fake_stdout):
        with mocked_input(inputs, write_input):
            module = importlib.import_module(module_name)
            if run_main:
                func = getattr(module, 'main')
                func()
    output = fake_stdout.getvalue()
    return output

def run_function(filename, func_name, inputs=[], write_input=True):
    fake_stdout = StringIO()
    assert filename.endswith('.py')
    directory, filename = os.path.split(filename)
    module_name = filename.replace('.py', '')
    sys.path.insert(0, directory)
    if module_name in sys.modules:    # so ugly: check if already imported
        del sys.modules[module_name]  # force "hard" reload

    with contextlib.redirect_stdout(fake_stdout):
        with mocked_input(inputs, write_input):
            module = importlib.import_module(module_name)
    func = getattr(module, func_name)
    retval = func(*inputs)
    output = fake_stdout.getvalue()
    return output, retval

class TestProgram(unittest.TestCase):
    def compareProgramOutputs(self, program_name, template,
                              template_kwargs, program_inputs, run_main=False):
        msg = "\nError!  Expected to find a file named {0}\n"
        msg += "But could not find this file.  Make sure it\n"
        msg += "is located in the same folder as the test program."
        msg = msg.format(program_name)
        self.assertTrue(os.path.isfile(program_name), msg)
        expected = template.format(**template_kwargs)
        inputs = [template_kwargs[in_name] for in_name in program_inputs]
        student_output = run_program(program_name, inputs, run_main=run_main)
        expected = expected.strip()
        student_output = student_output.strip()
        htmlout = program_name + ".html"
        if os.path.exists(htmlout):
            os.unlink(htmlout)

        msg = "\nUnexpected output executing: {0}\n"
        msg += "Expected to see this:\n\n{1}\n\n"
        msg += "Instead saw this:\n\n{2}\n"
        msg += "View a detailed output comparison in {0}.html."
        msg = msg.format(program_name, expected, student_output)

        if expected != student_output:
            diff = difflib.HtmlDiff(tabsize=4, wrapcolumn=40).make_file(expected.splitlines(keepends=True),student_output.splitlines(keepends=True), fromdesc="Expected output", todesc="Your program's output")
            with open("{}.html".format(program_name), "w") as outfile:
                outfile.write(diff)

        self.assertEqual(expected, student_output, msg)

class WaterTests(TestProgram):
    FILENAME = 'hw4_water.py'

    def checkValidMeterReading(self, reading, expected):
        _,result = run_function(WaterTests.FILENAME, "valid_meter_reading", [reading], write_input=False)
        self.assertEqual(result, expected, "valid_meter_reading('{}')".format(reading))
    
    def testValidMeterReading(self):
        for reading, expected in [('000000000',True), ('999999999',True), ('00000000x',False),
                                  ('11111111', False) ]:
            self.checkValidMeterReading(reading, expected)
    
    def checkUsage(self, begin, end, expected):
        _,result = run_function(WaterTests.FILENAME, "water_used", [begin, end], write_input=False)
        self.assertEqual(result, expected, "water_used({},{})".format(begin, end))
    
    def testWaterUsage(self):
        for begin,end,expected in [ ('000000000','000000000',0),
                                    ('000000000','000000010',1),
                                    ('000000009','000000011',0.2),
                                    ('999999999','000000000',0.1),
                                    ]:
            self.checkUsage(begin, end, expected)
    
    def checkBillAmount(self, code, usage, expected):
        _,result = run_function(WaterTests.FILENAME, "compute_bill_amount", [code, usage], write_input=False)
        self.assertEqual(result, expected, "compute_bill_amount('{}',{})".format(code, usage))

    def testBillAmount(self):
        for begin,end,expected in [ ('r', 0, 5),
                                    ('r', 10, 5+10*0.0005),
                                    ('c', 0, 1000),
                                    ('c', 4000000, 1000),
                                    ('c', 4000001, 1000+0.00025),
                                    ('c', 4000100, 1000+0.025),
                                    ('i', 0, 1000),
                                    ('i', 4000000, 1000),
                                    ('i', 4000001, 2000),
                                    ('i', 4000001, 2000),
                                    ('i', 10000000, 2000),
                                    ('i', 10000001, 2000+0.00025),
                                    ('i', 10000100, 2000+0.025),
                                    ]:
            self.checkBillAmount(begin, end, expected)
    
    def testMain1(self):
        template = '''How many customers? {i}
Code for customer {i}: {code}
Beginning meter reading for customer {i}: {begin}
Ending meter reading for customer {i}: {end}
Customer {i}: 
  Code: {code}
  Usage: {usage}
  Bill: ${bill}
Total amount billed: ${bill}'''
        kwargs = {'i':1, 'begin':'000000000','end':'000000010','code':'r','usage':round(1.0,1), 
                    'bill':round(5+0.0005*1,2)}
        self.compareProgramOutputs(WaterTests.FILENAME, template, kwargs, ['i','code','begin','end'], run_main=True)

    def testMain2(self):
        template = '''How many customers? {n}
Code for customer 1: {code1}
Beginning meter reading for customer 1: {begin1}
Ending meter reading for customer 1: {end1}
Customer 1: 
  Code: {code1}
  Usage: {usage1:.1f}
  Bill: ${bill1}
Code for customer 2: {code2}
Beginning meter reading for customer 2: {begin2}
Ending meter reading for customer 2: {end2}
Customer 2: 
  Code: {code2}
  Usage: {usage2:.1f}
  Bill: ${bill2}
Total amount billed: ${totbill}'''
        kwargs = {'n':2, 'begin1':'000000000','end1':'000000010','code1':'r','usage1':round(1.0,1), 
                    'bill1':round(5+0.0005*1,2),
                    'begin2':'000000010','end2':'600000010','usage2':round(60000000,2), 
                    'bill2':round(15000.0,2), 'code2':'c',
                    'totbill':round(15005.0,2)}
        self.compareProgramOutputs(WaterTests.FILENAME, template, kwargs, ['n','code1','begin1','end1','code2','begin2','end2'], run_main=True)

    def testMain3(self):
        template = '''How many customers? {n}
Total amount billed: $0
'''
        kwargs = {'n':-1}
        self.compareProgramOutputs(WaterTests.FILENAME, template, kwargs, ['n'], run_main=True)

    def testMain4(self):
        template = '''How many customers? {n}
Code for customer 1: {code}
Invalid customer code
Total amount billed: $0
'''
        kwargs = {'n':1,'code':'x'}
        self.compareProgramOutputs(WaterTests.FILENAME, template, kwargs, ['n','code'], run_main=True)

    def testMain5(self):
        template = '''How many customers? {n}
Code for customer 1: {code}
Beginning meter reading for customer 1: {begin}
Invalid begin reading
Total amount billed: $0
'''
        kwargs = {'n':1,'code':'r','begin':'012345678x'}
        self.compareProgramOutputs(WaterTests.FILENAME, template, kwargs, ['n','code','begin'], run_main=True)

    def testMain6(self):
        template = '''How many customers? {n}
Code for customer 1: {code}
Beginning meter reading for customer 1: {begin}
Ending meter reading for customer 1: {end}
Invalid end reading
Total amount billed: $0
'''
        kwargs = {'n':1,'code':'r','begin':'012345678','end':'00000000'}
        self.compareProgramOutputs(WaterTests.FILENAME, template, kwargs, ['n','code','begin','end'], run_main=True)

    def testMain7(self):
        template = '''How many customers? {n}
Code for customer 1: {code1}
Beginning meter reading for customer 1: {begin1}
Invalid begin reading
Code for customer 2: {code2}
Beginning meter reading for customer 2: {begin2}
Ending meter reading for customer 2: {end2}
Customer 2: 
  Code: {code2}
  Usage: {usage2:.1f}
  Bill: ${bill2}
Total amount billed: ${totbill}'''
        kwargs = {'n':2, 'begin1':'00000000','code1':'r',
                    'begin2':'000000010','end2':'600000010','usage2':round(60000000,2), 
                    'bill2':round(15000.0,2), 'code2':'c',
                    'totbill':round(15000.0,2)}
        self.compareProgramOutputs(WaterTests.FILENAME, template, kwargs, ['n','code1','begin1','code2','begin2','end2'], run_main=True)


if __name__ == '__main__':
    unittest.main(verbosity=10)
