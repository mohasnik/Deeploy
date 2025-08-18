# ----------------------------------------------------------------------
#
# File: GlobalAveragePoolTemplate.py
#
# Last edited: xxxx
#
# Copyright (C) 2021, ETH Zurich and University of Bologna.
#
# Author: Mohammad.H Nikkhah, EPFL
#
# ----------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the License); you may
# not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an AS IS BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from Deeploy.DeeployTypes import NetworkContext, NodeTemplate, OperatorRepresentation



# class _GlobalAveragePoolTemplate(NodeTemplate):
#     def __init__(self, templateStr: str):
#         super().__init__(templateStr)
    
#     def alignToContext(self, ctxt: NetworkContext, operatorRepresentation: OperatorRepresentation) -> Tuple[NetworkContext, OperatorRepresentation, List[str]]:
        




referenceTemplate = NodeTemplate("""
<%
    GAPInputSampleSize = C * H * W
    GAPOutputSampleSize = C                   
%>

// Global Average Pool (Name: ${nodeName}, Op: ${nodeOp})
BEGIN_SINGLE_CORE
    ${x_type.typeName} ref_${y}_${x} = ${x};
    ${y_type.typeName} ref_${y}_${y} = ${y};
                                 
    for (uint32_t n = 0; n < ${batch}; n++) {
        GAPool_fp${x_type.referencedType.typeWidth}_fp${y_type.referencedType.typeWidth}_NCHW (
            ref_${y}_${x},
            ${C}, ${H}, ${W},
            ref_${y}_${y}
        );
                                 
        ref_${y}_${x} += ${GAPInputSampleSize};
        ref_${y}_${y} += ${GAPOutputSampleSize};
    }
END_SINGLE_CORE
""")

# BEGIN_SINGLE_CORE
#     for (uint32_t i = 0; i < ${data_out_size}; i++) {
#         ${data_out}[i] = ${value};
#     }
#     uint32_t xoffset_${data_out}_${data_in};
#     uint32_t offset_in_${data_out}_${data_in} = 0;

#     % if channels_first:
#     // NCHW Layout
#     for(uint32_t n=0; n<${batch}; n++){
#         xoffset_${data_out}_${data_in} = n*${batchOffsetOut} + ${pad_y}*${dim_im_out_y}+${pad_x};
#         for (uint32_t c=0; c<${dim_im_in_ch}; ++c) {
#             for(uint32_t h=0; h<${dim_im_in_x}; h++){
#                 memcpy(${data_out} + xoffset_${data_out}_${data_in}, ${data_in}+offset_in_${data_out}_${data_in}, ${dim_im_in_y}*sizeof(${data_out_type.referencedType.typeName}));
#                 xoffset_${data_out}_${data_in} += ${dim_im_out_y};
#                 offset_in_${data_out}_${data_in} += ${dim_im_in_y};
#             }
#             xoffset_${data_out}_${data_in} += 2*${pad_y}*${dim_im_out_y};
#         }
#     }
#     % else:
#     // NHWC Layout
#     for(uint32_t n=0; n<${batch}; n++){
#         xoffset_${data_out}_${data_in} = n*${batchOffsetOut} + ${startPosX};
#         for(uint32_t h=0; h<${dim_im_in_x}; h++){
#             memcpy(${data_out}+xoffset_${data_out}_${data_in}, ${data_in}+offset_in_${data_out}_${data_in}, ${width}*sizeof(${data_out_type.referencedType.typeName}));
#             xoffset_${data_out}_${data_in} += ${addoffsetOut};
#             offset_in_${data_out}_${data_in} += ${addoffsetIn};
#         }
#     }
#     %endif
# END_SINGLE_CORE