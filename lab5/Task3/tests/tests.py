import unittest
import time
import tracemalloc
from lab5.Task3.src.NetworkPacketsProcessor import NetworkPacketsProcessor

class TestNetworkPacketsProcessor(unittest.TestCase):
    def test_given_packets_when_process_then_correct_start_times(self):
        # GIVEN
        processor = NetworkPacketsProcessor()
        buffer_size = 1
        packets = [(0,3),(3,3),(10,3)]
        tracemalloc.start()
        t_start = time.perf_counter()
        # WHEN
        res = processor.network_packets(buffer_size, packets)
        tracemalloc.stop()
        # THEN
        self.assertEqual(res, ['0', '3', '10'])
        self.assertLess(time.perf_counter() - t_start, 2)


if __name__ == '__main__':
    unittest.main()