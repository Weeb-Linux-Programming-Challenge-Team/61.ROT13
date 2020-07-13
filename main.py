#!/usr/bin/env python3
"""
Simple ROT13 encoding/decoding with Python
"""
import codecs


def encode(string: str):
    return codecs.encode(string, "rot_13")


def decode(string: str):
    return codecs.decode(string, "rot_13")


if __name__ == "__main__":
    mode = str(input("What are we doing today sire? (e)ncode or (d)ecode? "))
    if mode == "e":
        text = str(input("Enter text to encode: "))
        print("ROT13 Encoded text: {0}".format(encode(text)))
    elif mode == "d":
        text = str(input("Enter text to decode: "))
        print("ROT13 Decoded text: {0}".format(decode(text)))
    else:
        print("Unrecognized mode, exiting.")
        exit(0)
