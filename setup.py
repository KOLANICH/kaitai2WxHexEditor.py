#!/usr/bin/env python3
import os
from setuptools import setup

from pathlib import Path
thisDir=Path(__file__).parent

formatsPath=thisDir / "kaitai_struct_formats"
kaitaiSetuptoolsCfg={
	"formats":{
		"xgboost.py": {
			"path":"scientific/data_science/dmlc/xgboost/xgboost.ksy",
		}
	},
	"formatsRepo": {
		"git": "https://github.com/KOLANICH/kaitai_struct_formats.git",
		"refspec": "xgboost",
		"localPath" : formatsPath,
		"update": True
	},
	"outputDir": thisDir / "pyxgboost" / "kaitai",
	"inputDir": formatsPath
}

setup(use_scm_version = True, kaitai=kaitaiSetuptoolsCfg)

