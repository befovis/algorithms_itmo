# Lab6/Task4/src/AssocArrayProcessor.py

"""Module for processing operations on an associative array."""

from collections import OrderedDict
from typing import List


class AssocArrayProcessor:
    """
    A class to handle commands on an associative array.

    Supported commands:
    - put x y: Add or update the value for key x.
    - get x: Retrieve the value for key x or <none> if it doesn't exist.
    - prev x: Get the value of the key that was inserted immediately before key x.
    - next x: Get the value of the key that was inserted immediately after key x.
    - delete x: Remove the key x from the associative array.
    """

    @staticmethod
    def process_commands(commands: List[str]) -> List[str]:
        """
        Processes a list of commands on the associative array.

        :param commands: List of command strings.
        :return: List of results for 'get', 'prev', and 'next' commands.
        """
        assoc_map: OrderedDict[str, str] = OrderedDict()
        output_results: List[str] = []

        for command_line in commands:
            tokens = command_line.strip().split()
            operation = tokens[0]

            if operation == "put":
                key, value = tokens[1], tokens[2]
                assoc_map[key] = value

            elif operation == "get":
                key = tokens[1]
                retrieved_value = assoc_map.get(key, "<none>")
                output_results.append(retrieved_value)

            elif operation == "prev":
                key = tokens[1]
                if key in assoc_map:
                    keys_list = list(assoc_map.keys())
                    current_index = keys_list.index(key)
                    if current_index > 0:
                        prev_key = keys_list[current_index - 1]
                        output_results.append(assoc_map[prev_key])
                    else:
                        output_results.append("<none>")
                else:
                    output_results.append("<none>")

            elif operation == "next":
                key = tokens[1]
                if key in assoc_map:
                    keys_list = list(assoc_map.keys())
                    current_index = keys_list.index(key)
                    if current_index < len(keys_list) - 1:
                        next_key = keys_list[current_index + 1]
                        output_results.append(assoc_map[next_key])
                    else:
                        output_results.append("<none>")
                else:
                    output_results.append("<none>")

            elif operation == "delete":
                key = tokens[1]
                assoc_map.pop(key, None)

        return output_results
