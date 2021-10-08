# -*- coding: utf-8 -*-

#
# Nico Uploader Core
#
# github: https://github.com/xx-acg/
# author: xx-acg
# create: 2021/10/8
# xxacg - 超多galgame资源 ： https://xx-acg.com/
#

# 用于实验想法 :( 可能写的很烂 因为这是我的python出作品

import logging
import sys

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(name)s] %(levelname)s : %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S'
)


def sub_package(args):
    logging.info("Sub-Package")


def build_package(args):
    logging.info("Build-Package")


def upload(args):
    logging.info("Upload")


def download(args):
    logging.info("Download")


def main():
    args = sys.argv
    if len(args) == 1:
        logging.error("nico-upload-core [sub/build/upload/download]")
    else:
        action = args[1]
        if action == "sub":
            sub_package(args)
        elif action == "build":
            build_package(args)
        elif action == "upload":
            upload(args)
        elif action == "download":
            download(args)
        else:
            logging.error("nico-upload-core [upload/download]")


if __name__ == '__main__':
    main()
