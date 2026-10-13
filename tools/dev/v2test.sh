#!/bin/sh
# Compile and run all strict tests; stdout and exit status are both required.
# The products' suites live in their own repositories (usetin/tit, usetin/tinhub, usetin/tinland).
cd "$(dirname "$0")/../.." || exit 1
compiler=${1:-bin/tinc}
sh tools/ci/tin.sh suite "$compiler" || exit $?
# Diagnostic codes: the compiler, toolchain/docs/ERRORS.md and the .err files agree; examples compile as shown.
sh tools/ci/tin.sh diagnostics_check "$compiler" || exit $?
toolchain/tests/darwin.sh "$compiler" || exit $?
exec toolchain/tests/edition1.sh "$compiler"
