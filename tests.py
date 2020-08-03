import unittest

from exercise import top_ten_pages_requested, percentage_success_requests, percentage_unsuccess_requests, top_ten_unsuccessfull_page_requests, top_ten_hosts_with_the_most_requests
from exercise import HOST, REQUEST, RESPONSE_CODE
import pandas as pd
import numpy as np

class TestSum(unittest.TestCase):

    #data for the first dataframe
    TEST_data_1 = [['129.329.42.42', '/page1', 200], ['129.543.2.42', '/dashboard.html', 203], ['129.329.42.42', '/image.png', 300], ['18.329.1.42', '/image.png', 500],
                   ['129.329.42.42', '/nasa/nasa.gif', 403], ['18.329.1.42', '/login/gfd', 404], ['18.329.1.42', '/logout', 200], ['129.329.42.42', '/login', 200],
                   ['129.329.42.42', '/dashboard.html', 200], ['129.329.42.42', '/page1', 200], ['129.329.42.42', '/page1', 403]]
    #dataframe initialized
    TEST_DF_1 = pd.DataFrame(TEST_data_1, columns = [HOST, REQUEST, RESPONSE_CODE])
    #data for the second dataframe
    TEST_data_2 = [['129.329.42.42', '/page1', 200], ['','/dashboard.html', 203], ['129.329.42.42', '/image.png', 300], ['18.329.1.42', '/image.png', 500],
                   ['129.329.42.42', '/nasa/nasa.gif', 403], ['129.329.42.42', '/page1', 401]]
    #dataframe initialized
    TEST_DF_2 = pd.DataFrame(TEST_data_2, columns = [HOST, REQUEST, RESPONSE_CODE])

    def test_top_ten_pages_requested_df_1(self):
        result = top_ten_pages_requested(self.TEST_DF_1)
        data_expected = {REQUEST:['/page1', '/dashboard.html', '/login', '/login/gfd', '/logout'], 'count':[3, 2, 1, 1, 1]}

        # Create DataFrame
        expected_result = pd.DataFrame(data_expected, columns = [REQUEST, 'count'])
        pd.testing.assert_frame_equal(result, expected_result)


    def test_top_ten_pages_requested_df_2(self):
        result = top_ten_pages_requested(self.TEST_DF_2)
        data_expected = {REQUEST:['/page1', '/dashboard.html'], 'count':[2, 1]}

        # Create DataFrame
        expected_result = pd.DataFrame(data_expected, columns = [REQUEST, 'count'])
        pd.testing.assert_frame_equal(result, expected_result)


    def test_percentage_success_requests_df_1(self):
        result = percentage_success_requests(self.TEST_DF_1)
        self.assertEqual(result, 54.54545454545454)


    def test_percentage_success_requests_df_2(self):
        result = percentage_success_requests(self.TEST_DF_2)
        self.assertEqual(result, 33.333333333333329)


    def test_percentage_unsuccess_requests_df_1(self):
        result = percentage_unsuccess_requests(self.TEST_DF_1)
        self.assertEqual(result, 45.454545454545453)


    def test_percentage_unsuccess_requests_df_2(self):
        result = percentage_unsuccess_requests(self.TEST_DF_2)
        self.assertEqual(result, 66.666666666666657)


    def test_top_ten_unsuccessfull_page_requests_df_1(self):
        result = top_ten_unsuccessfull_page_requests(self.TEST_DF_1)
        data_expected = {REQUEST:['/login/gfd', '/page1'], 'count':[1, 1]}

        # Create DataFrame
        expected_result = pd.DataFrame(data_expected, columns = [REQUEST, 'count'])
        pd.testing.assert_frame_equal(result, expected_result)


    def test_top_ten_unsuccessfull_page_requests_df_2(self):
        result = top_ten_unsuccessfull_page_requests(self.TEST_DF_2)
        data_expected = {REQUEST:['/page1'], 'count':[1]}

        # Create DataFrame
        expected_result = pd.DataFrame(data_expected, columns = [REQUEST, 'count'])
        pd.testing.assert_frame_equal(result, expected_result)

    def test_top_ten_hosts_with_the_most_requests_df_1(self):
        result = top_ten_hosts_with_the_most_requests(self.TEST_DF_1)
        data_expected = {HOST:['129.329.42.42', '18.329.1.42', '129.543.2.42'], 'requests_count':[7, 3, 1]}

        # Create DataFrame
        expected_result = pd.DataFrame(data_expected, columns = [HOST, 'requests_count'])
        pd.testing.assert_frame_equal(result, expected_result)


    def test_top_ten_hosts_with_the_most_requests_df_2(self):
        result = top_ten_hosts_with_the_most_requests(self.TEST_DF_2)
        data_expected = {HOST:['129.329.42.42', '', '18.329.1.42'], 'requests_count':[4, 1, 1]}

        # Create DataFrame
        expected_result = pd.DataFrame(data_expected, columns = [HOST, 'requests_count'])
        pd.testing.assert_frame_equal(result, expected_result)


if __name__ == '__main__':
    unittest.main()
