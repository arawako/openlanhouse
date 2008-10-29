#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  
# Copyright (C) 2003-2006 Yann Le Boulanger <asterix@lagaule.org>
# Copyright (C) 2005-2006 Nikos Kouremenos <kourem@gmail.com>
#  Copyright (c) 2007-2008 Wilson Pinto Júnior <wilson@openlanhouse.org>

# Copyright (C) 2005
#      Dimitur Kirov <dkirov@gmail.com>
#      Travis Shirk <travis@pobox.com>
#
#  APTonCD - Copyright (c) 2006.
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import time
from hashlib import sha
from OpenlhClient.globals import *

def generate_id_bytime():
    
    
    cur_time = time.time()
    hash = sha(str(cur_time))
    
    return hash.hexdigest()
