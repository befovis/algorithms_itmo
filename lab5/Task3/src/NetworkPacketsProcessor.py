# Lab5/Task3/src/NetworkPacketsProcessor.py

"""Module for processing network packets with buffer constraints."""

from typing import List, Tuple


class NetworkPacketsProcessor:
    """
    A class to calculate the processing start time for each network packet.
    """

    @staticmethod
    def network_packets(buffer_size: int, packets: List[Tuple[int, int]]) -> List[str]:
        """
        Calculates the start processing time for each packet.

        :param buffer_size: Size of the buffer.
        :param packets: List of packets as tuples (arrival_time, processing_time).
        :return: List of start processing times as strings, or '-1' if the packet is dropped.
        """
        buffer: List[int] = []
        start_times: List[str] = []

        for arrival_time, processing_time in packets:
            # Remove packets that have been processed by the arrival time
            while buffer and buffer[0] <= arrival_time:
                buffer.pop(0)

            if len(buffer) >= buffer_size:
                start_times.append('-1')
            else:
                if not buffer:
                    start_time = arrival_time
                else:
                    start_time = buffer[-1]
                start_times.append(str(start_time))
                buffer.append(start_time + processing_time)
        return start_times
