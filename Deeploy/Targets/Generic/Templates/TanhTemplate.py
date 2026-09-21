# Copyright (C) 2026 EPFL.
# Solderpad Hardware License, Version 2.1, see LICENSE.md for details.
# SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
#
# File: Tanh.py
# Author: Mohammad Hossein Nikkhah
# Description: 


from typing import Dict, List, Tuple

from Deeploy.DeeployTypes import NetworkContext, NodeTemplate, OperatorRepresentation


referenceTemplate = NodeTemplate("""
// Tan (Name: ${nodeName}, Op: ${nodeOp})
    tanh_fp32(${data_in}, ${size}, ${data_out});
""")
