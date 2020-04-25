#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conans import ConanFile, tools, CMake


class CefalConan(ConanFile):
    name = "cefal"
    version = "0.1.0"
    license = "MIT"
    author = "Alexander Zaitsev zamazan4ik@tut.by"
    url = "https://github.com/ZaMaZaN4iK/conan-cefal"
    homepage = "https://github.com/dkormalev/cefal"
    description = "(Concepts-enabled) Functional Abstraction Layer for C++"
    topics = ("cpp", "cpp20", "concepts", "functional-programming", "monad")
    no_copy_sources = True

    _source_subfolder = "source_subfolder"

    def source(self):
        checksum = "eb8693b986a66e21935937fd547cc00bc91420eb82ae8fef80ce1dcc6c5357fe"
        tools.get("{0}/archive/{1}.tar.gz".format(self.homepage, self.version), sha256=checksum)      
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self._source_subfolder)
        cmake.install()
        self.copy("LICENSE", dst="licenses", src=self._source_subfolder)

    def package_info(self):
        self.info.header_only()
