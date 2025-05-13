#!/usr/bin/env python3
""" index_range func """


def index_range(page: int, page_size: int) -> tuple:
    """ tuple of size two containing a start index and an end index """
    start = (page - 1) * page_size
    return (start, start + page_size)
