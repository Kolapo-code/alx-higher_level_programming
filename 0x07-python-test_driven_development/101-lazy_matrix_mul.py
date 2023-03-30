#!/usr/bin/python3
"""Lazy multiplication module."""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Inside the method.

    Args:
        m_a: first matrix
        m_b: second_matrix
    """
    return np.matmul(m_a, m_b)
