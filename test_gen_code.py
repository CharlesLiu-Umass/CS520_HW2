# %%
#Import all GEMINI generated responses
import GEMINI_generated_code.CoT.gen_code_1 as GemCot1
import GEMINI_generated_code.CoT.gen_code_2 as GemCot2
import GEMINI_generated_code.CoT.gen_code_3 as GemCot3
import GEMINI_generated_code.CoT.gen_code_4 as GemCot4
import GEMINI_generated_code.CoT.gen_code_5 as GemCot5
import GEMINI_generated_code.CoT.gen_code_6 as GemCot6
import GEMINI_generated_code.CoT.gen_code_7 as GemCot7
import GEMINI_generated_code.CoT.gen_code_8 as GemCot8
import GEMINI_generated_code.CoT.gen_code_9 as GemCot9
import GEMINI_generated_code.CoT.gen_code_10 as GemCot10

import GEMINI_generated_code.SCoT.gen_code_1 as GemSCot1
import GEMINI_generated_code.SCoT.gen_code_2 as GemSCot2
import GEMINI_generated_code.SCoT.gen_code_3 as GemSCot3
import GEMINI_generated_code.SCoT.gen_code_4 as GemSCot4
import GEMINI_generated_code.SCoT.gen_code_5 as GemSCot5
import GEMINI_generated_code.SCoT.gen_code_6 as GemSCot6
import GEMINI_generated_code.SCoT.gen_code_7 as GemSCot7
import GEMINI_generated_code.SCoT.gen_code_8 as GemSCot8
import GEMINI_generated_code.SCoT.gen_code_9 as GemSCot9
import GEMINI_generated_code.SCoT.gen_code_10 as GemSCot10
#Import all GPT generated responses
import GPT_generated_code.CoT.gen_code_1 as GPTCot1
import GPT_generated_code.CoT.gen_code_2 as GPTCot2
import GPT_generated_code.CoT.gen_code_3 as GPTCot3
import GPT_generated_code.CoT.gen_code_4 as GPTCot4
import GPT_generated_code.CoT.gen_code_5 as GPTCot5
import GPT_generated_code.CoT.gen_code_6 as GPTCot6
import GPT_generated_code.CoT.gen_code_7 as GPTCot7
import GPT_generated_code.CoT.gen_code_8 as GPTCot8
import GPT_generated_code.CoT.gen_code_9 as GPTCot9
import GPT_generated_code.CoT.gen_code_10 as GPTCot10

import GPT_generated_code.SCoT.gen_code_1 as GPTSCot1
import GPT_generated_code.SCoT.gen_code_2 as GPTSCot2
import GPT_generated_code.SCoT.gen_code_3 as GPTSCot3
import GPT_generated_code.SCoT.gen_code_4 as GPTSCot4
import GPT_generated_code.SCoT.gen_code_5 as GPTSCot5
import GPT_generated_code.SCoT.gen_code_6 as GPTSCot6
import GPT_generated_code.SCoT.gen_code_7 as GPTSCot7
import GPT_generated_code.SCoT.gen_code_8 as GPTSCot8
import GPT_generated_code.SCoT.gen_code_9 as GPTSCot9
import GPT_generated_code.SCoT.gen_code_10 as GPTSCot10
#Import all tests
import tests_unit.test_cases.test_1 as test_1
import tests_unit.test_cases.test_2 as test_2
import tests_unit.test_cases.test_3 as test_3
import tests_unit.test_cases.test_4 as test_4
import tests_unit.test_cases.test_5 as test_5
import tests_unit.test_cases.test_6 as test_6
import tests_unit.test_cases.test_7 as test_7
import tests_unit.test_cases.test_8 as test_8
import tests_unit.test_cases.test_9 as test_9
import tests_unit.test_cases.test_10 as test_10

# Evaluate function to check generated code passes unit test
def evaluate(fn, test_cases):
    for args, expected in test_cases:
        result = fn(*args)
        assert result == expected or list(result) == expected, f"{fn.__name__}{args} = {result}, expected {expected}"

# Test functions to be run by pytest
#Problem 1
def test_GemCot1():
    evaluate(GemCot1.has_close_elements,test_1.TEST_CASES)
def test_GemSCot1():
    evaluate(GemSCot1.has_close_elements,test_1.TEST_CASES)
def test_GPTCot1():
    evaluate(GPTCot1.has_close_elements,test_1.TEST_CASES)
def test_GPTSCot1():
    evaluate(GPTSCot1.has_close_elements,test_1.TEST_CASES)
#Problem 2
def test_GemCot2():
    evaluate(GemCot2.separate_paren_groups,test_2.TEST_CASES)
def test_GemSCot2():
    evaluate(GemSCot2.separate_paren_groups,test_2.TEST_CASES)
def test_GPTCot2():
    evaluate(GPTCot2.separate_paren_groups,test_2.TEST_CASES)
def test_GPTSCot2():
    evaluate(GPTSCot2.separate_paren_groups,test_2.TEST_CASES)
#Problem 3
def test_GemCot3():
    evaluate(GemCot3.max_accordion_length,test_3.TEST_CASES)
def test_GemSCot3():
    evaluate(GemSCot3.max_accordion_length,test_3.TEST_CASES)
def test_GPTCot3():
    evaluate(GPTCot3.max_accordion_length,test_3.TEST_CASES)
def test_GPTSCot3():
    evaluate(GPTSCot3.max_accordion_length,test_3.TEST_CASES)
# #Problem 4
# def test_GemCot4():
#     evaluate(GemCot4.minimum_traps,test_4.TEST_CASES)
# def test_GemSCot4():
#     evaluate(GemSCot4.solve,test_4.TEST_CASES)
# def test_GPTCot4():
#     evaluate(GPTCot4.minimum_traps,test_4.TEST_CASES)
# def test_GPTSCot4():
#     evaluate(GPTSCot4.minimum_traps,test_4.TEST_CASES)
#Problem 5
def test_GemCot5():
    evaluate(GemCot5.calculate_martian_days_off,test_5.TEST_CASES)
def test_GemSCot5():
    evaluate(GemSCot5.calculate_martian_days_off,test_5.TEST_CASES)
def test_GPTCot5():
    evaluate(GPTCot5.martian_days_off,test_5.TEST_CASES)
def test_GPTSCot5():
    evaluate(GPTSCot5.martian_days_off,test_5.TEST_CASES)
#Problem 6
def test_GemCot6():
    evaluate(GemCot6.check_vasyas_sequence,test_6.TEST_CASES)
def test_GemSCot6():
    evaluate(GemSCot6.check_sequence_element,test_6.TEST_CASES)
def test_GPTCot6():
    evaluate(GPTCot6.check_sequence,test_6.TEST_CASES)
def test_GPTSCot6():
    evaluate(GPTSCot6.is_b_in_sequence,test_6.TEST_CASES)
#Problem 7
def test_GemCot7():
    evaluate(GemCot7.find_next_palindrome_time,test_7.TEST_CASES)
def test_GemSCot7():
    evaluate(GemSCot7.get_next_palindrome_time_minutes,test_7.TEST_CASES)
def test_GPTCot7():
    evaluate(GPTCot7.time_to_palindrome,test_7.TEST_CASES)
def test_GPTSCot7():
    evaluate(GPTSCot7.min_sleep_time,test_7.TEST_CASES)
#Problem 8
def test_GemCot8():
    evaluate(GemCot8.check_s_palindrome,test_8.TEST_CASES)
def test_GemSCot8():
    evaluate(GemSCot8.is_s_palindrome,test_8.TEST_CASES)
def test_GPTCot8():
    evaluate(GPTCot8.is_s_palindrome,test_8.TEST_CASES)
def test_GPTSCot8():
    evaluate(GPTSCot8.is_s_palindrome,test_8.TEST_CASES)
#Problem 9
def test_GemCot9():
    evaluate(GemCot9.min_typing_operations,test_9.TEST_CASES)
def test_GemSCot9():
    evaluate(GemSCot9.min_typing_operations,test_9.TEST_CASES)
def test_GPTCot9():
    evaluate(GPTCot9.min_operations,test_9.TEST_CASES)
def test_GPTSCot9():
    evaluate(GPTSCot9.minimum_operations,test_9.TEST_CASES)
#Problem 10
def test_GemCot10():
    evaluate(GemCot10.can_weight_item,test_10.TEST_CASES)
def test_GemSCot10():
    evaluate(GemSCot10.solve,test_10.TEST_CASES)
def test_GPTCot10():
    evaluate(GPTCot10.can_balance,test_10.TEST_CASES)
def test_GPTSCot10():
    evaluate(GPTSCot10.can_weight,test_10.TEST_CASES)