import os

TEST_PATH = os.path.dirname(__file__)
DUMMY_PATH = os.path.join(TEST_PATH, '_dummy')

CATFISH_PREPARE = os.path.join(DUMMY_PATH, 'test_catfish_prepare')
CATFISH_SWIM = os.path.join(DUMMY_PATH, 'test_catfish_swim')
READ_SCRIPT_PATH = os.path.join(DUMMY_PATH, 'test_read_script')
PARSE_SWIPL_PATH = os.path.join(DUMMY_PATH, 'test_parse_swipl')
VALIDATE_SWIPL_PATH = os.path.join(DUMMY_PATH, 'test_validate_swipl')
