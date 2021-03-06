
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN ATTRIBUTE COMMENT ELLIPSIS EXAMPLE NEWLINE TABcode : attribute\n            | context\n            | attribute code\n            | context codeattribute : ATTRIBUTEcontext : ASSIGNcontext : COMMENTcontext : NEWLINEcontext : ELLIPSIScontext : TABcontext : EXAMPLE'
    
_lr_action_items = {'ATTRIBUTE':([0,2,3,4,5,6,7,8,9,10,],[4,4,4,-5,-6,-7,-8,-9,-10,-11,]),'ASSIGN':([0,2,3,4,5,6,7,8,9,10,],[5,5,5,-5,-6,-7,-8,-9,-10,-11,]),'COMMENT':([0,2,3,4,5,6,7,8,9,10,],[6,6,6,-5,-6,-7,-8,-9,-10,-11,]),'NEWLINE':([0,2,3,4,5,6,7,8,9,10,],[7,7,7,-5,-6,-7,-8,-9,-10,-11,]),'ELLIPSIS':([0,2,3,4,5,6,7,8,9,10,],[8,8,8,-5,-6,-7,-8,-9,-10,-11,]),'TAB':([0,2,3,4,5,6,7,8,9,10,],[9,9,9,-5,-6,-7,-8,-9,-10,-11,]),'EXAMPLE':([0,2,3,4,5,6,7,8,9,10,],[10,10,10,-5,-6,-7,-8,-9,-10,-11,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,],[0,-1,-2,-5,-6,-7,-8,-9,-10,-11,-3,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'code':([0,2,3,],[1,11,12,]),'attribute':([0,2,3,],[2,2,2,]),'context':([0,2,3,],[3,3,3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> code","S'",1,None,None,None),
  ('code -> attribute','code',1,'p_attributes','main.py',39),
  ('code -> context','code',1,'p_attributes','main.py',40),
  ('code -> attribute code','code',2,'p_attributes','main.py',41),
  ('code -> context code','code',2,'p_attributes','main.py',42),
  ('attribute -> ATTRIBUTE','attribute',1,'p_attribute','main.py',44),
  ('context -> ASSIGN','context',1,'p_assign','main.py',59),
  ('context -> COMMENT','context',1,'p_comment','main.py',65),
  ('context -> NEWLINE','context',1,'p_newline','main.py',70),
  ('context -> ELLIPSIS','context',1,'p_ellipsis','main.py',76),
  ('context -> TAB','context',1,'p_tab','main.py',80),
  ('context -> EXAMPLE','context',1,'p_example','main.py',86),
]
