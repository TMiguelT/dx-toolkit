/*
 * Copyright (C) 2013 DNAnexus, Inc.
 *
 * This file is part of dx-toolkit (DNAnexus platform client libraries).
 *
 *   Licensed under the Apache License, Version 2.0 (the "License"); you may
 *   not use this file except in compliance with the License. You may obtain a
 *   copy of the License at
 *
 *       http://www.apache.org/licenses/LICENSE-2.0
 *
 *   Unless required by applicable law or agreed to in writing, software
 *   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 *   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 *   License for the specific language governing permissions and limitations
 *   under the License.
 */

#ifndef UA_COMPRESS_H
#define UA_COMPRESS_H

#include <zlib.h>

uLong gzCompressBound(uLong sourceLen);
int gzCompress(Bytef * dest, uLongf * destLen, const Bytef * source, uLong sourceLen, int level);

#endif
