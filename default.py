# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# XBMC entry point
# ------------------------------------------------------------

import os
import sys
import xbmc

# functions that on kodi 19 moved to xbmcvfs
try:
    import xbmcvfs
    xbmc.translatePath = xbmcvfs.translatePath
    xbmc.validatePath = xbmcvfs.validatePath
    xbmc.makeLegalFilename = xbmcvfs.makeLegalFilename
except:
    pass
from platformcode import config, logger

logger.info("init...")


librerias = xbmc.translatePath(os.path.join(config.get_runtime_path(), 'lib'))
sys.path.insert(0, librerias)

if 'mandrakodi' in xbmc.getInfoLabel('Container.FolderPath'):
    from platformcode.platformtools import dialog_ok
    dialog_ok('Kodi on Demand', 'Non è consentito sfruttare KoD da add-on esterni')
    exit()

from platformcode import launcher

if sys.argv[2] == "":
    launcher.start()

launcher.run()
