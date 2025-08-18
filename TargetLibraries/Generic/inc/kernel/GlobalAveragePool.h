/* =====================================================================
 * Title:        GlobalAveragePool.h
 * Description:
 *
 * Date:         xx.xx.xxxx
 *
 * ===================================================================== */

/*
 * Copyright (C) 2023 ETH Zurich and University of Bologna.
 *
 * Authors:
 * - Mohammad.H Nikkhah
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

 #ifndef __DEEPLOY_BASIC_MATH_MAXPOOL_KERNEL_HEADER_
 #define __DEEPLOY_BASIC_MATH_MAXPOOL_KERNEL_HEADER_
 
 #include "DeeployBasicMath.h"
 
 /* DESCRIPTIONS
  *
  */
 
 /******************************************************************************/
 /*                         General MaxPool (8bit)                         */
 /******************************************************************************/
 
 /*
  * Global Average Pool  ----------------------------------
  * kernel      = GAPool_fp32_fp32_NCHW
  * layout      = NCHW
  * data type   = 8-bit integer
  * kernel size = generic
  * unrolling   = no
  * simd        = no
  */
 
void GAPool_fp32_fp32_NCHW(float32_t const *__restrict__ pSrcA, 
                            uint32_t C, uint32_t H, uint32_t W,
                            float32_t *__restrict__ pDstC);
                            
#endif //__DEEPLOY_BASIC_MATH_MAXPOOL_KERNEL_HEADER_
 