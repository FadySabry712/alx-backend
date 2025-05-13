#!/usr/bin/env python3
""" Simple pagination """
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """return a tuple of size two containing a start index and an end index"""
    start = (page - 1) * page_size
    return (start, start + page_size)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # skip header

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return the appropriate page of the dataset.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows for the requested page.
        """
        # Validate input
        assert isinstance(page, int) and page > 0,
        assert isinstance(page_size, int) and page_size > 0,


        # Get start and end indexes
        start, end = index_range(page, page_size)

        # Retrieve the dataset
        dataset = self.dataset()

        # Return the slice, or empty list if out of bounds
        return dataset[start:end]
