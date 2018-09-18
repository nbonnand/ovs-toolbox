#!/usr/bin/python3

#Copyright 2018 Nicolas Bonnand

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import (QFileDialog,QInputDialog,QAbstractScrollArea,QAbstractItemView,QDockWidget,QCompleter,QItemDelegate,QHeaderView,QDesktopWidget,QTreeView,QSizePolicy,QTableView)
from PyQt5.QtCore import (QTimer,QStringListModel,QSettings, QPoint, QSize, QVariant, QSortFilterProxyModel)
from PyQt5.QtGui import (QStandardItemModel,QStandardItem,QPixmap,QPalette)
from PyQt5.QtCore import QT_VERSION_STR
from PyQt5.Qt import PYQT_VERSION_STR
from sip import SIP_VERSION_STR
from PyQt5.QtCore import pyqtRemoveInputHook

import random
import sys
import time
import os
from os.path import expanduser
from pathlib import Path
from lxml import etree
import subprocess
import re
import tempfile
import inspect # for debugging
import json
import paramiko
import socket
import tarfile
import io
import platform

#for debugging only ( remove it)
from pprint import pprint
from pdb import set_trace
