#!/usr/bin/env python
import sys
import os


def readJsonFile(file):
    try:
        while(True):
            f=open(file)
            body = f.readline()
            print("contenido de archivo encontrado \n", body)

    except OSError as err:
        print("OS error: {0}".format(err))
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise



if __name__ == "__main__":
    readJsonFile('entrada/entrada.json')

