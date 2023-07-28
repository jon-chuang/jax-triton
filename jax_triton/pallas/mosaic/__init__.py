# Copyright 2023 The jax_triton Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Module for Mosaic lowering of Pallas call."""

from jax_triton.pallas.mosaic import core
from jax_triton.pallas.mosaic import pallas_call_registration
from jax_triton.pallas.mosaic.core import PrefetchScalarGridSpec
from jax_triton.pallas.mosaic.core import TPUMemorySpace
from jax_triton.pallas.mosaic.primitives import repeat
from jax_triton.pallas.mosaic.primitives import trace


VMEM = TPUMemorySpace.VMEM
SMEM = TPUMemorySpace.SMEM
CMEM = TPUMemorySpace.CMEM
del pallas_call_registration