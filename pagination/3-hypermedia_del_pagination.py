#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination module.
"""
import csv
import math
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieve a page of data starting from a specific index,
        handling potential deletions in the dataset.

        Args:
            index (int): The starting index of the page.
            page_size (int): The number of items to return.

        Returns:
            Dict: A dictionary containing index,
              next_index, page_size, and data.
        """
        # 1. Verification of index range
        indexed_data = self.indexed_dataset()
        assert index is not None and 0 <= index < len(indexed_data)

        data = []
        current_index = index

        # 2. Fetch data: we skip missing keys until we have 'page_size' items
        while len(data) < page_size and current_index < len(indexed_data):
            item = indexed_data.get(current_index)
            if item is not None:
                data.append(item)
            current_index += 1

        # 3. The next index to query is where the loop stopped
        if current_index < len(indexed_data):
            next_index = current_index
        else:
            None

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }
