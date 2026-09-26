# SPDX-FileCopyrightText: 2026 EPFL
#
# SPDX-License-Identifier: Apache-2.0
#
# File: xheep_config.cmake
# Author: Mohammad Hossein Nikkhah
# Description:

<%
  cpu = xheep.cpu()
%>


% if cpu.get_param("fpu"):
set(ISA rv32imfc_zicsr CACHE STRING "X-HEEP RISC-V ISA")
% else:
set(ISA rv32imc_zicsr CACHE STRING "X-HEEP RISC-V ISA")
% endif

