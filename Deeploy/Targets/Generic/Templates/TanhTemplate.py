# SPDX-FileCopyrightText: 2026 EPFL
#
# SPDX-License-Identifier: Apache-2.0
#
# File: Tanh.py
# Author: Mohammad Hossein Nikkhah
# Description:


from typing import Dict, List, Tuple

from Deeploy.DeeployTypes import NetworkContext, NodeTemplate, OperatorRepresentation


referenceTemplate = NodeTemplate("""
// Tan (Name: ${nodeName}, Op: ${nodeOp})
BEGIN_SINGLE_CORE
    tanh_fp32(${data_in}, ${size}, ${data_out});
END_SINGLE_CORE
""")
