# better_zipfile

**本项目旨在对优化python中自带的zipfile，以处理mnbvc项目解压遇到的问题**

目前基于原始的zipfile有了以下两种优化：

1. 在读取文件名时，使用alan的charset-mnbvc库，支持更多种类型的文件内文件名编码。
2. 如果遇到文件尾部多余的数据时，自动处理掉尾部数据并正确读取。