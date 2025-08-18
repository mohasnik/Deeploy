/* =====================================================================
* Title:        GlobalAveragePool_fp32.c
* Description:
*
* Date:         xx.xx.xxxx
*
* ===================================================================== */

/*
* Copyright (C) 2022 ETH Zurich and University of Bologna.
*
* Authors:
* - Mohammad.H Nikkhah, EPFL
*
* SPDX-License-Identifier: Apache-2.0
*
* Licensed under the Apache License, Version 2.0 (the License); you may
* not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
* www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an AS IS BASIS, WITHOUT
* WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*/

#include "DeeployBasicMath.h"

void GAPool_fp32_fp32_NCHW(float32_t const *__restrict__ pSrcA, 
                                uint32_t C, uint32_t H, uint32_t W,
                                float32_t *__restrict__ pDstC) {

    for(uint32_t c = 0; c < C; c++) {
        float32_t average = 0.0;

        for(uint32_t h = 0; h < H; h++) {
            for(uint32_t w=0; w < W; w++) {
                average += pSrcA[c * H * W + h * W + w];
            }
        }

        pDstC[c] = average / (((float)H) * ((float)W));
    }

}

