'''
Lambda function to verify validity of the Reward function
@author: Sunil Mallya
@author: Manish Manwani
'''

import inspect
import json
import re
import traceback
import unittest

import sys


class DeepRacerError(Exception):
    def __init__(self, **kwargs):
        self._dict = kwargs

    def __str__(self):
        return json.dumps(self._dict)


def wrap(fn):
    def f(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except DeepRacerError:
            raise
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            tb = traceback.extract_tb(exc_traceback)[-1]
            exc = traceback.format_exc().splitlines()[-1]
            is_syntax_error = isinstance(exc_value, SyntaxError)
            filename = exc_value.filename if is_syntax_error else tb[0]
            lineno = exc_value.lineno if is_syntax_error else tb[1]
            line = exc_value.text if is_syntax_error else tb[3]
            error, message = exc.split(":")

            type = 'SYNTAX_ERROR' if is_syntax_error \
                else 'IMPORT_ERROR' if isinstance(exc_value, ImportError) \
                else 'TEST_FAILURE'
            _dict = {'type': type,
                     'message': message.strip(),
                     'line': line.strip(),
                     }
            if filename.endswith('reward_function.py'):
                _dict['lineNumber'] = lineno

            raise DeepRacerError(**_dict)

    return f


class TestSyntax(unittest.TestCase):
    @wrap
    def test_syntax(self):
        from reward_function import reward_function


class TestRewardFunction(unittest.TestCase):
    @wrap
    def setUp(self):
        from reward_function import reward_function

        self.rf = reward_function

        # reinvent track waypoints
        self.waypoints = [[0.25, 0.15, 0.0],
                          [0.333, 0.15, 0.0],
                          [0.417, 0.15, 0.0],
                          [0.5, 0.15, 0.0],
                          [0.583, 0.15, 0.0],
                          [0.667, 0.15, 0.0],
                          [0.75, 0.15, 0.0],
                          [0.833, 0.15, 0.0],
                          [0.917, 0.15, 0.35],
                          [0.975, 0.188, 0.85],
                          [1.013, 0.3, 1.55],
                          [1.008, 0.375, 2.0],
                          [0.992, 0.425, 2.25],
                          [0.958, 0.475, 2.74],
                          [0.917, 0.55, 3.14],
                          [0.833, 0.5, 3.14],
                          [0.75, 0.5, 3.14],
                          [0.708, 0.512, 2.84],
                          [0.667, 0.525, 2.49],
                          [0.583, 0.688, 2.19],
                          [0.5, 0.875, 2.19],
                          [0.467, 0.938, 2.4],
                          [0.433, 0.975, 2.8],
                          [0.4, 1.0, 3.15],
                          [0.333, 1.0, -3.08],
                          [0.25, 0.99, -3.08],
                          [0.208, 0.988, -2.94],
                          [0.167, 0.975, -2.6],
                          [0.133, 0.938, -2.25],
                          [0.092, 0.812, -1.4],
                          [0.117, 0.637, -1.4],
                          [0.15, 0.388, -1.4],
                          [0.16, 0.3, -1.2],
                          [0.183, 0.225, -0.85],
                          [0.217, 0.177, -0.55]]
        self.valid_params = {'on_track': True,
                             'x': 0,
                             'y': 0,
                             'distance_from_center': 0,
                             'car_orientation': -3.14,
                             'progress': 0,
                             'steps': 1,
                             'throttle': 0.1,
                             'steering': 0.2,
                             'track_width': 2.5,
                             'waypoints': self.waypoints,
                             'closest_waypoint': 0}

        self.start_car = {'on_track': True,
                          'x': 0,
                          'y': 0,
                          'distance_from_center': 0,
                          'car_orientation': 0,
                          'progress': 0,
                          'steps': 1,
                          'throttle': 0.1,
                          'steering': 0.2,
                          'track_width': 2.5,
                          'waypoints': self.waypoints,
                          'closest_waypoint': 0}

        self.progress_car = {'on_track': True,
                             'x': 0.5,
                             'y': 0.5,
                             'distance_from_center': 0.3,
                             'car_orientation': -3.14,
                             'progress': 0.5,
                             'steps': 100,
                             'throttle': 0.1,
                             'steering': 0.2,
                             'track_width': 2.5,
                             'waypoints': self.waypoints,
                             'closest_waypoint': 3}

        self.off_track_car = {'on_track': False,
                              'x': 1,
                              'y': 1,
                              'distance_from_center': 1,
                              'car_orientation': -3.14,
                              'progress': 0,
                              'steps': 1,
                              'throttle': 0.1,
                              'steering': 0.2,
                              'track_width': 2.5,
                              'waypoints': self.waypoints,
                              'closest_waypoint': 5}

        self.finish_car = {'on_track': True,
                           'x': 0.9,
                           'y': 0.9,
                           'distance_from_center': 0,
                           'car_orientation': 0,
                           'progress': 1,
                           'steps': 10000,
                           'throttle': 0.1,
                           'steering': 0.2,
                           'track_width': 2.5,
                           'waypoints': self.waypoints,
                           'closest_waypoint': 34}

        self._reward_function_args = ['on_track', 'x', 'y', 'distance_from_center', 'car_orientation', 'progress', 'steps', 'throttle',
                                      'steering', 'track_width', 'waypoints', 'closest_waypoint']

        self._method_signature = "reward_function({})".format(",".join(self._reward_function_args))

    @wrap
    def test_reward_function_signature(self):
        actual = list(inspect.signature(self.rf).parameters.keys())
        expected = self._reward_function_args

        if len(actual) > len(expected):
            self.fail("Invalid method signature. Found more arguments: {}".format(
                set(actual) - set(expected)
            ))
        elif len(expected) > len(actual):
            self.fail("Invalid method signature. Missing arguments: {}".format(
                set(expected) - set(actual)
            ))

    @wrap
    def warn_reward_function_signature(self):
        actual = list(inspect.signature(self.rf).parameters.keys())
        expected = self._reward_function_args

        if len(actual) == len(expected):
            for a, b in zip(actual, expected):
                if a != b:
                    self.fail("Method signature may be invalid. Found: {}, Expected: {}".format(a, b))

    @wrap
    def test_all_imported_modules(self):
        self.rf(*list(self.valid_params.values()))

    @wrap
    def test_return_type(self):
        reward = self.rf(*list(self.valid_params.values()))
        if not isinstance(reward, float):
            self.fail("Method returned non-floating type value: {}".format(reward))

    @wrap
    def test_reward_range(self):
        reward = self.rf(*list(self.valid_params.values()))
        if not self._reward_in_range(reward):
            self.fail("Reward score out of range. Reward: {}, range: {}".format(reward, "[-1e5, 1e5]"))

    @staticmethod
    def _reward_in_range(reward):
        return isinstance(reward, float) and -1e5 <= reward <= 1e5

    @wrap
    def test_start_car(self):
        reward = self.rf(*list(self.start_car.values()))
        if not self._reward_in_range(reward):
            self.fail("Vehicle failed at start position. Reward: {}".format(reward))

    @wrap
    def test_progress_car(self):
        reward = self.rf(*list(self.progress_car.values()))
        if not self._reward_in_range(reward):
            self.fail("Vehicle failed to make progress. Reward: {}".format(reward))

    @wrap
    def test_off_track_car(self):
        reward = self.rf(*list(self.off_track_car.values()))
        if not self._reward_in_range(reward):
            self.fail("Off-track vehicle failed to make progress. Reward: {}".format(reward))

    @wrap
    def test_finish_car(self):
        reward = self.rf(*list(self.finish_car.values()))
        if not self._reward_in_range(reward):
            self.fail("Vehicle failed to make it to end of track. Reward: {}".format(reward))

    def fail(self, msg=None):
        raise DeepRacerError(message=msg, type='TEST_FAILURE')


def fail_fast_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestSyntax('test_syntax'))
    suite.addTest(TestRewardFunction('test_reward_function_signature'))
    suite.addTest(TestRewardFunction('test_all_imported_modules'))
    suite.addTest(TestRewardFunction('test_return_type'))
    return suite


def functional_test_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestRewardFunction('warn_reward_function_signature'))
    suite.addTest(TestRewardFunction('test_reward_range'))
    suite.addTest(TestRewardFunction('test_start_car'))
    suite.addTest(TestRewardFunction('test_progress_car'))
    suite.addTest(TestRewardFunction('test_off_track_car'))
    suite.addTest(TestRewardFunction('test_finish_car'))
    return suite


def lambda_handler(event, context):
    errors = process_results(unittest.TextTestRunner(failfast=True).run(fail_fast_suite())) \
             or process_results(unittest.TextTestRunner().run(functional_test_suite()))
    return errors


def process_results(test_results):
    return list(map(lambda e: extract_failure_message(e[1]), test_results.errors + test_results.failures))


def extract_failure_message(txt):
    line = txt.splitlines()[-1]
    try:
        return json.loads(re.search('DeepRacerError: (.+)', line).group(1))
    except:
        pass
    return json.loads(str(DeepRacerError(message=line, type='TEST_FAILURE')))
