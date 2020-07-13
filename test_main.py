#!/usr/bin/env python3
"""
Unit test for the ROT13 encoding/decoding code
"""
import main


class TestROT13:
    def test_decoding(self):
        assert "WeebLinux" == main.decode("JrroYvahk")

    def test_encoding(self):
        assert "JrroYvahk" == main.encode("WeebLinux")
