# -*- coding: utf-8 -*-
# Copyright (C)2016 Noe Nieto

import logging, os, zc.buildout
import zc.recipe.egg

class Recipe(object):
    """Downloads, compiles, installs and configures beanstalkd"""

    def __init__(self, buildout, name, options):
        self.name, self.options, self.buildout = name, options, buildout
        self.port = options.get('port', '1025')
        self.ip = options.get('ip', '127.0.0.1')
        self.backend = options.get('backend', 'memory')
        self.db_path = options.get('db-path', os.path.join(
            buildout['buildout']['directory'], 'parts', name
        ))

    def install(self):
        """Installer"""
        # Return files that were created by the recipe. The buildout
        # will remove all returned files upon reinstall.

    def update(self):
        return self._install_script()