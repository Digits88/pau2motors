__doc__ = """
The lists of joints defined here correspond to the angle array
"m_angles" in pau.msg. These keys are used in the config files to specify
which angles to extract from the incoming PAU messages.
"""
try:
    xrange
except NameError:
    xrange = range

_joint_list = ['R_Shoulder_Pitch','R_Shoulder_Roll','R_Shoulder_Yaw','R_Elbow','R_Wrist_Yaw','R_Wrist_Roll','R_Index_Finger','R_Middle_Finger',
'R_Ring_Finger','R_Pinky_Finger','R_Thumb_Finger','R_Thumb_Roll','R_Spreading','L_Shoulder_Pitch','L_Shoulder_Roll','L_Shoulder_Yaw','L_Elbow','L_Wrist_Yaw',
'L_Wrist_Roll','L_Index_Finger','L_Middle_Finger','L_Ring_Finger','L_Pinky_Finger','L_Thumb_Finger','L_Thumb_Roll','L_Spreading']


def _build_index(lst):
  """Build a dictionary mapping the given list values to their indices"""
  result = {}
  for i in xrange(len(lst)):
    result[lst[i]] = i
  return result

#Call _build_index() for every joint_list
_joint2index = [
  _build_index(joint_list)
  for joint_list in [_joint_list]
]

_current_dict = _joint2index[0]

def _get_dict_with(joint):
  """
  Gets the joint2index dictionary, which has the given joint in it out of
  available joint2index dictionaries.
  """
  result = None
  for dct in _joint2index:
    if joint in dct:
      result = dct
      break
  if result == None:
    raise KeyError("Joint '%s' not found." % joint)
  return result

def getIndex(joint):
  """Gets the index of the given joint string."""
  global _current_dict
  if not joint in _current_dict:
    _current_dict = _get_dict_with(joint)
  return _current_dict[joint]
