#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 7/05/23 10:57
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : EncryptData.py
from base64 import urlsafe_b64decode, urlsafe_b64encode

from Crypto.Cipher import AES


class EncryptData:
    def __init__(self, key):
        self.key = urlsafe_b64decode(key)  # 初始化**
        self.length = AES.block_size  # 初始化数据块大小
        self.aes = AES.new(self.key, AES.MODE_ECB)  # 初始化AES,ECB模式的实例
        # 截断函数，去除填充的字符
        self.unpad = lambda date: date[0:-ord(date[-1])]

    def pad(self, text):
        """
        #填充函数，使被加密数据的字节码长度是block_size的整数倍
        """
        count = len(text.encode('utf-8'))
        add = self.length - (count % self.length)
        text = text + (chr(add) * add)
        return text

    def encrypt(self, encrData):  # 加密函数
        res = self.aes.encrypt(self.pad(encrData).encode("utf8"))
        msg = str(urlsafe_b64encode(res), encoding="utf8")
        return msg

    def decrypt(self, decrData):  # 解密函数
        res = urlsafe_b64decode(decrData.encode("utf8"))
        msg = self.aes.decrypt(res).decode("utf8")
        return self.unpad(msg)
