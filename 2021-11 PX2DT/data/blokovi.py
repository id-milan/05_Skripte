

b_pocetak = """INIT MASTER(S)
NASTRAN SYSTEM(442)=-1,SYSTEM(319)=1
ID model,FEMAP
SOL SESTATIC
CEND
  TITLE = Analiza
  ECHO = NONE
  DISPLACEMENT(PLOT) = ALL
  SPCFORCE(PLOT) = ALL
  OLOAD(PLOT) = ALL
  FORCE(PLOT,CORNER) = ALL
  STRESS(PLOT,CORNER) = ALL
  SPC = 1
  LOAD = 1
BEGIN BULK
$ ***************************************************************************
$   Written by : PX2DAT
$   Version    : 2021.2.0
$   Translator : PX2DAT
$   From Model :
$   Date       : Mon Nov 29 11:28:46 2021
$   Output To  :
$ ***************************************************************************
$
PARAM,PRGPST,NO
PARAM,POST,-1
PARAM,OGEOM,NO
PARAM,AUTOSPC,YES
PARAM,K6ROT,100.
PARAM,GRDPNT,0
CORD2C         1       0      0.      0.      0.      0.      0.      1.+FEMAPC1
+FEMAPC1      1.      0.      1.
CORD2S         2       0      0.      0.      0.      0.      0.      1.+FEMAPC2
+FEMAPC2      1.      0.      1.
***************************************************************************
"""

b_kraj = "ENDDATA"