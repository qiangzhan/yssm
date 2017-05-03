#print('init pipeline')

import __builtin__
exec(('import os.path;from maya import cmds;'
      'from maya import mel;import pymel.core as pm;'),
     vars(__builtin__))

# import setEnv
# setEnv.setEnv()

# import leadMel
# leadMel.leadMel()

import pymel.mayautils

import menu_yssm
#print 'create pipeline custom menu'
pymel.mayautils.executeDeferred(menu_yssm.loadMenu)
