import maya.cmds as mc
from maya.mel import eval as meval

############################################
# GET WEIGHTS OF A JOINT
############################################
# select joint, then mesh
bndJnt, mesh = mc.ls(os=True)[:2]

vtxCount = mc.polyEvaluate(mesh, v=True)
skn = meval('findRelatedSkinCluster("%s")' % mesh)

weights = []

for vtxId in range(vtxCount):
	weight = mc.skinPercent(skn, '%s.vtx[%d]' % (mesh, vtxId), transform=bndJnt, q=True, v=True)
	weights.append(weight)
	
print weights
