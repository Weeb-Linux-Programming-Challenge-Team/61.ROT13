#!/usr/bin/env python3
"""
Simple ROT13 encoding/decoding with Python
"""
import codecs


def encode(string: str):
    return codecs.encode(string, "rot_13")


def decode(string: str):
    return codecs.decode(string, "rot_13")
